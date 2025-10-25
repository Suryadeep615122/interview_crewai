from crewai_tools import tool
import os
import requests

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

@tool("Web Search Tool")
def web_search_tool(query: str) -> str:
    """Uses Google Search (Serper) to find recent and relevant information."""
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