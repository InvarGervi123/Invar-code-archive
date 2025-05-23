from openai import OpenAI

client = OpenAI()

gpt_behaviuor = 'You are help'

response = client.create_company(
    model="gpt-4-turbo",
    prompt="what is PI",
    max_tokens=100
    )