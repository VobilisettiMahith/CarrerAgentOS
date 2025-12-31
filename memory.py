import json
import os

MEMORY_FILE = "memory.json"

class Memory:
    def __init__(self):
        if not os.path.exists(MEMORY_FILE):
            self.save_context({"user_goal": None, "logs": []})
    
    def get_context(self):
        try:
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}

    def save_context(self, data):
        with open(MEMORY_FILE, 'w') as f:
            json.dump(data, f, indent=4)
            
    def update_goal(self, goal):
        data = self.get_context()
        data["user_goal"] = goal
        self.save_context(data)

    def update_log(self, entry):
        data = self.get_context()
        if "logs" not in data:
            data["logs"] = []
        data["logs"].append(entry)
        self.save_context(data)