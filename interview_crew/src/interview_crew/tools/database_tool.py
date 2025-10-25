from crewai_tools import tool
import json, os

@tool("database_tool")
def save_to_memory(user_id: str, data: dict):
    """Save user interview data persistently to JSON."""
    os.makedirs("memory", exist_ok=True)
    file_path = f"memory/{user_id}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    return f"✅ Data saved for {user_id}"

