from dotenv import load_dotenv
from anthropic import Anthropic
import os


load_dotenv()
client = Anthropic()

def generate_questions(topic, num_questions=3):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        system=f"あなたは{topic}の専門家です。そのトピックについて、初学者が勉強になるような質問を生成します。",
        messages=[
            {"role": "user", "content": f"あなたは{topic}について、初学者が勉強になるような{num_questions}つの質問を生成してください。"}
        ],
        stop_sequences=[f"{num_questions+1}."]
    )
    print(response.content[0].text)

generate_questions("Python", 3)
