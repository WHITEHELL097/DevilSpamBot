from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from Devil.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
        ],
        [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/devilz_bots"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/devilz_support")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/WHITEHELL097/DevilSpamBot")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [😈](https://t.me/whitehell097)**\n\n"
        TEXT += f"» **ʙᴏᴛ ꜱᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `M3.2`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph//file/4dc15eb9557d661270a58.jpg",
                caption=TEXT, 
                buttons=PythonButton)
