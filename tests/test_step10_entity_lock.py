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
    print("ENTITIES:", result.get("detected_entities"))
    print("TIMEFRAME:", result.get("detected_timeframe"))
    print("CONFIDENCE:", result.get("confidence_label"), result.get("confidence_score"))
    print("COVERAGE NOTE:", result.get("coverage_note"))
    print("ERROR:", result.get("error"))

    articles = result.get("news_results", []) or result.get("web_results", [])
    print("ARTICLE COUNT:", len(articles))
    for idx, article in enumerate(articles, start=1):
        print(
            f"{idx}. {article.get('title')} | "
            f"{article.get('source')} | "
            f"score={article.get('_score')}"
        )
    print("=" * 100)


if __name__ == "__main__":
    run_test([], "latest OpenAI news in Europe", "technology")
    run_test([], "today's S&P 500 and Nasdaq news", "finance")

    history = [
        {"role": "user", "content": "latest champions league news"},
        {"role": "assistant", "content": "Here are the latest Champions League updates."},
    ]
    run_test(history, "give me more on Arsenal", "sports")

