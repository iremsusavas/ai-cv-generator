import openai

api_key = input("🔑 Please enter your OpenAI API key:\n(If you don’t have one, get it here: https://platform.openai.com/account/api-keys)\n> ")
openai.api_key = api_key

def generate_text(prompt, model="gpt-4-turbo"):

    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes professional CVs and cover letters."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
