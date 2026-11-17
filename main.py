import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    print("Hello from python-ai!")

    load_dotenv()
    api_key=os.environ.get('OPENROUTER_API_KEY')
    if api_key == None:
        raise RuntimeError('api_key_error')

    client=OpenAI(
        base_url='https://openrouter.ai/api/v1',
        api_key=api_key,
    )

    response=client.chat.completions.create(
        model='openrouter/free',
        messages=[
            {
                'role':'user',
                'content':'Can you tell me how much response ive used today on openrouter?'
            }
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
