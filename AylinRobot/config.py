# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "23860620"))
   API_HASH = os.getenv("API_HASH", "347c94d92d0bbcfbc223651b73d71345")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7118958431:AAGKzEFm9WHnEFh2ZLlVGYrXyER_PKjGYLY")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "LaylaaRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "L A Y L A  💁‍♀")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6413040743"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Tanimiramkimem") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "True"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002050222287"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "laylalist1")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002115106214"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002001432627"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "b66e353e-9aa9-4e67-8170-465165aac5f2")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Teamabasof")
   CHANNEL = os.environ.get("CHANNEL", "teamabasov")
   SUPPORT = os.environ.get("SUPPORT", "teamabasov")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/6eaba9b91d762137a22f7.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2bdf3b6e7ebbd91d3706e.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
