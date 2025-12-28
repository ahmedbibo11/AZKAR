# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ================= USER STATE =================
USER_COUNTER = {}

# ================= ADHKAR =================
ADHKAR = [
    {
        "text": "رضيت بالله ربًا وبالإسلام دينًا وبمحمد ﷺ نبيًا",
        "count": 3
    },
    {
        "text": "سبحان الله وبحمده",
        "count": 10
    },
    {
        "text": "أستغفر الله العظيم وأتوب إليه",
        "count": 10
    },
    {
        "text": "لا إله إلا الله وحده لا شريك له",
        "count": 5
    }
]

# ================= KEYBOARDS =================
def counter_kb(uid):
    remaining = USER_COUNTER[uid]["remaining"]
    kb = InlineKeyboardMarkup(row_width=1)

    kb.add(
        InlineKeyboardButton(
            f"📿 {remaining} متبقي",
            callback_data="count"
        )
    )
    return kb


def done_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔁 ذكر آخر", callback_data="new")
    )
    return kb

# ================= SEND DHIKR =================
def send_new_dhikr(chat_id, uid):
    dhikr = random.choice(ADHKAR)

    USER_COUNTER[uid] = {
        "text": dhikr["text"],
        "remaining": dhikr["count"]
    }

    message = (
        f"﴿ {dhikr['text']} ﴾\n\n"
        f"✨ العدد: {dhikr['count']}"
    )

    bot.send_message(
        chat_id,
        f"<code>{message}</code>",
        reply_markup=counter_kb(uid)
    )

# ================= HANDLERS =================
@bot.message_handler(commands=["start"])
def start(m):
    send_new_dhikr(m.chat.id, m.from_user.id)

@bot.callback_query_handler(func=lambda c: True)
def handle(c):
    uid = c.from_user.id
    chat_id = c.message.chat.id

    if c.data == "count":
        if uid not in USER_COUNTER:
            return

        USER_COUNTER[uid]["remaining"] -= 1
        remaining = USER_COUNTER[uid]["remaining"]

        if remaining > 0:
            bot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=c.message.message_id,
                reply_markup=counter_kb(uid)
            )
            bot.answer_callback_query(c.id, "📿")

        else:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=c.message.message_id,
                text="<b>تقبّل الله 🤍</b>\n\n🌸 بارك الله في ذكرك",
                reply_markup=done_kb()
            )
            bot.answer_callback_query(c.id)

    elif c.data == "new":
        send_new_dhikr(chat_id, uid)
        bot.answer_callback_query(c.id)

# ================= RUN =================
print("🤍 Dhikr Counter Bot running...")
bot.infinity_polling(skip_pending=True)
