import os
import asyncio
from openai import OpenAI
from config import settings
from prompt_utils import format_prompt

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=settings.HF_TOKEN,
)

async def get_claude_answer(question: str) -> str:
    prompt = format_prompt(question)
    completion = await asyncio.to_thread(
        client.chat.completions.create,
        model="deepseek-ai/DeepSeek-V3-0324:together",
        messages=[
            {"role": "system", "content": "You are a travel documentation assistant. Answer the following question in a helpful, organized format."},
            {"role": "user", "content": question}
        ],
    )
    return completion.choices[0].message.content

async def stream_claude_answer(question: str):
    prompt = format_prompt(question)
    def sync_stream():
        return client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324:together",
            messages=[
                {"role": "system", "content": "You are a travel documentation assistant. Answer the following question in a helpful, organized format."},
                {"role": "user", "content": question}
            ],
            stream=True
        )
    stream = await asyncio.to_thread(sync_stream)
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield f"data: {delta}\n\n"
    yield "data: [DONE]\n\n" 