from sys import version_info
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from time import time
from datetime import datetime
from AylinRobot import AylinRobot as app


@app.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**💁‍♀️ @MeryemRoBot Sizinlədi\n\nƏtraflı məlumat üçün mənə şəxsidə yaz**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🫠 Mənə yaz", url=f"https://t.me/MeryemRobot?start=start")]])
    )



@app.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**Salam hazirda aktif olaraq çalışıram kömək üçün aşağıda buttonu isdifadə edin!**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Kömək", url=f"https://t.me/OldMultiBot?start")]])
    )

