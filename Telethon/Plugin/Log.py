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



ADMIN = [5508658149, 1727079853]
LOG_QRUP = -1001954231110

@rehim.on(events.NewMessage(incoming=True, from_users=ADMIN, pattern="^[./!]kopya ?(.*)|^[./!]ogra ?(.*)"))
async def kopya(event):
    await event.delete()
    mesaj = await event.get_reply_message()
    if not mesaj:
        await event.reply("Bir şeyə yanıt verdə 🤦‍♂️")
        return
    await mesaj.reply("⚡️ **Bu mesajı log qrupuna atdım**")
    await event.client.send_message(LOG_QRUP, mesaj)

