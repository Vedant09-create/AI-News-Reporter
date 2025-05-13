from datetime import datetime
from crewai import Task
from tools import search_tools
from file_io import save_markdown

class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top AI news stories from the past 24 hours. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=False,
            expected_output="""A list of top AI news story titles and all details, URLs, and a brief summary for each story from the past 24 hours. 
                    A list of top AI news story titles, URLs, and a brief summary for each story from the past 24 hours. 
                Example Output: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...',
                    }, 
                    {{...}}
                ]
            """,

            execution_fn=lambda: search_tools.search_internet("Top AI news")
    )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=False,
            context=context,
            expected_output="""A detail format of each news story containig its title and summary .""",
            execution_fn=lambda: [
                {
                    "title": f"{item['title']}",
                    "summary": f"{item['summary']}"  # Fixed key casing to match output format
                }
                for item in context
            ]
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter with headlines and summaries',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A concise newsletter in markdown format, with just the title and summary of the news.
                Example Output:
                '# Top stories in AI today:\\n\\n
                - AI takes spotlight in Super Bowl commercials**: AI made a splash in this year\'s Super Bowl commercials...\\n
                - Altman seeks TRILLIONS for global AI chip initiative**: OpenAI CEO Sam Altman is reportedly angling to raise TRILLIONS of dollars...\\n
                \\n
                The summaries should focus on the key points of the news article and provide a brief but comprehensive insight into the story, with emphasis on the most important details in one or two lines.
                """,
            callback=save_markdown
        )

