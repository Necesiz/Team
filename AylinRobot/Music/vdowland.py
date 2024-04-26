from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
import requests
import os






# Web sitesinden skorları alacak URL
score_url = "https://example.com/live_scores"

# Pyrogram istemcisini oluşturun


# Skorları almak için bir fonksiyon
def get_live_scores():
    response = requests.get(score_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Günün ve önemli maçları gönderme işlevi
def send_today_scores():
    scores = get_live_scores()
    if scores:
        # Burada dönen JSON verisini analiz ederek istediğiniz şekilde düzenleyebilirsiniz
        # Örneğin, belirli bir formatta maç bilgileri alıp kullanıcılara gönderebilirsiniz
        today_scores = "Günün ve önemli maçlar:\n"
        for match in scores:
            today_scores += f"{match['home_team']} {match['home_score']} - {match['away_score']} {match['away_team']}\n"
        
        # Sonucu döndür
        return today_scores
    else:
        return "Skor bilgileri alınamadı."


# /start komutunu işleme

# /scores komutunu işleme
@app.on_message(filters.command("scores"))
def scores_command(_, message):
    today_scores = send_today_scores()
    message.reply_text(today_scores)


# Botu çalıştırma
if __name__ == "__main__":
    app.run()
