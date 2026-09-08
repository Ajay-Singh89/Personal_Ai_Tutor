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

        messages = [
        SystemMessage(
            content="""
            You are a helpful and patient AI tutor.
            Explain concepts clearly and simply.
            Adapt your explanations to the student's level.
            Use examples when helpful.
            Encourage the student to understand the concept rather than
            simply giving them the answer.
            """
        ),

        HumanMessage(content=user_messages)
    ]

    response = await llm.ainvoke(message)

    return response.content[0]["text"]