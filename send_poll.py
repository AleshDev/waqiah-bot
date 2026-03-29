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
    # Save poll ID so remind.py only checks answers for this poll
    with open("poll_id.txt", "w") as f:
        f.write(message.poll.id)
    print(f"Poll sent and pinned! Poll ID: {message.poll.id}")


asyncio.run(main())
