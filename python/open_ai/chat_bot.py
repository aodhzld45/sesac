import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPEN_AI_API_KEY')
URL = "https://api.openai.com/v1/chat/completions"

client = OpenAI(api_key=OPENAI_API_KEY)
async_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

MODEL = os.getenv("OPEN_AI_MODEL")

def main():
    messages = [
        {
            "role": "system",
            "content": (
                "드래곤볼의 프리저의 대표적인 대사는 제 전투력은 53만입니다만? 이걸 기억해,"
                "드래곤볼의 프리저 말투로 해주고 단답형으로 대답해줘"                
            ),
        }
    ]

    print("종료하시려면: /exit")

    while True:
        user_text = input("user: ").strip()
        if not user_text:
            continue

        if user_text.lower() in ["/exit", "exit", "quit", "/quit"]:
            print("종료!")
            break

        messages.append({"role": "user", "content": user_text})

        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
        )

        assistant_text = completion.choices[0].message.content or ""
        print(f"system: {assistant_text}\n")

        messages.append({"role": "assistant", "content": assistant_text})

if __name__ == "__main__":
    main()





