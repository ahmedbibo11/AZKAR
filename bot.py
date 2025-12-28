# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ================= USER STATE =================
USER_COUNTER = {}

# ================= ADHKAR DATA =================
ADHKAR = {
    "morning": [
        {"text": "رضيت بالله ربًا وبالإسلام دينًا وبمحمد ﷺ نبيًا", "count": 3},
        {"text": "اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت", "count": 1},
        {"text": "أصبحنا وأصبح الملك لله والحمد لله", "count": 1}
    ],
    "evening": [
        {"text": "اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت", "count": 1},
        {"text": "أمسينا وأمسى الملك لله والحمد لله", "count": 1}
    ],
    "tasbeeh": [
        {"text": "سبحان الله", "count": 33},
        {"text": "الحمد لله", "count": 33},
        {"text": "الله أكبر", "count": 34}
    ],
    "forgiveness": [
        {"text": "أستغفر الله العظيم وأتوب إليه", "count": 10},
        {"text": "رب اغفر لي وتب علي إنك أنت التواب الرحيم", "count": 5}
    ],
    "general": [
        {"text": "لا إله إلا الله وحده لا شريك له", "count": 5},
        {"text": "حسبي الله لا إله إلا هو عليه توكلت", "count": 3},
        {"text": "ألا بذكر الله تطمئن القلوب", "count": 1}
    ]
}

# ================= CATEGORY LABELS =================
CATEGORIES = {
    "morning": "🌅 أذكار الصباح",
    "evening": "🌙 أذكار المساء",
    "tasbeeh": "📿 تسبيح",
    "forgiveness": "🤍 استغفار",
    "general": "✨ أذكار متنوعة"
}

# ================= KEYBOARDS =================
def categories_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    for k, v in CATEGORIES.items():
        kb.add(InlineKeyboardButton(v, callback_data=f"cat|{k}"))
    return kb

def counter_kb(uid):
    remaining = USER_COUNTER[uid]["remaining"]
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(f"📿 {remaining} متبقي", callback_data="count")
    )
    return kb

def done_kb(category):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔁 ذكر آخر", callback_data=f"again|{category}")
    )
    kb.add(
        InlineKeyboardButton("⬅️ رجوع للأقسام", callback_data="back")
    )
    return kb

# ================= SEND DHIKR =================
def send_new_dhikr(chat_id, uid, category):
    dhikr = random.choice(ADHKAR[category])

    USER_COUNTER[uid] = {
        "text": dhikr["text"],
        "remaining": dhikr["count"],
        "category": category
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
    bot.send_message(
        m.chat.id,
        "🤍 مرحبًا بك في بوت الأذكار\nاختر القسم:",
        reply_markup=categories_kb()
    )

@bot.callback_query_handler(func=lambda c: True)
def handle(c):
    uid = c.from_user.id
    chat_id = c.message.chat.id
    data = c.data.split("|")

    if data[0] == "cat":
        send_new_dhikr(chat_id, uid, data[1])
        bot.answer_callback_query(c.id)

    elif c.data == "count":
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
            category = USER_COUNTER[uid]["category"]
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=c.message.message_id,
                text="<b>تقبّل الله 🤍</b>\n\n🌸 بارك الله في ذكرك",
                reply_markup=done_kb(category)
            )
            bot.answer_callback_query(c.id)

    elif data[0] == "again":
        send_new_dhikr(chat_id, uid, data[1])
        bot.answer_callback_query(c.id)

    elif c.data == "back":
        bot.send_message(
            chat_id,
            "📂 اختر القسم:",
            reply_markup=categories_kb()
        )
        bot.answer_callback_query(c.id)

# ================= RUN =================
print("🤍 Dhikr Counter Bot running...")
bot.infinity_polling(skip_pending=True)
