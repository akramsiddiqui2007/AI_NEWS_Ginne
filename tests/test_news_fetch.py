from src.state import NewsGenieState
from src.graph.workflow import newsgenie_graph


def run_test(query: str):
    state = NewsGenieState(user_query=query)
    result = newsgenie_graph.invoke(state)

    print("=" * 100)
    print("QUERY:", query)
    print("TYPE:", result.get("query_type"))
    print("CATEGORY:", result.get("selected_category"))
    print("ERROR:", result.get("error"))
    print("NEWS COUNT:", len(result.get("news_results", [])))
    print("WEB COUNT:", len(result.get("web_results", [])))
    print("FINAL ANSWER:\n")
    print(result.get("final_answer"))
    print("=" * 100)


if __name__ == "__main__":
    run_test("latest AI news")
    run_test("today's stock market news")
    run_test("Explain inflation and also give me today's finance news")

