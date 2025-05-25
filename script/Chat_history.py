import json
from datetime import datetime
import os

HISTORY_FILE = "chat_history.jsonl"

def save_chat_entry(user_input, bot_response):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "bot": bot_response
    }
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def load_chat_history(limit=50):
    if not os.path.exists(HISTORY_FILE):
        return []

    history = []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                history.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue

    return history[-limit:]  # return last `limit` messages
