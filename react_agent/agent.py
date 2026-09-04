import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
curr = 0
max_iter = 10

while True:
    curr+=1
    if curr >= max_iter:
        print("Iteration limit reached")
        break
    



