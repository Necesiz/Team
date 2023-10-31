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

isleyen = []


@rehim.on(events.NewMessage(pattern="^/chatbot ?(.*)"))
async def chatbot(event):
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **ChatBot bu qrupda aktiv olundu !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **ChatBot onsuzda aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **ChatBot bu qrupda deaktiv olundu !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **ChatBot onsuzda deaktivdir !**")
        return
    
    else:
        await event.reply("On və yaxud Off yazmadınız")


@rehim.on(events.NewMessage)
async def test(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    if "Salam" in mesaj or "Selam" in mesaj or "sa" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "Necəsən" in mesaj or "Necesen" in mesaj or "Necəsiz" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "Gedirəm" in mesaj or "Getdim" in mesaj or "Gedəcəm" in mesaj:
        await event.reply(f"{random.choice(getdim)}")
    if "Gəldim" in mesaj or "Geldim" in mesaj or "Gəldimm" in mesaj:
        await event.reply(f"{random.choice(geldim)}")
    if "ban" in mesaj or "mute" in mesaj or "warn" in mesaj:
        await event.reply(f"{random.choice(ban)}")
    if "Hardasınız" in mesaj or "Hardasan" in mesaj or "Hardeidin" in mesaj:
        await event.reply(f"{random.choice(hardasan)}")
    
    
