from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from composio_crewai import ComposioToolSet, Action
from crewai import Agent
import litellm, os

import dotenv
dotenv.load_dotenv()

litellm.api_key = os.environ.get("OPENAI_API_KEY")

toolset = ComposioToolSet(entity_id="Testing")
search_tool = toolset.get_tools(actions=[Action.TAVILY_TAVILY_SEARCH])
tweet_tool = toolset.get_tools(actions=[Action.TWITTER_CREATION_OF_A_POST])

@CrewBase
class TwitterContentCrew:
    """TwitterContentCrew"""

    agents_config = 'config/drafts/agents.yaml'
    tasks_config = 'config/drafts/tasks.yaml'

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'],
            llm="openai/gpt-4o-mini",
            tools=search_tool,
            verbose=True
        )

    @agent
    def drafting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['drafting_agent'],
            llm="openai/gpt-4o-mini",
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def drafting_task(self) -> Task:
        return Task(
            config=self.tasks_config['drafting_task'],
        )
    
    @crew
    def draft_crew(self) -> Crew:
        """Creates the TwitterContentCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical
        )

    
@CrewBase
class TwitterPostCrew:
    """TwitterPostCrew"""

    agents_config = 'config/post/agents.yaml'
    tasks_config = 'config/post/tasks.yaml'

    @agent
    def posting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['posting_agent'],
            llm="openai/gpt-4o-mini",
            tools=tweet_tool,
            verbose=True
        )

    @task
    def posting_task(self) -> Task:
        return Task(
            config=self.tasks_config['posting_task'],
        )

    @crew
    def post_crew(self) -> Crew:
        """Creates the TwitterContentCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical
        )