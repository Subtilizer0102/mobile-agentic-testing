import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

base_url = os.getenv("GOOGLE_URL")
api_key = os.getenv("GOOGLE")
model_name = os.getenv("GOOGLE_GEMMA")

client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a college physics professor. Give high priority to constraints"},
        {"role": "user", "content": "Explain quantum computing in 2 sentences."}
    ],
)

print(response.choices[0].message.content)


