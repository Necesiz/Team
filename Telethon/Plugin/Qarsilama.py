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



sahip_murti = [5508658149] 
yardimci = [333321239] 

@rehim.on(events.ChatAction)
async def katildi(event):
    if event.user_joined:
        gon = await event.get_user()
        etiket = f"[{gon.first_name}](tg://user?id={gon.id})"
    if gon.id in sahip_murti:
        await event.reply(f"● Bu gələn mənim sahibimdir, xoş gəldin sahibim {etiket}")
    elif gon.id in yardimci:
        await event.reply(f"● Bu gələn mənim Sudomdur\nXoş gəldin  {etiket}") 
    else:
        await event.reply(f"● {etiket} {random.choice(userjoin)}")



@rehim.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply(random.choice(xosgetdin))

userjoin = (

    "Xoş Gəldoin",
    "Xoş Gəldin Gözəl İnsan", 
    "Sənin Gəlişin Məni Sevindirdi", 
    "Aramıza Xoş Gəldin",
    "Partimizə Xoş Gəldin",
    "Bayaqdan Səni Gözləyirəm",
    "Xoşgəldin, Pizza gətirəcəyivi düşnürdük.",
    "Xoşgəldin, Çıxacagsansa indidən çıx 😒.",
)


xosgetdin = (

    "Əla birdə gəlmə",
    "Şükür Allaha getdi😉", 
    "Niyə çıxdız 🙄", 
    "xoş getdin 😐",
    "Sağolun birdə gəlmək ümidi ilə",
)



