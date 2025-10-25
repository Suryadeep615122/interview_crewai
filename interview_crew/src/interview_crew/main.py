#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from interview_crew.crew import InterviewCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
#!/usr/bin/env python

"""
This file serves as the main entry point for running the Interview Crew.
You can:
  - Run a normal interview flow with `run()`
  - Train and refine the crew with `train()`
  - Replay a past execution with `replay()`
  - Test and evaluate the crew with `test()`
"""

def run():
    """
    Run the interview crew with sample or dynamic inputs.
    """
    inputs = {
        "user_id": "user_001",
        "candidate_name": "Vishal",
        "job_role": "Software Engineer Intern",
        "topic": "AI and Data Structures",
        "difficulty": "Medium",
        "current_year": str(datetime.now().year),
    }

    try:
        print("🚀 Starting Interview Crew...\n")
        InterviewCrew().crew().kickoff(inputs=inputs)
        print("\n✅ Interview crew finished successfully.")
    except Exception as e:
        raise Exception(f"❌ Error while running the crew: {e}")


def train():
    """
    Train the interview crew for a given number of iterations.
    Usage: python main.py train <n_iterations> <output_filename>
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        InterviewCrew().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
        print(f"\n✅ Training completed and saved to {filename}")
    except Exception as e:
        raise Exception(f"❌ Error during training: {e}")


def replay():
    """
    Replay a previous interview crew execution from a specific task.
    Usage: python main.py replay <task_id>
    """
    try:
        task_id = sys.argv[1]
        InterviewCrew().crew().replay(task_id=task_id)
        print(f"\n✅ Replayed task {task_id} successfully.")
    except Exception as e:
        raise Exception(f"❌ Error during replay: {e}")


def test():
    """
    Test the crew for evaluation.
    Usage: python main.py test <n_iterations> <eval_llm_model>
    Example: python main.py test 3 gpt-4o-mini
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        n_iterations = int(sys.argv[1])
        eval_llm = sys.argv[2]
        InterviewCrew().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)
        print(f"\n✅ Testing completed with {n_iterations} iterations.")
    except Exception as e:
        raise Exception(f"❌ Error during testing: {e}")


if __name__ == "__main__":
    """
    Run this file with:
      python main.py run        → normal execution
      python main.py train 5 out.json  → training mode
      python main.py replay <task_id>  → replay mode
      python main.py test 2 gpt-4o-mini → testing mode
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py [run|train|replay|test]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print("Unknown command. Use one of: run | train | replay | test")
