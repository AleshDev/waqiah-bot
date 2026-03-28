import os
import asyncio
from telegram import Bot


async def main():
    bot = Bot(token=os.environ["BOT_TOKEN"])
    await bot.send_poll(
        chat_id=os.environ["CHAT_ID"],
        question="Did you read Al-Waqiah today? 📖",
        options=["✅ Yes", "❌ No"],
        is_anonymous=False,
        allows_multiple_answers=False,
    )
    print("Poll sent!")


asyncio.run(main())
