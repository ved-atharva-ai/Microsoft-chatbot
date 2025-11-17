# app.py
import os
from fastapi import FastAPI, Request
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from demo.bot import MyBot

app = FastAPI()

adapter = BotFrameworkAdapter(
    BotFrameworkAdapterSettings("", "")
)

bot = MyBot()


@app.post("/api/messages")
async def messages(request: Request):
    body = await request.json()
    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")

    async def call_bot(turn_context: TurnContext):
        await bot.on_turn(turn_context)

    return await adapter.process_activity(activity, auth_header, call_bot)
