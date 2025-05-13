from crewai_tools import SerperDevTool
from crewai import Crew, Process, LLM
from dotenv import load_dotenv
import os
from tasks import AINewsLetterTasks
from agents import AINewsLetterAgents
from file_io import save_markdown
from openai import OpenAI

os.environ["OTEL_SDK_DISABLED"]="true"
# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("SERPER_API_KEY")

# Initialize the SerperDevTool
tool = SerperDevTool(
    search_url="https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en",
    api_key=api_key,
    n_results=5,  # Set a higher limit to get enough results to choose from
)

# Initialize the NVIDIA LLM for the agents
nvidia_llm = LLM(
    model="nvidia/llama-3.1-nemotron-70b-instruct",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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",
)

# Initialize agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Instantiate the agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# Create tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(newsletter_compiler, [analyze_news_task], save_markdown)

# Define the Crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=nvidia_llm,
    verbose=True
)

# Kick off the Crew's work
result = crew.kickoff()

# Print the results of the workflow
print("Crew Work Results:")
print(result)
try:
    output_file = "newsletter_output.md"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(result))  # Convert results to string if it's not already
    print(f"Results saved successfully in '{output_file}'.")
except Exception as e:
    print(f"Error saving results to file: {e}")