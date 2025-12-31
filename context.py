class ContextManager:
    def __init__(self, memory_instance):
        self.memory = memory_instance

    def retrieve_current_state(self):
        # Fetches the raw JSON and converts it to a usable object
        data = self.memory.get_context()
        return {
            "goal": data.get("user_goal", "Not Set"),
            "recent_activity": data.get("logs", [])[-1] if data.get("logs") else None
        }