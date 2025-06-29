import unittest

from dotenv import load_dotenv, find_dotenv
from openai.types.chat import ChatCompletionMessageParam

from infrastructure.openai_client.openai_client import OpenAIClient


def setUpModule():
    load_dotenv(find_dotenv())


def to_message(role: str, content: str) -> ChatCompletionMessageParam:
    return {"role": role, "content": content}


class TestOpenAIClient(unittest.TestCase):

    def test_get_openai_client(self):
        client = OpenAIClient.get_client()
        messages: list[ChatCompletionMessageParam] = [
            to_message("system", "You are a helpful assistant."),
            to_message("user", "对于你来说，我是说中文你处理的比较好，还是我说英文你处理的比较好？")
        ]
        response = client.chat.completions.create(
            model="qwen-plus",
            messages=messages
        )
        response_content = response.choices[0].message.content
        print(response_content)
