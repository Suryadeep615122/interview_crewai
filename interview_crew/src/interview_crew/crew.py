from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from interview_crew.tools import web_search_tool, save_to_memory

@CrewBase
class InterviewCrew():
    """AI Interview Crew - manages the complete multi-agent workflow"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # === Agents ===
    @agent
    def interview_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_manager'], # type: ignore[index]
            tools=[web_search_tool],
            verbose=True
        )

    @agent
    def question_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['question_generator'], # type: ignore[index]
            tools=[web_search_tool],
            verbose=True
        )

    @agent
    def conversation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['conversation_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def response_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['response_evaluator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def feedback_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_coach'], # type: ignore[index]
            verbose=True
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'], # type: ignore[index]
            tools=[save_to_memory],
            verbose=True
        )

    @agent
    def memory_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['memory_agent'], # type: ignore[index]
            tools=[save_to_memory],
            verbose=True
        )

    @agent
    def coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['coordinator'], # type: ignore[index]
            verbose=True
        )

    # === Tasks ===
    @task
    def manage_interview_flow(self) -> Task:
        return Task(
            config=self.tasks_config['manage_interview_flow'], # type: ignore[index]
        )

    @task
    def generate_questions(self) -> Task:
        return Task(
            config=self.tasks_config['generate_questions'], # type: ignore[index]
        )

    @task
    def conduct_conversation(self) -> Task:
        return Task(
            config=self.tasks_config['conduct_conversation'], # type: ignore[index]
        )

    @task
    def evaluate_response(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_response'], # type: ignore[index]
        )

    @task
    def provide_feedback(self) -> Task:
        return Task(
            config=self.tasks_config['provide_feedback'], # type: ignore[index]
        )

    @task
    def generate_report(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report'], # type: ignore[index]
            output_file='interview_report.json'
        )

    # === Crew Definition ===
    @crew
    def crew(self) -> Crew:
        """Creates and configures the Interview Simulation Crew"""
        return Crew(
            agents=self.agents,      # all agents auto-loaded from above
            tasks=self.tasks,        # all tasks auto-loaded from above
            process=Process.sequential,  # or Process.parallel if needed
            verbose=True
        )
