# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "8953338"))
   API_HASH = os.getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6543631318:AAEmou9VAMkrszY_ep3KCQF2UUc3tv9ckxY")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "MeryemRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "M Ə R Y Ə M 💁‍♀")   
   OWNER_ID = int(os.environ.get("OWNER_ID","5508658149"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Erebliqaqas") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001954231110"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "MeryemPlayList")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001867892155"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001938386236"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05c7f123-51de-49ce-abd4-a016f8529a13")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Teamabasof")
   CHANNEL = os.environ.get("CHANNEL", "teamabasov")
   SUPPORT = os.environ.get("SUPPORT", "teamabasov")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b2c2ed59a89933a384ae3.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())