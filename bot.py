# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os
import re

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ================= USER MEMORY =================
USER_HISTORY = {}

def seen_before(uid, key):
    USER_HISTORY.setdefault(uid, [])
    return key in USER_HISTORY[uid]

def remember(uid, key):
    USER_HISTORY.setdefault(uid, []).append(key)
    if len(USER_HISTORY[uid]) > 150:
        USER_HISTORY[uid] = USER_HISTORY[uid][-150:]

# ================= ADHKAR CATEGORIES =================
CATEGORIES = {
    "morning": "🌅 أذكار الصباح",
    "evening": "🌙 أذكار المساء",
    "tasbeeh": "📿 تسبيح",
    "forgiveness": "🤍 استغفار",
    "calm": "🕊️ طمأنينة"
}

# ================= ADHKAR DATA =================
ADHKAR = {
    "morning": [
        "أصبحنا وأصبح الملك لله، والحمد لله",
        "اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت",
        "رضيت بالله ربًا وبالإسلام دينًا وبمحمد ﷺ نبيًا"
    ],
    "evening": [
        "أمسينا وأمسى الملك لله، والحمد لله",
        "اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت",
        "حسبي الله لا إله إلا هو عليه توكلت"
    ],
    "tasbeeh": [
        "سبحان الله وبحمده",
        "سبحان الله العظيم",
        "سبحان الله والحمد لله ولا إله إلا الله والله أكبر"
    ],
    "forgiveness": [
        "أستغفر الله العظيم وأتوب إليه",
        "اللهم اغفر لي ذنبي كله دقه وجله",
        "رب اغفر لي وتب علي إنك أنت التواب الرحيم"
    ],
    "calm": [
        "ألا بذكر الله تطمئن القلوب",
        "اللهم إني أعوذ بك من الهم والحزن",
        "لا إله إلا أنت سبحانك إني كنت من الظالمين"
    ]
}

# ================= MOODS / INTENTIONS =================
MOODS = {
    "🤲 خاشع": [
        "بخشوع القلب",
        "بيقين صادق",
        "بتسليم كامل"
    ],
    "🌿 هادئ": [
        "بسكون النفس",
        "بطمأنينة",
        "براحة القلب"
    ],
    "🔥 مكثف": [
        "بإلحاح",
        "بتركيز",
        "بقلب حاضر"
    ]
}

# ================= GENERATOR =================
def generate_dhikr(uid, category, mood):
    for _ in range(40):
        dhikr = random.choice(ADHKAR[category])
        intention = random.choice(MOODS[mood])

        key = f"{dhikr}|{intention}"
        if seen_before(uid, key):
            continue

        remember(uid, key)

        text = (
            f"﴿ {dhikr} ﴾\n\n"
            f"<i>{intention}</i> 🌸"
        )
        return f"<code>{text}</code>"

    return "<code>لا يوجد ذكر جديد حالياً 🤍</code>"

# ================= KEYBOARDS =================
def categories_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    for k, v in CATEGORIES.items():
        kb.add(InlineKeyboardButton(v, callback_data=f"cat|{k}"))
    return kb

def mood_kb(category):
    kb = InlineKeyboardMarkup(row_width=1)
    for m in MOODS.keys():
        kb.add(InlineKeyboardButton(m, callback_data=f"mood|{category}|{m}"))
    return kb

def again_kb(category, mood, copied=False):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🔄 ذكر آخر", callback_data=f"again|{category}|{mood}")
    )
    if not copied:
        kb.add(
            InlineKeyboardButton("📋 نسخ", callback_data=f"copy|{category}|{mood}")
        )
    else:
        kb.add(
            InlineKeyboardButton("✅ تم النسخ", callback_data="noop")
        )
    return kb

# ================= HANDLERS =================
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(
        m.chat.id,
        "🤍 مرحبًا بك في بوت الأذكار\nاختر النوع:",
        reply_markup=categories_kb()
    )

@bot.callback_query_handler(func=lambda c: True)
def handle(c):
    data = c.data.split("|")
    uid = c.from_user.id

    if data[0] == "cat":
        bot.send_message(
            c.message.chat.id,
            "🌸 اختر الحالة:",
            reply_markup=mood_kb(data[1])
        )

    elif data[0] == "mood":
        _, cat, mood = data
        text = generate_dhikr(uid, cat, mood)
        bot.send_message(
            c.message.chat.id,
            text,
            reply_markup=again_kb(cat, mood)
        )

    elif data[0] == "again":
        _, cat, mood = data
        text = generate_dhikr(uid, cat, mood)
        bot.send_message(
            c.message.chat.id,
            text,
            reply_markup=again_kb(cat, mood)
        )

    elif data[0] == "copy":
        bot.edit_message_reply_markup(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            reply_markup=again_kb(data[1], data[2], copied=True)
        )
        bot.answer_callback_query(c.id, "تم النسخ 🤍")

    else:
        bot.answer_callback_query(c.id)

# ================= RUN =================
print("🤍 Dhikr Bot is running...")
bot.infinity_polling(skip_pending=True)
