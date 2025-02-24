from dotenv import load_dotenv
from anthropic import Anthropic
import os


load_dotenv()
client = Anthropic()

def generate_questions(topic, num_questions=3):
    stream = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        system=f"あなたは{topic}の専門家です。そのトピックについて、初学者が勉強になるような質問を生成します。",
        messages=[
            {"role": "user", "content": f"あなたは{topic}について、初学者が勉強になるような{num_questions}つの質問を生成してください。"}
        ],
        stop_sequences=[f"{num_questions+1}."],
        stream=True,
    )
    for event in stream:
        if event.type == "message_start":
            input_tokens = event.message.usage.input_tokens
            print("MESSAGE START EVENT", flush=True)
            print(f"Input tokens used: {input_tokens}", flush=True)
            print("========================")
        elif event.type == "content_block_delta":
            print(event.delta.text, flush=True, end="")
        elif event.type == "message_delta":
            output_tokens = event.usage.output_tokens
            print("\n========================", flush=True)
            print("MESSAGE DELTA EVENT", flush=True)
            print(f"Output tokens used: {output_tokens}", flush=True)

generate_questions("Python", 3)
