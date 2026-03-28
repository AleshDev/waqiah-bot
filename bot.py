import os
import logging
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

bot = Bot(token=BOT_TOKEN)


async def send_poll():
    await bot.send_poll(
        chat_id=CHAT_ID,
        question="Did you read Al-Waqiah today? 📖",
        options=["✅ Yes", "❌ No"],
        is_anonymous=False,
        allows_multiple_answers=False,
    )
    logger.info("Poll sent successfully")


def job():
    asyncio.run(send_poll())


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(
        job,
        CronTrigger(hour=19, minute=0, timezone="Asia/Almaty"),
    )
    logger.info("Bot started. Poll scheduled daily at 19:00 Asia/Almaty.")
    scheduler.start()


if __name__ == "__main__":
    main()
