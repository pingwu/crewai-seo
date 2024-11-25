from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class MarketingSEOCrew:
    """MarketingSEO crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def director_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["director_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=True,
            verbose=True,
        )

    @agent 
    def manager_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["manager_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def editor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["editor_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def review_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["review_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def publisher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["publisher_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def calendar_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["calendar_agent"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def keyword_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["keyword_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def analytics_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analytics_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def qa_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["qa_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def strategic_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["strategic_planning_task"],
            agent=self.director_agent(),
        )

    @task 
    def workflow_coordination_task(self) -> Task:
        return Task(
            config=self.tasks_config["workflow_coordination_task"],
            agent=self.manager_agent(),
        )

    @task
    def content_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_optimization_task"],
            agent=self.editor_agent(),
        )

    @task
    def content_review_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_review_task"], 
            agent=self.review_agent(),
        )

    @task
    def content_publishing_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_publishing_task"],
            agent=self.publisher_agent(),
        )

    @task
    def schedule_management_task(self) -> Task:
        return Task(
            config=self.tasks_config["schedule_management_task"],
            agent=self.calendar_agent(),
        )

    @task
    def keyword_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["keyword_research_task"],
            agent=self.keyword_agent(),
        )

    @task
    def performance_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["performance_analysis_task"],
            agent=self.analytics_agent(),
        )

    @task
    def quality_assurance_task(self) -> Task:
        return Task(
            config=self.tasks_config["quality_assurance_task"],
            agent=self.qa_agent(),
            output_file="qa_report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingSEO crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
