from asyncio.queues import QueueEmpty
from pyrogram import filters

from ... import *
from ...modules.mongo.streams import *
from ...modules.utilities import queues

# Audio Player
@app.on_message(cdz(["ply", "play"]) & ~filters.private)
@sudo_users_only
async def audio_stream(client, message):
    chat_id = message.chat.id
    aux = await eor(message, "**Processing ...**")
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    type = "Audio"
    try:
        if audio:
            await aux.edit("Downloading ...")
            file = await client.download_media(message.reply_to_message)
        else:
            if len(message.command) < 2:
                return await aux.edit("**🥀 ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ\nᴘʟᴀʏ ᴍᴜsɪᴄ ᴏʀ ᴠɪᴅᴇᴏ❗...**")
            query = message.text.split(None, 1)[1].split("?si=")[0] if "?si=" in message.text else message.text.split(None, 1)[1]
            results = await get_result(query)
            link = results[0]
            file = await get_stream(link, type)

        try:
            a = await call.get_call(chat_id)
            if a.status == "not_playing":
                stream = await run_stream(file, type)
                await call.change_stream(chat_id, stream)
                await aux.edit("Playing!")
            elif a.status in ["playing", "paused"]:
                position = await queues.put(chat_id, file=file, type=type)
                await aux.edit(f"Queued At {position}")
        except Exception as e:
            if "not joined" in str(e).lower():
                stream = await run_stream(file, type)
                await call.join_group_call(chat_id, stream)
                await aux.edit("Playing!")
            else:
                print(f"Error: {e}")
                return await aux.edit("**Please Try Again !**")
    except Exception as e:
        print(f"Error: {e}")
        return await aux.edit("**Please Try Again !**")

# Video Player
@app.on_message(cdz(["vply", "vplay"]) & ~filters.private)
@sudo_users_only
async def video_stream(client, message):
    chat_id = message.chat.id
    aux = await eor(message, "**Processing ...**")
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    type = "Video"
    try:
        if video:
            await aux.edit("Downloading ...")
            file = await client.download_media(message.reply_to_message)
        else:
            if len(message.command) < 2:
                return await aux.edit("**🥀 ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ\nᴘʟᴀʏ ᴍᴜsɪᴄ ᴏʀ ᴠɪᴅᴇᴏ❗...**")
            query = message.text.split(None, 1)[1].split("?si=")[0] if "?si=" in message.text else message.text.split(None, 1)[1]
            results = await get_result(query)
            link = results[0]
            file = await get_stream(link, type)

        try:
            a = await call.get_call(chat_id)
            if a.status == "not_playing":
                stream = await run_stream(file, type)
                await call.change_stream(chat_id, stream)
                await aux.edit("Playing!")
            elif a.status in ["playing", "paused"]:
                position = await queues.put(chat_id, file=file, type=type)
                await aux.edit(f"Queued At {position}")
        except Exception as e:
            if "not joined" in str(e).lower():
                stream = await run_stream(file, type)
                await call.join_group_call(chat_id, stream)
                await aux.edit("Playing!")
            else:
                print(f"Error: {e}")
                return await aux.edit("**Please Try Again !**")
    except Exception as e:
        print(f"Error: {e}")
        return await aux.edit("**Please Try Again !**")

# Audio Player (Play From Anywhere)
@app.on_message(cdz(["cply", "cplay"]))
@sudo_users_only
async def audio_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message, "**🥀 Please Set A Chat To Start Stream❗**")

    aux = await eor(message, "**Processing ...**")
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    type = "Audio"
    try:
        if audio:
            await aux.edit("Downloading ...")
            file = await client.download_media(message.reply_to_message)
        else:
            if len(message.command) < 2:
                return await aux.edit("**🥀 ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ\nᴘʟᴀʏ ᴍᴜsɪᴄ ᴏʀ ᴠɪᴅᴇᴏ❗...**")
            query = message.text.split(None, 1)[1].split("?si=")[0] if "?si=" in message.text else message.text.split(None, 1)[1]
            results = await get_result(query)
            link = results[0]
            file = await get_stream(link, type)

        try:
            a = await call.get_call(chat_id)
            if a.status == "not_playing":
                stream = await run_stream(file, type)
                await call.change_stream(chat_id, stream)
                await aux.edit("Playing!")
            elif a.status in ["playing", "paused"]:
                position = await queues.put(chat_id, file=file, type=type)
                await aux.edit(f"Queued At {position}")
        except Exception as e:
            if "not joined" in str(e).lower():
                stream = await run_stream(file, type)
                await call.join_group_call(chat_id, stream)
                await aux.edit("Playing!")
            else:
                print(f"Error: {e}")
                return await aux.edit("**Please Try Again !**")
    except Exception as e:
        print(f"Error: {e}")
        return await aux.edit("**Please Try Again !**")

# Video Player (Play From Anywhere)
@app.on_message(cdz(["cvply", "cvplay"]))
@sudo_users_only
async def video_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message, "**🥀 Please Set A Chat To Start Stream❗**")

    aux = await eor(message, "**Processing ...**")
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    type = "Video"
    try:
        if video:
            await aux.edit("Downloading ...")
            file = await client.download_media(message.reply_to_message)
        else:
            if len(message.command) < 2:
                return await aux.edit("**🥀 ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ\nᴘʟᴀʏ ᴍᴜsɪᴄ ᴏʀ ᴠɪᴅᴇᴏ❗...**")
            query = message.text.split(None, 1)[1].split("?si=")[0] if "?si=" in message.text else message.text.split(None, 1)[1]
            results = await get_result(query)
            link = results[0]
            file = await get_stream(link, type)

        try:
            a = await call.get_call(chat_id)
            if a.status == "not_playing":
                stream = await run_stream(file, type)
                await call.change_stream(chat_id, stream)
                await aux.edit("Playing!")
            elif a.status in ["playing", "paused"]:
                position = await queues.put(chat_id, file=file, type=type)
                await aux.edit(f"Queued At {position}")
        except Exception as e:
            if "not joined" in str(e).lower():
                stream = await run_stream(file, type)
                await call.join_group_call(chat_id, stream)
                await aux.edit("Playing!")
            else:
                print(f"Error: {e}")
                return await aux.edit("**Please Try Again !**")
    except Exception as e:
        print(f"Error: {e}")
        return await aux.edit("**Please Try Again !**")
