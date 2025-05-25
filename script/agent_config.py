from phi.agent import Agent
from phi.model.groq import Groq

agent = Agent(
    name="DocBot",
    role="Expert documentation assistant",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Be helpful and extract info from documentation.",
        "Use only context provided to answer queries."
    ],
    markdown=True
)
