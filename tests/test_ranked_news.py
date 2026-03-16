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
    print("FINAL ANSWER:\n")
    print(result.get("final_answer"))
    print("\nRANKED ARTICLES:\n")

    articles = result.get("news_results", []) or result.get("web_results", [])
    for idx, article in enumerate(articles, start=1):
        print(
            f"{idx}. {article.get('title')} | "
            f"{article.get('source')} | "
            f"score={article.get('_score')}"
        )

    print("=" * 100)


if __name__ == "__main__":
    run_test("latest AI news")
    run_test("today's stock market news")
    run_test("latest champions league news")

