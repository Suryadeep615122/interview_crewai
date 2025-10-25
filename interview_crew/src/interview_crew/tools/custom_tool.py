from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import os
import requests


SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def google_search(query: str) -> str:
    """Perform a web search using Serper (Google Search API)."""
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        results = response.json().get("organic", [])
        top_results = "\n".join([r["snippet"] for r in results[:5]])
        return top_results if top_results else "No relevant results found."
    else:
        return f"Error: {response.text}"

# Create a tool instance for the agents to use
web_search_tool = Tool(
    name="Web Search Tool",
    description="Uses Google Search (Serper) to find recent and relevant information.",
    func=google_search
)


