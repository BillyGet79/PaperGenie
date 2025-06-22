from dotenv import load_dotenv, find_dotenv
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionUserMessageParam, \
    ChatCompletionSystemMessageParam

from infrastructure.openai_client.openai_client import OpenAIClient


def setUpModule():
    load_dotenv(find_dotenv())


def to_message(role: str, content: str) -> ChatCompletionMessageParam:
    return {"role": role, "content": content}


class TestOpenAIClient:

    def test_get_client_chat(self):
        client = OpenAIClient.get_client()
        response = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                to_message("system", "You are a helpful assistant."),
                to_message("user", "What is the meaning of life?")
            ]
        )
        response_content = response.choices[0].message.content
        print(response_content)

    def test_get_client_embedding(self):
        client = OpenAIClient.get_client()
        response = client.embeddings.create(
            model="text-embedding-v4",
            input="What is the meaning of life?"
        )
        response_embedding = response.data[0].embedding
        print(response_embedding)
