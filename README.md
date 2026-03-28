# Al-Waqiah Daily Poll Bot

Telegram bot that sends a daily poll at 19:00 (Almaty time) asking if you read Surah Al-Waqiah.

## Setup

### 1. Create the bot

1. Open Telegram, search for **@BotFather**
2. Send `/newbot`, follow the prompts, pick a name and username
3. Copy the **bot token** you receive

### 2. Get the chat ID

1. Add your bot to the target group/channel **as an admin**
2. Send any message in that group
3. Open in your browser:
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```
4. Find `"chat":{"id": ...}` in the JSON response — that number is your **chat ID**
   - For channels it usually starts with `-100`

### 3. Deploy to Railway (free)

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) and sign in with GitHub
3. Click **New Project** → **Deploy from GitHub repo** → select this repo
4. Go to **Variables** tab and add:
   - `BOT_TOKEN` = your bot token
   - `CHAT_ID` = your chat/channel ID
5. Railway detects the `Procfile` automatically and runs the worker

The bot will now send the poll every day at 19:00 Almaty time.

## Local testing

```bash
export BOT_TOKEN="your-token"
export CHAT_ID="your-chat-id"
pip install -r requirements.txt
python bot.py
```
