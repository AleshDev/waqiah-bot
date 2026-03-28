import os
import asyncio
from telegram import Bot


async def main():
    bot = Bot(token=os.environ["BOT_TOKEN"])
    chat_id = os.environ["CHAT_ID"]
    message = await bot.send_poll(
        chat_id=chat_id,
        question="Did you read Al-Waqiah today? 📖",
        options=["✅ Yes", "❌ No"],
        is_anonymous=False,
        allows_multiple_answers=False,
    )
    await bot.pin_chat_message(chat_id=chat_id, message_id=message.message_id)
    print("Poll sent and pinned!")


asyncio.run(main())
