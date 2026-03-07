from dataclasses import dataclass

@dataclass
class ChatRequest:
    user_id: str
    message: str


@dataclass
class ChatResponse:
    reply: str
