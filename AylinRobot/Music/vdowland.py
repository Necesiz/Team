from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
import requests
import os

# Telegram API bilgilerinizi buraya girin


# TikTok video URL'inden videoyu indiren fonksiyon
def download_tiktok_video(url):
    response = requests.get(url)
    filename = "tiktok_video.mp4"
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

# Instagram video URL'inden videoyu indiren fonksiyon
def download_instagram_video(url):
    # Buraya Instagram video indirme kodunu ekleyin (örneğin, instaloader kullanabilirsiniz)
    pass

# TikTok ve Instagram video URL'lerini algılayan filtre
@app.on_message(filters.regex(r"(https?://(www\.)?tiktok\.com/.+)|(https?://(www\.)?instagram\.com/.+)"))
def save_videos(client, message: Message):
    chat_id = message.chat.id
    video_url = message.text

    if "tiktok.com" in video_url:
        filename = download_tiktok_video(video_url)
    elif "instagram.com" in video_url:
        filename = download_instagram_video(video_url)

    # İndirilen videoyu Telegram'a gönderme
    client.send_video(chat_id, video=filename)

    # İndirilen videoyu temizleme
    os.remove(filename)
