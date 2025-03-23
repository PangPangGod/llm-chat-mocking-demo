import pytest

from langchain_core.messages import HumanMessage
from langchain_core.language_models.fake_chat_models import (
    FakeListChatModel,
    FakeChatModel,
)


def test_chat():
    model = FakeListChatModel(responses=["Hello World!"])
    ai_message = model.invoke("What is most famous programming quote?")
    assert ai_message.content == "Hello World!"


def test_sync_call_returns_fake_response():
    model = FakeChatModel()
    message = HumanMessage(content="Hello?")
    result = model._call([message])
    assert result == "fake response"


@pytest.mark.asyncio
async def test_async_generate_returns_fake_response():
    model = FakeChatModel()
    message = HumanMessage(content="Hello?")
    result = await model._agenerate([message])

    assert result.generations[0].message.content == "fake response"
    assert result.generations[0].message.type == "ai"
