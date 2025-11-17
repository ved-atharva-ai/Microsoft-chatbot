from botbuilder.core import ActivityHandler, TurnContext
from agent import LangChainAgent
import json
from dotenv import load_dotenv
load_dotenv()
import os
class MyBot(ActivityHandler):
    def __init__(self):
        api_key = os.getenv(API_KEY)
        self.agent = LangChainAgent(api_key)

    async def on_message_activity(self, turn_context: TurnContext):
        user_msg = turn_context.activity.text

        reply = self.agent.run(user_msg)

        # FIX: Convert any dict/list to string
        if isinstance(reply, (dict, list)):
            reply = json.dumps(reply, indent=2)

        await turn_context.send_activity(reply)
