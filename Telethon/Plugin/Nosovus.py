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

SOYUS_CAVAB = ["🤖 Mən Mesajı Sildim\n⛔ SƏBƏB:- Söyüş Tipli Sözlər isdifadə Elıdiyin Üçün","🚫 Söyüş Tipli Mətn Olduğu Üçün Yazılan Mesajı Sildim"]


@rehim.on(events.NewMessage(pattern=f'(?i)s[iı]k+'))
@rehim.on(events.NewMessage(pattern=f'(?i)pox+'))
@rehim.on(events.NewMessage(pattern=f'(?i)s[iı]kd[iı]+'))
@rehim.on(events.NewMessage(pattern=f'(?i)da[sş]ax+'))
@rehim.on(events.NewMessage(pattern=f'(?i)s[iı]k[iı]m+'))
@rehim.on(events.NewMessage(pattern=f'(?i)p[eə]ys[eə]r+'))
@rehim.on(events.NewMessage(pattern=f'(?i)g[iı]jdlaa[ghx]+'))
@rehim.on(events.NewMessage(pattern=f'(?i)s[iı]k[iı]lm[iı][şs]+'))
@rehim.on(events.NewMessage(pattern=f'(?i)c[ıi]nd[ıi]r+'))
@rehim.on(events.NewMessage(pattern=f'(?i)q[əe]hb[əe]+'))
@rehim.on(events.NewMessage(pattern=f'(?i)dalbayov+'))
@rehim.on(events.NewMessage(pattern=f'(?i)c[ıi]r+'))
@rehim.on(events.NewMessage(pattern=f'(?i)c[iı]nd[iı]r+'))
@rehim.on(events.NewMessage(pattern=f'(?i)m[əe]k[iı]+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.delete()
    await event.reply(f"{random.choice(SOYUS_CAVAB)}")

