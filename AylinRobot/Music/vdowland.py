from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
import requests
import os






# TikTok video indirme işlevi
def download_tiktok_video(url):
    # TikTok video bağlantısını kullanarak videoyu indir
    response = requests.get(url)
    if response.status_code == 200:
        video_url = response.json()["itemInfo"]["itemStruct"]["video"]["downloadAddr"]
        video_data = requests.get(video_url).content
        return video_data
    else:
        return None


# Instagram video indirme işlevi
def download_instagram_video(url):
    # Instagram video bağlantısını kullanarak videoyu indir
    response = requests.get(url)
    if response.status_code == 200:
        video_url = response.text.split('"')[4]
        video_data = requests.get(video_url).content
        return video_data
    else:
        return None





# Video bağlantısını işleme
@app.on_message(filters.text & filters.private)
def handle_video_link(_, message: Message):
    text = message.text.strip()

    # TikTok veya Instagram video bağlantısı olup olmadığını kontrol edin
    if "tiktok.com" in text:
        video_data = download_tiktok_video(text)
        if video_data:
            message.reply_video(video_data)
        else:
            message.reply_text("Üzgünüm, TikTok video indirilemedi.")
    elif "instagram.com" in text:
        video_data = download_instagram_video(text)
        if video_data:
            message.reply_video(video_data)
        else:
            message.reply_text("Üzgünüm, Instagram video indirilemedi.")
    else:
        message.reply_text("Geçersiz video bağlantısı. Lütfen TikTok veya Instagram video bağlantısı paylaşın.")


