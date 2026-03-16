from src.config import settings
from src.utils.helpers import get_llm_client


def main():
    print("---- NewsGenie Smoke Test ----")
    print(f"Provider: {settings.model_provider}")
    print(f"Environment: {settings.app_env}")
    print(f"Debug: {settings.debug}")

    try:
        settings.validate()
        print("Config validation: PASSED")
    except Exception as e:
        print(f"Config validation: FAILED -> {e}")
        return

    try:
        client = get_llm_client()
        reply = client.generate(
            system_prompt="You are a helpful assistant.",
            user_prompt="Reply with exactly: Setup works."
        )
        print("LLM call: PASSED")
        print("Model reply:", reply)
    except Exception as e:
        print(f"LLM call: FAILED -> {e}")


if __name__ == "__main__":
    main()

