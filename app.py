from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from knowledge.knowledge_store import KnowledgeStore
from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from rag.rag_pipeline import RAGPipeline
from llm.llm_client import LLMClient


app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Initialize RAG pipeline
knowledge_store = KnowledgeStore()
retriever = Retriever(knowledge_store)
prompt_builder = PromptBuilder()
llm_client = LLMClient()

rag = RAGPipeline(retriever, prompt_builder, llm_client)


class ChatRequest(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(req: ChatRequest):

    response = rag.run(req.message)

    return {"reply": response}
