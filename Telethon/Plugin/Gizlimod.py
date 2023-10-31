from Telethon.Plugin.Telethon import rehim
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events
import asyncio
import random
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import ChannelParticipantsBots
from os import remove
from telethon.tl.functions.users import GetFullUserRequest
from AylinRobot.config import Config
from telethon import Button, events
import speedtest
from asyncio import sleep
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
import random, base64
from telethon import events, errors
from telethon.tl.types import ChannelParticipantsAdmins
import time
from telethon import events
from telethon import events, errors
from telethon.tl.types import ChannelParticipantsAdmins
import time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsAdmins

SAHIB = [5508658149]

# Bu məlumatları silmək qadağandır...!
# Apache 2.0 License
# https://github.com/aykhan026/AykhanRoBot/LICENSE
# 
# Telegram: @RoBotlarimTg | @aykhan_s



isleyen = []

@rehim.on(events.NewMessage(incoming=True, from_users=SAHIB, pattern="^[./!]gizlimod ?(.*)"))
async def gizlimod(event):
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **Gizli Mod bu qrupda aktiv olundu !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **Gizli Mod onsuzda aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **Gizli Mod bu qrupda deaktiv olundu !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **Gizli Mod onsuzda deaktivdir !**")
        return
    else:
        await event.reply("On və yaxud Off yazmadınız")


@rehim.on(events.NewMessage(incoming=True))
async def gizli(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    yanitlanmis_mesaj = event.message.reply_to_msg_id
    if qrup not in isleyen:
        return
    if not yanitlanmis_mesaj:
       yanitlanmis_mesaj = None
       await rehim.send_message(event.chat_id, mesaj, reply_to=yanitlanmis_mesaj)
       await event.delete()
    else:
        await rehim.send_message(event.chat_id, mesaj, reply_to=yanitlanmis_mesaj)
        await event.delete()

