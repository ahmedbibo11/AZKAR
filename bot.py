# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN") or "PUT_YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ==================================================
# DATA
# ==================================================

ADHKAR = {

    "morning": [
        {
            "text": "أَعُوذُ بِاللهِ مِنْ الشَّيْطَانِ الرَّجِيمِ\nاللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ...",
            "count": 1
        },
        {
            "text": "قُلْ هُوَ ٱللَّهُ أَحَدٌ",
            "count": 3
        },
    ],

    "evening": [
        {
            "text": "أَمْسَيْنَا وَأَمْسَى الْمُلْكُ لِلَّهِ...",
            "count": 1
        },
    ],

    "tasbeeh": [
        {"text": "سبحان الله", "count": 33},
        {"text": "الحمد لله", "count": 33},
        {"text": "الله أكبر", "count": 34},
    ],

    "istighfar": [
        {"text": "أستغفر الله العظيم وأتوب إليه", "count": 100},
    ],

    # ===== أذكار متنوعة =====
    "sleep": [
        {"text": "بِاسْمِكَ رَبِّي وَضَعْتُ جَنْبِي", "count": 1},
    ],

    "study": [
        {"text": "اللهم لا سهل إلا ما جعلته سهلاً", "count": 1},
    ],

    "forgotten": [
        {"text": "سبحان الله عدد ما خلق", "count": 3},
    ],

    "prayer": [
        {"text": "اللهم أعني على ذكرك وشكرك وحسن عبادتك", "count": 1},
    ],
}

# ==================================================
# USER STATE
# ==================================================

USER_STATE = {}
# user_id : { section, index, remaining }

# ==================================================
# KEYBOARDS
# ==================================================

def main_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🌅 أذكار الصباح", callback_data="morning"),
        InlineKeyboardButton("🌙 أذكار المساء", callback_data="evening"),
        InlineKeyboardButton("📿 تسبيح", callback_data="tasbeeh"),
        InlineKeyboardButton("🕊️ استغفار", callback_data="istighfar"),
        InlineKeyboardButton("✨ أذكار متنوعة", callback_data="misc"),
    )
    return kb


def misc_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🌙 أذكار النوم", callback_data="sleep"),
        InlineKeyboardButton("📚 أذكار المذاكرة", callback_data="study"),
        InlineKeyboardButton("🕯️ أذكار مهجورة", callback_data="forgotten"),
        InlineKeyboardButton("🕌 أذكار الصلاة", callback_data="prayer"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="back"),
    )
    return kb


def counter_kb(remaining):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(f"📿 {remaining} متبقي", callback_data="count")
    )
    return kb

# ==================================================
# CORE LOGIC
# ==================================================

def start_section(chat_id, uid, section):
    USER_STATE[uid] = {
        "section": section,
        "index": 0,
        "remaining": ADHKAR[section][0]["count"]
    }
    send_current_dhikr(chat_id, uid)


def send_current_dhikr(chat_id, uid):
    state = USER_STATE[uid]
    dhikr = ADHKAR[state["section"]][state["index"]]

    bot.send_message(
        chat_id,
        f"<code>﴿ {dhikr['text']} ﴾</code>",
        reply_markup=counter_kb(state["remaining"])
    )


def next_dhikr(chat_id, uid):
    state = USER_STATE[uid]
    state["index"] += 1

    if state["index"] >= len(ADHKAR[state["section"]]):
        bot.send_message(chat_id, "🤍 <b>تقبّل الله</b>")
        del USER_STATE[uid]
        return

    state["remaining"] = ADHKAR[state["section"]][state["index"]]["count"]
    send_current_dhikr(chat_id, uid)

# ==================================================
# HANDLERS
# ==================================================

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(
        m.chat.id,
        "🤍 مرحبًا بك\nاختر قسم الأذكار:",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda c: True)
def callbacks(c):
    uid = c.from_user.id
    chat_id = c.message.chat.id

    if c.data in ADHKAR:
        start_section(chat_id, uid, c.data)

    elif c.data == "misc":
        bot.send_message(chat_id, "✨ اختر نوع الأذكار:", reply_markup=misc_menu())

    elif c.data == "back":
        bot.send_message(chat_id, "اختر قسم الأذكار:", reply_markup=main_menu())

    elif c.data == "count":
        if uid not in USER_STATE:
            return

        USER_STATE[uid]["remaining"] -= 1

        if USER_STATE[uid]["remaining"] > 0:
            bot.edit_message_reply_markup(
                chat_id,
                c.message.message_id,
                reply_markup=counter_kb(USER_STATE[uid]["remaining"])
            )
        else:
            bot.edit_message_text("✔️ تم", chat_id, c.message.message_id)
            next_dhikr(chat_id, uid)

    bot.answer_callback_query(c.id)

# ==================================================
# RUN
# ==================================================

print("🤍 Dhikr Bot Running...")
bot.infinity_polling(skip_pending=True)
