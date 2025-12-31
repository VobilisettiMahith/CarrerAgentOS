from llm import RealLLM

class Recommender:
    def __init__(self):
        self.llm = RealLLM()

    def generate_adaptive_plan(self, role, metrics):
        gap = metrics.get('focus_gap') 
        
        system_prompt = "You are an Expert Career Strategist. Write a short, bulleted action plan."
        
        user_prompt = f"""
        Role: {role}
        Detected Bloom's Level: {gap}
        User Journal: "{metrics.get('raw_input')}"
        
        INSTRUCTIONS:
        - If 'RECALL_GAP': Suggest Spaced Repetition (Anki) & Cheat Sheets.
        - If 'CONCEPT_GAP': Suggest Analogy Videos (YouTube) & Diagrams.
        - If 'APPLICATION_GAP': Suggest Debugging Drills & LeetCode Easy.
        - If 'SYNTHESIS': Suggest Capstone Projects.
        
        Output Format: Clear bullet points with specific resources.
        """
        return self.llm.generate(system_prompt, user_prompt)