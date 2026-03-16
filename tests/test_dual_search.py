from src.state import NewsGenieState
from src.graph.workflow import newsgenie_graph


def run_test(chat_history, user_query, selected_category="general"):
    state = NewsGenieState(
        user_query=user_query,
        selected_category=selected_category,
        chat_history=chat_history,
    )
    result = newsgenie_graph.invoke(state)

    print("=" * 100)
    print("USER QUERY:", user_query)
    print("REWRITTEN QUERY:", result.get("rewritten_query"))
    print("EXPANDED QUERIES:", result.get("expanded_queries"))
    print("MEMORY CONTEXT:", result.get("memory_context"))
    print("TYPE:", result.get("query_type"))
    print("CATEGORY:", result.get("selected_category"))
    print("ERROR:", result.get("error"))

    articles = result.get("news_results", []) or result.get("web_results", [])
    print("ARTICLES:")
    for idx, article in enumerate(articles, start=1):
        print(
            f"{idx}. {article.get('title')} | "
            f"{article.get('source')} | "
            f"score={article.get('_score')}"
        )
    print("=" * 100)


if __name__ == "__main__":
    history_1 = [
        {"role": "user", "content": "latest AI news"},
        {"role": "assistant", "content": "Here are the latest AI updates."},
    ]
    run_test(history_1, "what about in Europe?", "technology")

    history_2 = [
        {"role": "user", "content": "today's stock market news"},
        {"role": "assistant", "content": "Here are today's market headlines."},
    ]
    run_test(history_2, "and in the US?", "finance")

    history_3 = [
        {"role": "user", "content": "latest champions league news"},
        {"role": "assistant", "content": "Here are the latest Champions League updates."},
    ]
    run_test(history_3, "give me more on Arsenal", "sports")

