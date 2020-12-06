import asyncio

from pyrogram import Client, filters, emoji
from pyrogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from plate import Plate

app = Client("pyrolangbot")
plate = Plate()

USERS = {289579584: "de_DE"}  # Setting myself to Germany
DE = emoji.FLAG_GERMANY  # \U0001f1e9\U0001f1ea
US = emoji.FLAG_UNITED_STATES  # \U0001f1fa\U0001f1f8
IT = emoji.FLAG_ITALY  # \U0001f1ee\U0001f1f9


@app.on_message(filters.command("start") & filters.private)
async def start(app: Client, message: Message):
    if message.from_user.id in USERS:
        await message.reply_text(plate("hello", USERS[message.from_user.id]))
    else:
        await message.reply_text(
            "Language? Sprache? Linguaggio?",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton(DE), KeyboardButton(US), KeyboardButton(IT),]],
                resize_keyboard=True,
                one_time_keyboard=True,
            ),
        )


# Literally matching the fucking Unicode points of Emoji. Just because.
@app.on_message(filters.regex(f"({DE}|{US}|{IT})"))
async def set_lang(app: Client, message: Message):
    i = message.from_user.id
    if message.text == DE:
        USERS[i] = "de_DE"
    elif message.text == US:
        USERS[i] = "en_US"
    elif message.text == IT:
        USERS[i] = "it_IT"
    print(i, message.from_user.first_name, USERS[i])
    await start(app, message)


app.run()
