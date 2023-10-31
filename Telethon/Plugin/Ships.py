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




faiz = ['10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','31%','32%','33%','34%','35%','36%','37%','38%','39%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','100%']
urek = ['❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️‍🔥','❤️‍🩹','❣️','💕','💞','💓','💗','💖','💘','💝']
cvb = ['Hə','Yox','Yaxında toydu','Nişanlanacaqlar','Evlənib boşanacaqlar']

@rehim.on(events.NewMessage(pattern="^/eros ?(.*)|^/ship ?(.*)"))
async def eros(event):
     if event.is_private:
          return await event.respond("Bu əmr qruplar üçün etibarlıdır!  ")
     qrup = await event.get_chat() 
     istifadeciler = await client.get_participants(qrup)
     sev1, sev2 = random.sample(istifadeciler, 2)
     secirem = await event.reply(f"{random.choice(urek)} Erosun oxu atıldı 🏹 \n🙈 Cütlükləri seçirəm")
     await asyncio.sleep(2)
     await secirem.delete()
     await event.reply(f"{random.choice(urek)} Cütlüklər:\n\n"
                       f" [{sev1.first_name}](tg://user?id={sev1.id})" + f" [{sev2.first_name}](tg://user?id={sev2.id})\n\n"
                       f"♥️ Sevgi Faizi: {random.choice(faiz)}\n\n"
                       f"💑 Evlənəcəklər: {random.choice(cvb)}")  
    

# aykhan026 | aykhan_s
# 0-dan yığılıb sənöl
# öz adına çıxaran papa de

