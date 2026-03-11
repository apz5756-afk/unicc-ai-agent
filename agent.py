import os
from typing import List

from openai import OpenAI
from dotenv import load_dotenv


SYSTEM_PROMPT = """You are AIna, a concise and helpful AI assistant.
Answer clearly, ask follow-up questions when needed, and keep responses practical.
"""


def load_config() -> tuple[str, str]:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        raise SystemExit(
            "Missing OPENAI_API_KEY. Add it to your environment before running the agent."
        )

    return api_key, model


def create_client() -> OpenAI:
    api_key, _ = load_config()
    return OpenAI(api_key=api_key)


def build_input(history: List[dict], user_message: str) -> List[dict]:
    conversation = list(history)
    conversation.append({"role": "user", "content": user_message})
    return conversation


def get_reply(client: OpenAI, model: str, history: List[dict], user_message: str) -> str:
    response = client.responses.create(
        model=model,
        input=build_input(history, user_message),
    )
    return response.output_text.strip()


def main() -> None:
    _, model = load_config()
    client = create_client()
    history: List[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("AIna is ready. Type 'exit' to quit.")

    while True:
        user_message = input("You: ").strip()
        if not user_message:
            continue
        if user_message.lower() in {"exit", "quit"}:
            print("AIna: Goodbye.")
            break

        answer = get_reply(client, model, history, user_message)
        print(f"AIna: {answer}")

        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
