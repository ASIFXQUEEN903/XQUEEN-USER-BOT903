import random
import time
import requests
from ... import app, SUDO_USER
from ... import *


from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(cdz(["ai"])  & (filters.me | filters.user(SUDO_USER))
)
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n/chatgpt Where is TajMahal?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                # Check if "results" key is present in the JSON response
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f" {x}      ᴀɴsᴡᴇʀɪɴɢ ʙʏ ➛  @ARAME9",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"**á´‡Ê€Ê€á´Ê€: {e} ")


__NAME__ = " Aɪ Cʜᴀᴛɢᴘᴛ"
__MENU__ = """
`.ai` - **Example:.chatgpt Where is Punjab?.**
`.cc` - **Some Live Generated CC.**
`.image` - **give image name for search .**
`.rmbg` - **Reply only to a photo to Remove it's Background.**
"""
