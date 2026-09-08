import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# Create Gemini LLM
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)


# --------------------------------------------------
# Agent function
# --------------------------------------------------

async def run_agent(user_message: str):

    response = await llm.ainvoke(user_message)

    return response.content[0]["text"]