import os
from dotenv import load_dotenv
from openai import OpenAI
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "modular_prompt"))
from build_prompt import build_system_prompt
from make_yaml import save_yaml_flow

load_dotenv()

base_url = os.getenv("GOOGLE_URL")
api_key = os.getenv("GOOGLE")
model_name = os.getenv("GOOGLE_GEMMA")

client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)
contacts_app = "com.apple.MobileAddressBook"
calendar_app = "com.apple.mobilecal"
#system_prompt = "You are a college physics professor. Give high priority to constraints"
system_prompt = build_system_prompt(
    mode="maestro_yaml_generator_basic",
    app_id=calendar_app,
    platform="iOS",
)
test_case_1 = ("Open the Contacts app, go to 'All iPhone' folder. press 'Add' to add new contact. First fill 'First name'"
             "box with test_first_name and then fill 'Last name' box with test_last_name,"
             "then cancel (by pressing 'Cancel') and discard the changes (by pressing on 'Discard Changes'), then press"
             "'Lists', then go to the home screen (by pressing the home key).")
test_case_2 = ("open calendar app, add an event with 'Add'. then add title name as test_title in 'Title'."
               "select starting date by first going on '28-Aug-2026' and then select '29' to put date as "
               "27-August-2026. Then select time by first going on '4:00 PM'. Then scroll until you can see the element "
               "'20 minutes' and use speed of 100, timeout of 60000ms and visibility percentage as 20. To set repeat, go "
               " to 'Never' and change it to'Every Day' by picking that option. Then press 'Cancel'. To discard the"
               "changes, press 'Discard Changes'. Then press home key to go to the home screen.")
#user_prompt = "Explain quantum computing in 2 sentences."
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": test_case_2},
    ],
)

print(response.choices[0].message.content)

raw_output = response.choices[0].message.content
saved_path = save_yaml_flow(raw_output, filename="iOS_ai_test_2.1.yaml")
print(f"Saved flow to: {saved_path}")


