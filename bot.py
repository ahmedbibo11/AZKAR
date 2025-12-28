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
        "text": "أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله ، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير ، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه ، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُبِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر ، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر.",
        "count": 1
    },

    {
        "text": "اللّهـمَّ أَنْتَ رَبِّـي لا إلهَ إلاّ أَنْتَ ، خَلَقْتَنـي وَأَنا عَبْـدُك ، وَأَنا عَلـى عَهْـدِكَ وَوَعْـدِكَ ما اسْتَـطَعْـت ، أَعـوذُبِكَ مِنْ شَـرِّ ما صَنَـعْت ، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ.",
        "count": 1
    },

    {
        "text": "رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً.",
        "count": 3
    },

    {
        "text": "اللّهُـمَّ إِنِّـي أَصْبَـحْتُ أُشْـهِدُك ، وَأُشْـهِدُ حَمَلَـةَ عَـرْشِـك ، وَمَلَائِكَتَكَ ، وَجَمـيعَ خَلْـقِك ، أَنَّـكَ أَنْـتَ اللهُ لا إلهَ إلاّ أَنْـتَ وَحْـدَكَ لا شَريكَ لَـك ، وَأَنَّ ُ مُحَمّـداً عَبْـدُكَ وَرَسـولُـك.",
        "count": 4
    },

    {
        "text": "اللّهُـمَّ ما أَصْبَـَحَ بي مِـنْ نِعْـمَةٍ أَو بِأَحَـدٍ مِـنْ خَلْـقِك ، فَمِـنْكَ وَحْـدَكَ لا شريكَ لَـك ، فَلَـكَ الْحَمْـدُ وَلَـكَ الشُّكْـر.",
        "count": 1
    },

    {
        "text": "حَسْبِـيَ اللّهُ لا إلهَ إلاّ هُوَ عَلَـيهِ تَوَكَّـلتُ وَهُوَ رَبُّ العَرْشِ العَظـيم.",
        "count": 7
    },

    {
        "text": "بِسـمِ اللهِ الذي لا يَضُـرُّ مَعَ اسمِـهِ شَيءٌ في الأرْضِ وَلا في السّمـاءِ وَهـوَ السّمـيعُ العَلـيم.",
        "count": 3
    },

    {
        "text": "اللّهُـمَّ بِكَ أَصْـبَحْنا وَبِكَ أَمْسَـينا ، وَبِكَ نَحْـيا وَبِكَ نَمُـوتُ وَإِلَـيْكَ النُّـشُور.",
        "count": 1
    }

]

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
