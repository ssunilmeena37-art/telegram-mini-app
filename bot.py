import os
import json
import telebot

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    user = {
        "id": message.from_user.id,
        "username": message.from_user.username,
        "name": message.from_user.first_name
    }

    users = []
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            users = json.load(f)

    if not any(u["id"] == user["id"] for u in users):
        users.append(user)

    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)

    bot.reply_to(message, f"Welcome {user['name']}!")

bot.infinity_polling()
