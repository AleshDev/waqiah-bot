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

    updates = await bot.get_updates()

    # Find the latest poll answer updates to collect who responded
    responded = set()
    for update in updates:
        if update.poll_answer:
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
