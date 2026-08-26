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
#system_prompt = "You are a college physics professor. Give high priority to constraints"
system_prompt = build_system_prompt(
    mode="maestro_yaml_generator",
    app_id="com.apple.MobileAddressBook",
)
test_case = ("Open the Contacts app, add a new contact with a first (fill First name box) and last name (fill Last name box),"
             "then cancel (by pressing Cancel) and discard the changes (by pressing on Discard Changes), then go to the home screen (by pressing the home key")
#user_prompt = "Explain quantum computing in 2 sentences."
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": test_case},
    ],
)

print(response.choices[0].message.content)


