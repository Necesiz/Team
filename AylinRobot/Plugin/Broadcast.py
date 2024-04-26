from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pymongo import MongoClient

# Telegram API anahtarları ve MongoDB bağlantı URL'si

mongo_uri = "mongodb+srv://Userbot1234:Userbot1234@cluster0.t3gnphl.mongodb.net/?retryWrites=true&w=majority"
owner_id = "6413040743"  # Bot sahibinin Telegram kullanıcı kimliği

# MongoDB'ye bağlanma
mongo_client = MongoClient(mongo_uri)
db = mongo_client["telegram_broadcast_bot"]
users_collection = db["users"]
groups_collection = db["groups"]

# Pyrogram istemcisini oluşturma


# /start komutunu işleme


# /broadcast komutunu işleme
@app.on_message(filters.command("broadcast") & filters.private)
def broadcast_command(_, message):
    # Sadece bot sahibi /broadcast komutunu kullanabilir
    if str(message.from_user.id) == owner_id:
        message.reply_text("Yayın başlatılıyor! Lütfen göndermek istediğiniz mesajı yazın.")
        app.set("broadcast_mode", True)
    else:
        message.reply_text("Bu komutu kullanma izniniz yok.")


# Broadcast mesajını işleme
@app.on_message(filters.command("bcast") & filters.private)
def handle_broadcast(_, message):
    if app.set("broadcast_mode", False):
        users = users_collection.find()
        for user in users:
            try:
                app.send_message(user["_id"], message.text)
            except Exception as e:
                print(f"Hata: {e}")
        message.reply_text("Yayın tamamlandı.!")
        app.set("broadcast_mode", False)


# /stats komutunu işleme
@app.on_message(filters.command("stats") & filters.private)
def stats_command(_, message):
    # Sadece bot sahibi /stats komutunu kullanabilir
    if str(message.from_user.id) == owner_id:
        total_users = users_collection.count_documents({})
        total_groups = groups_collection.count_documents({})
        message.reply_text(f"Botu kullanan kullanıcı sayısı: {total_users}\nToplam grup sayısı: {total_groups}")
    else:
        message.reply_text("Bu komutu kullanma izniniz yok.")


# Grup sohbetine katılma
@app.on_message(filters.new_chat_members & filters.group)
def join_group(_, message):
    # Sadece grup bilgilerini kaydetmek için
    groups_collection.update_one(
        {"_id": message.chat.id},
        {"$set": {"title": message.chat.title}},
        upsert=True,
    )


# Botu ça