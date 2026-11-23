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
    parser.add_argument('prompt', type=str, help='User prompt')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args=parser.parse_args()

    messages=[
        {'role':'user', 'content':args.prompt},
    ]

    response=client.chat.completions.create(
        model='openrouter/free',
        messages=messages,
    )

    if response.usage is None:
        raise RuntimeError('usage_empty')
        
    if args.verbose:
        print('Prompt: ', args.prompt)
        print('Prompt tokens: ',response.usage.prompt_tokens)
        print('Response tokens: ',response.usage.completion_tokens)

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
