from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from transformers.pipelines.conversational import Conversation


class Body(BaseModel):
    response: str
    arguments: Optional[Dict[str, Any]]
    tracker: Dict[str, Any]
    channel: Dict[str, str] = None


@dataclass
class Response:
    text: str
    buttons: List[Any] = field(default_factory=lambda: [])
    image: str = None
    elements: List[Any] = field(default_factory=lambda: [])
    attachments: List[Any] = field(default_factory=lambda: [])
    custom: Dict = field(default_factory=lambda: {})


def build_conversation(tracker: Dict[str, Any]) -> Conversation:
    events = tracker["events"]
    user_msgs = [e["text"] for e in events if e["event"] == "user"]
    bot_msgs = [e["text"] for e in events if e["event"] == "bot"]

    latest_user_msg = user_msgs[-1]
    user_hist = user_msgs[:-1]

    return Conversation(
        text=latest_user_msg, past_user_inputs=user_hist, generated_responses=bot_msgs
    )


app = FastAPI()
model_pipeline = pipeline(
    task="conversational", framework="pt", model="facebook/blenderbot-3B"
)


@app.post("/nlg")
def generate_response(body: Body = None):
    conv = build_conversation(body.tracker)
    bot_response_text = model_pipeline(conv).generated_responses[-1]
    return Response(text=bot_response_text)
