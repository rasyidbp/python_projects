import os, argparse
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

    parser=argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('prompt', type=str, help='User_prompt')
    args=parser.parse_args()

    response=client.chat.completions.create(
        model='openrouter/free',
        messages=[
            {
                'role':'user',
                'content':args.prompt,
            }
        ]
    )

    print('Prompt: ', args.prompt)

    if response.usage is None:
        raise RuntimeError('usage_empty')
    print('Prompt tokens: ',response.usage.prompt_tokens)
    print('Response tokens: ',response.usage.completion_tokens)

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
