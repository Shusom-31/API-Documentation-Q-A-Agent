from phi.agent import Agent
from phi.model.groq import Groq

agent = Agent(
    name="DocAI",
    model=Groq(id="llama-3.3-70b-versatile"),

    role = (
         "An intelligent, developer-focused assistant designed to answer technical queries by leveraging "
         "scraped and embedded API documentation. It effectively interprets developer questions, summarizes "
         "relevant API endpoints, and provides clear guidance on API usage and integration."
     ),

    description = (
        "This LLM-powered virtual assistant is trained to help developers understand, explore, and implement APIs with ease. "
        "It specializes in retrieving relevant documentation, interpreting user intent, and delivering accurate, "
        "developer-friendly responses to support efficient API development workflows."
     ),

    instructions=[
        "Be helpful and extract info from documentation.",
        "Use only context provided to answer queries."
    ],
    markdown=True
)
