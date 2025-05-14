import openai
import os
from dotenv import load_dotenv
load_dotenv()


client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt():
    user_input = input("고은이에게 뭐든 물어보세요 ♡: ")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("\n💬 GPT의 답변:")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"❗ 오류 발생: {str(e)}")

if __name__ == "__main__":
    while True:
        chat_with_gpt()
        print("\n---\n")
