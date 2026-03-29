import os
import asyncio
from telegram import Bot

MEMBERS = [
    "aleshnasx",
    "Rakhatuly_Imangali",
    "aidohn",
    "AsaRJ24",
    "insaneinnsan",
    "akmaralh",
]


async def main():
    bot = Bot(token=os.environ["BOT_TOKEN"])
    chat_id = os.environ["CHAT_ID"]

    # Read today's poll ID
    try:
        with open("poll_id.txt") as f:
            today_poll_id = f.read().strip()
    except FileNotFoundError:
        print("No poll_id.txt found — poll may not have been sent today")
        return

    updates = await bot.get_updates()

    # Only count answers for today's specific poll
    responded = set()
    for update in updates:
        if update.poll_answer and update.poll_answer.poll_id == today_poll_id:
            user = update.poll_answer.user
            if user.username:
                responded.add(user.username.lower())

    missing = [m for m in MEMBERS if m.lower() not in responded]

    if missing:
        tags = " ".join(f"@{u}" for u in missing)
        await bot.send_message(
            chat_id=chat_id,
            text=f"You haven't voted yet! 📖\n{tags}",
        )
        print(f"Reminded: {missing}")
    else:
        print("Everyone voted!")


asyncio.run(main())
