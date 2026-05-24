
import os
from langchain_groq import ChatGroq

# Read API key from environment variable `GROQ_API_KEY`.
# If you prefer a `.env` file, set the variable there or export it in your shell.
groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError(
        "GROQ_API_KEY environment variable is not set.\n"
        "Set it for the current PowerShell session:\n"
        "  $env:GROQ_API_KEY = '<your_key>'\n"
        "Run the app after that in the same session.\n"
        "Or set it persistently for future sessions:\n"
        "  setx GROQ_API_KEY '<your_key>'\n"
        "Then open a new terminal and run the app.\n"
        "Do not put the key directly in source code."
    )

llm = ChatGroq(
    temperature=0,
    groq_api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
)

