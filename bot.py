# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")  # أو حط التوكن مباشرة كنص
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ===================== DATA =====================

ADHKAR = {
    "morning": [
        {
            "text": "أَعُوذُ بِاللهِ مِنْ الشَّيْطَانِ الرَّجِيمِ\nاللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلاَ يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ وَلاَ يَؤُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ. [آية الكرسى - البقرة 255]",
            "count": 1
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ هُوَ ٱللَّهُ أَحَدٌ، ٱللَّهُ ٱلصَّمَدُ، لَمْ يَلِدْ وَلَمْ يُولَدْ، وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ، مِن شَرِّ مَا خَلَقَ، وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ، وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ، وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        {
            "text": "أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله ، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير ، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه ، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُبِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر ، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر",
            "count": 1
        }
        "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        {
            "text": "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم\nقُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
            "count": 3
        },
        
    ]
}

# ===================== USER STATE =====================

USER_STATE = {}
# {
#   user_id: {
#       "section": "morning",
#       "index": 0,
#       "remaining": 3
#   }
# }

# ===================== KEYBOARDS =====================

def main_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🌅 أذكار الصباح", callback_data="morning"),
        InlineKeyboardButton("🌙 أذكار المساء", callback_data="evening"),
        InlineKeybo
        ardButton("📿 تسبيح", callback_data="tasbeeh"),
        InlineKeyboardButton("🕊️ استغفار", callback_data="istighfar"),
        InlineKeyboardButton("✨ أذكار متنوعة", callback_data="misc"),
    )
    return kb


def counter_kb(remaining):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(f"📿 {remaining} متبقي", callback_data="count")
    )
    return kb

# ===================== FUNCTIONS =====================

def send_current_dhikr(chat_id, uid):
    state = USER_STATE[uid]
    dhikr = ADHKAR[state["section"]][state["index"]]

    bot.send_message(
        chat_id,
        f"<code>﴿ {dhikr['text']} ﴾</code>",
        reply_markup=counter_kb(state["remaining"])
    )


def start_section(chat_id, uid, section):
    USER_STATE[uid] = {
        "section": section,
        "index": 0,
        "remaining": ADHKAR[section][0]["count"]
    }
    send_current_dhikr(chat_id, uid)


def next_dhikr(chat_id, uid):
    state = USER_STATE[uid]
    state["index"] += 1

    if state["index"] >= len(ADHKAR[state["section"]]):
        bot.send_message(chat_id, "🤍 <b>تقبّل الله</b>\n\n🌸 انتهت أذكار الصباح")
        del USER_STATE[uid]
        return

    dhikr = ADHKAR[state["section"]][state["index"]]
    state["remaining"] = dhikr["count"]
    send_current_dhikr(chat_id, uid)

# ===================== HANDLERS =====================

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

    if c.data == "morning":
        start_section(chat_id, uid, "morning")
        bot.answer_callback_query(c.id)

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
            bot.edit_message_text(
                "✔️ تم",
                chat_id,
                c.message.message_id
            )
            next_dhikr(chat_id, uid)

        bot.answer_callback_query(c.id)

# ===================== RUN =====================

print("🤍 Dhikr Bot Running...")
bot.infinity_polling(skip_pending=True)
