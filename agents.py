from crewai import Agent, LLM

nvidia_llm=LLM(
    model="nvidia/llama-3.1-nemotron-70b-instruct",
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = "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"
)

class AINewsLetterAgents():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Oversee the creation of the AI Newsletter',
            backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter
            not only informs but also engages and inspires the readers. """,
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )

    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top AI news stories for the day',
            backstory="""As a digital sleuth, you scour the internet for the latest and most impactful developments
            in the world of AI, ensuring that our readers are always in the know.""",
            verbose=True,
            allow_delegation=True,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed summary',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of AI news stories, making them accessible and engaging for our audience.""",
            #tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
            llm=nvidia_llm
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsCompiler',
            goal='Compile the analyzed news stories into a sequential, structured report format with clear sections for titles, summaries',
            backstory="""As the final architect of the report, you ensure that all news stories are formatted 
            into a cohesive, reader-friendly document with distinct sections, emphasizing clarity and structure.""",
            verbose=True,
            llm=nvidia_llm
    )

