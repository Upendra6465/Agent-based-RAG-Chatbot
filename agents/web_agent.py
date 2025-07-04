from duckduckgo_search import DDGS

class WebAgent:
    def search(self, query):
        with DDGS() as ddgs:
            results = ddgs.text(query)
            answers = [r.get("body", "") for r in results if "body" in r]
        return "🔎 Web Result:\n\n" + "\n\n".join(answers[:2]) if answers else "No web results found."