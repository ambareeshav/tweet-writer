# src/main.py
from .crews import TwitterContentCrew

def run(topic: str) -> str:
    inputs = {
        'topic': topic
    }
    return TwitterContentCrew().crew().kickoff(inputs=inputs).raw

