# Pyrogram Language Switch

Basically just an example on how to switch the language of your bot dynamically.

## Requirements

[Async Pyrogram](https://github.com/pyrogram/pyrogram) (to run the actual bot),
[`tgcrypto`](https://github.com/pyrogram/tgcrypto) for faster crypto, and
[Plate](https://github.com/delivrance/plate) to chose the correct language files.

## Setup

As per the documentation of [Pyrogram](https://docs.pyrogram.org/intro/setup) and [Plate](https://github.com/delivrance/plate#setup).

*Keep in mind that you will need Telegram [API Keys](https://my.telegram.org/apps) and a [Bot Token](https://t.me/BotFather) for Pyrogram.*

## How it works

Upon start we just check if the user is already in our dictionary that consists of a user_id and their chosen language
code (e.g. `"de_DE"` for German). If they are not yet in this dictionary, we simply send a message asking for their
language and present a ReplyKeyboard with Emoji representing the languages they can choose from. Then we just have a
MessageHandler that catches the Unicode points of the Emoji and add their user_id and their chosen language code to the
dictionary. Afterwards we can just rely on this value. If you need, you can add more or different languages.

## Modifying and License (I guess?)

I'm not licensing this at all. Do as you please. Credit is highly appreciated, but not required.

If you want to add more or different languages, refer to Plate's documentation (or rather its [Readme](https://github.com/delivrance/plate#plate) lol).
