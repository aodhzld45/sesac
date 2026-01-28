import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
MODEL = os.getenv("OPEN_AI_MODEL", "gpt-4.1")  # 없으면 기본값
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

TMDB_BASE = "https://api.themoviedb.org/3"

def get_now_playing_movies(region : str = 'KR'):
    """TMDB API를 호출하여 현재 상영 중인 영화 목록을 가져옵니다."""

    print(f'{region}의 영화를 가져옵니다.')

    url = "https://api.themoviedb.org/3/movie/now_playing"
    
    params = {
        'language' : 'ko-kr',
        'region' : region
    }
    
    headers = {
        'Authorization' : f'Bearer {TMDB_API_KEY}'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()    
        return response.json()['results']
    except Exception as e:
        print(e)

TOOLS = [
    {
        "type": "function",
        "name": "get_now_playing_movies",
        "description": "TMDB에서 현재 상영작(now_playing) 데이터를 가져와서 주어진 질문에 맞게 대답한다.",
        "parameters": {
            "type": "object",
            "properties": {
                "language": {"type": "string", "description": "예: ko-KR, en-US"},
                "region": {"type": "string", "description": "예: KR, US"},
                "page": {"type": "integer", "description": "now_playing 페이지(기본 1)", "minimum": 1},
            },
            "required": [],
            "additionalProperties": False,
        },
    }
]

def main():
    input_messages = [
        {
            "role": "system",
            "content": (
                "드래곤볼의 프리저 말투로, 단답형에 가깝게 대답해.\n"
                "사용자가 '현재 상영', '상영작', 'now playing' 같은 요청을 하면 "
                "반드시 get_now_playing_movies 툴을 호출해서 실제 데이터를 근거로 답해."
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

        input_messages.append({"role": "user", "content": user_text})

        response = client.responses.create(
            model=MODEL,
            input=input_messages,
            tools=TOOLS,
        )

        while True:
            tool_calls = [item for item in response.output if item.type == "function_call"]
            if not tool_calls:
                break

            call = tool_calls[0]

            response = client.responses.create(
                model=MODEL,
                previous_response_id=response.id,
                input=[{
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": json.dumps(ensure_ascii=False),
                }],
                tools=TOOLS,
            )

        # 최종 텍스트 출력
        assistant_text = getattr(response, "output_text", "") or ""
        print(f"system: {assistant_text}\n")

        input_messages.append({"role": "assistant", "content": assistant_text})

if __name__ == "__main__":
    main()
