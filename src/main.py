# src/main.py
from .crews import TwitterContentCrew, TwitterPostCrew

def draft(topic: str) -> str:
    inputs = {
        'topic': topic
    }
    return TwitterContentCrew().draft_crew().kickoff(inputs=inputs).raw

def post(drafts: str, choice:str) -> str:
    inputs = {
        'draft': drafts,
        'choice': choice
    }
    return TwitterPostCrew().post_crew().kickoff(inputs=inputs).raw

