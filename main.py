import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    print("Hello from python-ai!")

    load_dotenv()
    api_key=os.environ.get('OPENROUTER_API_KEY')

    if api_key is None:
        raise RuntimeError('api_key_error')
    client=OpenAI(
        base_url='https://openrouter.ai/api/v1',
        api_key=api_key,
    )

    prompt='just testing, dont waste any more token.'

    response=client.chat.completions.create(
        model='openrouter/free',
        messages=[
            {
                'role':'user',
                'content':prompt,
            }
        ]
    )

    print('Prompt: ', prompt)

    if response.usage is None:
        raise RuntimeError('usage_empty')
    print('Prompt tokens: ',response.usage.prompt_tokens)
    print('Response tokens: ',response.usage.completion_tokens)

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
