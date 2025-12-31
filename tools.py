from duckduckgo_search import DDGS

class ResearchTool:
    def scan_market(self, role):
        try:
            query = f"top technical skills required for {role} 2025"
            results = DDGS().text(query, max_results=3)
            return "\n".join([f"- {r['body']}" for r in results])
        except:
            return "Market Data Unavailable (Using Internal Knowledge)"