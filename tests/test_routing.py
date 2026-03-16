from src.state import NewsGenieState
from src.graph.workflow import newsgenie_graph


def run_test(query: str):
    state = NewsGenieState(user_query=query)
    result = newsgenie_graph.invoke(state)

    print("=" * 80)
    print("QUERY:", query)
    print("TYPE:", result.get("query_type"))
    print("CATEGORY:", result.get("selected_category"))
    print("REASON:", result.get("route_reason"))
    print("FINAL ANSWER:\n", result.get("final_answer"))
    print("=" * 80)


if __name__ == "__main__":
    run_test("Who is the CEO of Microsoft?")
    run_test("What are the latest technology news updates?")
    run_test("Explain what inflation means and also give me today's finance news.")
    run_test("What happened in the Champions League recently?")

