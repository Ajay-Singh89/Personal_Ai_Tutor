from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent.agent import run_agent


# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI()


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# --------------------------------------------------
# Request schema
# --------------------------------------------------

class ChatRequest(BaseModel):
    message: str


# --------------------------------------------------
# Chat endpoint
# --------------------------------------------------

@app.post("/chat")
async def chat(request: ChatRequest):

    # Get message from frontend
    user_message = request.message

    # Send message to the agent
    ai_response = await run_agent(user_message)

    # Send response back to frontend
    return {
        "response": ai_response
    }