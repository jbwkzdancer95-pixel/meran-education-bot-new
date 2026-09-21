import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"


# =========================
# Telegram yordamchi funksiyalar
# =========================

def send_message(chat_id, text, reply_markup=None):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    if reply_markup:
        data["reply_markup"] = reply_markup

    requests.post(
        f"{TELEGRAM_API}/sendMessage",
        json=data
    )


def answer_callback(callback_query_id):
    requests.post(
        f"{TELEGRAM_API}/answerCallbackQuery",
        json={"callback_query_id": callback_query_id}
    )


# =========================
# Tugmalar
# =========================

def main_menu():
    return {
        "inline_keyboard": [
            [{"text": "📚 O‘quv materiallari", "callback_data": "materials"}],
            [{"text": "👶 Bolajonlar uchun", "callback_data": "kids"}],
            [{"text": "🎁 Promo kodlar", "callback_data": "promo"}],
            [{"text": "ℹ️ Biz haqimizda", "callback_data": "about"}]
        ]
    }


def materials_menu():
    return {
        "inline_keyboard": [
            [{"text": "📖 Adabiyot", "callback_data": "literature"}],
            [{"text": "🔙 Ortga", "callback_data": "main"}]
        ]
    }


def literature_menu():
    return {
        "inline_keyboard": [
            [{"text": "📚 Asarlar", "callback_data": "works"}],
            [{"text": "📝 Mavzulashtirilgan testlar", "callback_data": "tests"}],
            [{"text": "🔙 Ortga", "callback_data": "materials"}]
        ]
    }


def tests_menu():
    return {
        "inline_keyboard": [
            [{
                "text": "📸 Chekni yuborish",
                "url": "https://t.me/MERAN_EDU"
            }],
            [{"text": "🔙 Ortga", "callback_data": "literature"}]
        ]
    }


def promo_menu():
    return {
        "inline_keyboard": [
            [{"text": "🎓 Ibrat Academy", "callback_data": "ibrat"}],
            [{"text": "📚 Mutolaa", "callback_data": "mutolaa"}],
            [{"text": "♟️ UZchess", "callback_data": "uzchess"}],
            [{"text": "🤖 Ustoz AI", "callback_data": "ustoz"}],
            [{"text": "🔙 Ortga", "callback_data": "main"}]
        ]
    }


def promo_product_menu():
    return {
        "inline_keyboard": [
            [{
                "text": "📸 Chekni yuborish",
                "url": "https://t.me/MERAN_EDU"
            }],
            [{"text": "🔙 Ortga", "callback_data": "promo"}]
        ]
    }


def about_menu():
    return {
        "inline_keyboard": [
            [{"text": "🔙 Ortga", "callback_data": "main"}]
        ]
    }


# =========================
# Matnlar
# =========================

START_TEXT = """🎓 **MERAN EDUCATION BOT📚**

Assalomu alaykum! 👋
MERAN EDUCATION bilim maskaniga xush kelibsiz!

Kerakli bo‘limni tanlang:
"""


MATERIALS_TEXT = """📚 **O‘QUV MATERIALLARI**

Kerakli bo‘limni tanlang:
"""


LITERATURE_TEXT = """📖 **ADABIYOT**

Kerakli bo‘limni tanlang:
"""


TESTS_TEXT = """💳 **TO‘LOV QILISH**

🔐 Ushbu xizmatdan foydalanish **obuna asosida** amalga oshiriladi.

🔹 1 oylik obuna — **30 000 so‘m**

🔹 2 oylik obuna — **50 000 so‘m**

💳 **Karta raqami:**

`9860 1601 3522 3172`

*Nargiza Samandarova*

📞 Qo‘shimcha ma’lumot olish uchun:

**@Meran_education**
"""


PROMO_TEXT = """📱 O‘zingizga kerakli ilovani tanlang va obuna promo-kodini xarid qiling:
"""


IBRAT_TEXT = """🎓 **IBRAT ACADEMY**

📱 Ibrat Academy uchun **obuna promo-kodi**.

💳 **Promo-kod narxi:**
🔹 **79 000 so‘m**

📅 **Obuna muddati:**
🔹 **3 oy**

💳 **Karta raqami:**

`9860 1601 3522 3172`

*Nargiza Samandarova*

📌 To‘lovni amalga oshirgandan so‘ng, **chekni yuboring.**

📞 Qo‘shimcha ma’lumot uchun:
**@Meran_education**
"""


MUTOLAA_TEXT = """📚 **MUTOLAA**

📱 Mutolaa uchun **obuna promo-kodi**.

💳 **Promo-kod narxi:**
🔹 **49 000 so‘m**

📅 **Obuna muddati:**
🔹 **3 oy**

💳 **Karta raqami:**

`9860 1601 3522 3172`

*Nargiza Samandarova*

📌 To‘lovni amalga oshirgandan so‘ng, **chekni yuboring.**

📞 Qo‘shimcha ma’lumot uchun:
**@Meran_education**
"""


