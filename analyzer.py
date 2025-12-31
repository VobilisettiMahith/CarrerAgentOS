from llm import RealLLM
import json

class LogAnalyzer:
    def __init__(self):
        self.llm = RealLLM()

    def analyze_log(self, user_text):
        """
        Analyzes the student's journal and provides EVIDENTIAL reasoning.
        """
        system_prompt = """
        You are an AI Pedagogy Expert. Analyze the student's journal using Bloom's Taxonomy.
        
        1. CLASSIFY the Cognitive State:
           - "RECALL_GAP": Forgetting names/syntax. (Score: 30-45)
           - "CONCEPT_GAP": Confused by logic/theory. (Score: 45-60)
           - "APPLICATION_GAP": Bugs, errors, code crashes. (Score: 60-75)
           - "SYNTHESIS": Success/Mastery. (Score: 80-100)
           
        2. GENERATE ANALYSIS (The "How"):
           - Write a short, single sentence explaining your logic.
           - MUST quote specific keywords the user wrote to prove you read it.
           - Example: "Since you mentioned 'syntax errors' and 'bugs', I detected an Application Gap."

        OUTPUT JSON ONLY:
        {
            "score": <int>, 
            "focus_gap": "GAP_NAME",
            "reasoning": "I detected terms like '...' which indicates ..."
        }
        """
        
        response = self.llm.generate(system_prompt, f"Student Update: '{user_text}'")
        
        try:
            start = response.find("{")
            end = response.rfind("}") + 1
            return json.loads(response[start:end])
        except:
            return {
                "score": 50, 
                "focus_gap": "GENERAL", 
                "reasoning": "Analysis failed to parse specific keywords."
            }