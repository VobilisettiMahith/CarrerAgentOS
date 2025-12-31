from llm import RealLLM
from memory import Memory
from tools import ResearchTool
from analyzer import LogAnalyzer
from recommender import Recommender
import statistics

class SupervisorAgent:
    def __init__(self):
        self.memory = Memory()
        self.researcher = ResearchTool()
        self.llm = RealLLM()
        self.analyzer = LogAnalyzer()
        self.recommender = Recommender()
        
    def calculate_velocity(self, history):
        if len(history) < 2: return "Stable"
        scores = [log.get("metrics", {}).get("score", 0) for log in history]
        avg = statistics.mean(scores)
        current = scores[-1]
        return f"Velocity: {current - avg:+.1f}"

    def create_roadmap(self, role):
        history = self.memory.get_context().get("logs", [])
        velocity = self.calculate_velocity(history)
        market_data = self.researcher.scan_market(role)
        self.memory.update_goal(role)
        
        system = "You are a Career Architect."
        prompt = f"""
        Target: {role}
        User Velocity: {velocity}
        Market Data: {market_data}
        Task: Create a roadmap.
        """
        return self.llm.generate(system, prompt)

    def run_adaptive_cycle(self, user_text):
        # 1. Analyze
        analysis = self.analyzer.analyze_log(user_text)
        
        # 2. Package Metrics
        metrics = {
            "score": analysis.get("score", 50),
            "focus_gap": analysis.get("focus_gap", "GENERAL"),
            "reasoning": analysis.get("reasoning", "No analysis provided."),
            "raw_input": user_text
        }
        
        # 3. Update Memory
        self.memory.update_log({"action": "weekly_review", "metrics": metrics})
        
        # 4. Generate Plan
        role = self.memory.get_context().get("user_goal", "General")
        return self.recommender.generate_adaptive_plan(role, metrics)