UZCHESS_TEXT = """♟️ **UZCHESS**

📱 UZchess uchun **obuna promo-kodi**.

💳 **Promo-kod narxi:**
🔹 **39 000 so‘m**

📅 **Obuna muddati:**
🔹 **3 oy**

💳 **Karta raqami:**

`9860 1601 3522 3172`

*Nargiza Samandarova*

📌 To‘lovni amalga oshirgandan so‘ng, **chekni yuboring.**

📞 Qo‘shimcha ma’lumot uchun:
**@Meran_education**
"""


USTOZ_TEXT = """🤖 **USTOZ AI**

📱 Ustoz AI uchun **obuna promo-kodi**.

💳 **Promo-kod narxi:**
🔹 **129 000 so‘m**

📅 **Obuna muddati:**
🔹 **1 yil**

💳 **Karta raqami:**

`9860 1601 3522 3172`

*Nargiza Samandarova*

📌 To‘lovni amalga oshirgandan so‘ng, **chekni yuboring.**

📞 Qo‘shimcha ma’lumot uchun:
**@Meran_education**
"""


ABOUT_TEXT = """ℹ️ **BIZ HAQIMIZDA**

🎓 **MERAN EDUCATION** — bilim olish, rivojlanish va zamonaviy ta’lim imkoniyatlarini bir joyda jamlagan ta’lim platformasi.

📚 Bizning asosiy yo‘nalishlarimiz:
— 📖 Adabiy asarlar va o‘quv materiallari
— 📝 Mavzulashtirilgan testlar
— 🎁 Foydali ta’limiy platformalar uchun promo-kodlar

🚀 **MERAN EDUCATION — bilim sari birgalikda!**

📞 Murojaat uchun:
**@Meran_education**
"""


# =========================
# Asarlar
# =========================

WORKS_TEXT = """📚 **ASARLAR**

Hozircha asarlar ro‘yxati qo‘shilmagan.

Tez orada 36 ta asar Telegram kanalidagi PDF fayllarga havola bilan joylashtiriladi.
"""


# =========================
# Bolajonlar
# =========================

KIDS_TEXT = """👶 **BOLAJONLAR UCHUN**

Ushbu bo‘lim tez orada ishga tushadi. 🚀
"""


# =========================
# Callback boshqaruvi
# =========================

def handle_callback(chat_id, callback_query_id, data):

    answer_callback(callback_query_id)

    if data == "main":
        send_message(
            chat_id,
            START_TEXT,
            main_menu()
        )

    elif data == "materials":
        send_message(
            chat_id,
            MATERIALS_TEXT,
            materials_menu()
        )

    elif data == "literature":
        send_message(
            chat_id,
            LITERATURE_TEXT,
            literature_menu()
        )

    elif data == "tests":
        send_message(
            chat_id,
            TESTS_TEXT,
            tests_menu()
        )

    elif data == "promo":
        send_message(
            chat_id,
            PROMO_TEXT,
            promo_menu()
        )

    elif data == "ibrat":
        send_message(
            chat_id,
            IBRAT_TEXT,
            promo_product_menu()
        )

    elif data == "mutolaa":
        send_message(
            chat_id,
            MUTOLAA_TEXT,
            promo_product_menu()
        )

    elif data == "uzchess":
        send_message(
            chat_id,
            UZCHESS_TEXT,
            promo_product_menu()
        )

    elif data == "ustoz":
        send_message(
            chat_id,
            USTOZ_TEXT,
            promo_product_menu()
        )

    elif data == "about":
        send_message(
            chat_id,
            ABOUT_TEXT,
            about_menu()
        )

    elif data == "works":
        send_message(
            chat_id,
            WORKS_TEXT,
            {
                "inline_keyboard": [
                    [{"text": "🔙 Ortga", "callback_data": "literature"}]
                ]
            }
        )

    elif data == "kids":
        send_message(
            chat_id,
            KIDS_TEXT,
            {
                "inline_keyboard": [
                    [{"text": "🔙 Ortga", "callback_data": "main"}]
                ]
            }
        )


# =========================
# Webhook
# =========================

@app.route("/", methods=["GET"])
def home():
    return "MERAN EDUCATION BOT ishlayapti! ✅", 200


@app.route("/webhook", methods=["POST"])
def webhook():

    update = request.get_json()

    if not update:
        return "OK", 200

    # Oddiy xabar
    if "message" in update:

        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":

            send_message(
                chat_id,
                START_TEXT,
                main_menu()
            )

    # Inline tugma bosilganda
    elif "callback_query" in update:

        callback = update["callback_query"]

        callback_query_id = callback["id"]
        chat_id = callback["message"]["chat"]["id"]
        data = callback.get("data", "")

        handle_callback(
            chat_id,
            callback_query_id,
            data
        )

    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(
        host="0.0.0.0",
        port=port
    )
