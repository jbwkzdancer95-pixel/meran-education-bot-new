import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Foydalanuvchi qaysi menyuda turganini saqlaydi
user_states = {}


def send_message(chat_id, text, keyboard=None):
    data = {
        "chat_id": chat_id,
        "text": text
    }

    if keyboard:
        data["reply_markup"] = keyboard

    requests.post(
        f"{TELEGRAM_API}/sendMessage",
        json=data
    )


# =========================
# REPLY KEYBOARDS
# =========================

def main_keyboard():
    return {
        "keyboard": [
            [{"text": "📚 O‘quv materiallari"}],
            [{"text": "👶 MERAN KIDS"}],
            [{"text": "🎁 Promo kodlar"}],
            [{"text": "ℹ️ Biz haqimizda"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def materials_keyboard():
    return {
        "keyboard": [
            [{"text": "📖 Adabiyot"}],
            [{"text": "🔙 Ortga"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def literature_keyboard():
    return {
        "keyboard": [
            [{"text": "📚 Asarlar"}],
            [{"text": "📝 Mavzulashtirilgan testlar"}],
            [{"text": "🔙 Ortga"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def promo_keyboard():
    return {
        "keyboard": [
            [{"text": "🎓 Ibrat Academy"}],
            [{"text": "📚 Mutolaa"}],
            [{"text": "♟️ UZchess"}],
            [{"text": "🤖 Ustoz AI"}],
            [{"text": "🔙 Ortga"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def back_keyboard():
    return {
        "keyboard": [
            [{"text": "🔙 Ortga"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


# =========================
# INLINE CHEK TUGMASI
# =========================

def receipt_keyboard():
    return {
        "inline_keyboard": [
            [
                {
                    "text": "📸 Chekni yuborish",
                    "url": "https://t.me/MERAN_EDU"
                }
            ]
        ]
    }


# =========================
# TEXTLAR
# =========================

START_TEXT = """🎓 MERAN EDUCATION BOT📚

Assalomu alaykum! 👋
MERAN EDUCATION bilim maskaniga xush kelibsiz!

Kerakli bo‘limni tanlang:
"""


MATERIALS_TEXT = """📚 O‘QUV MATERIALLARI

Kerakli bo‘limni tanlang:
"""


LITERATURE_TEXT = """📖 ADABIYOT

Kerakli bo‘limni tanlang:
"""


TESTS_TEXT = """💳 TO‘LOV QILISH

🔐 Ushbu xizmatdan foydalanish obuna asosida amalga oshiriladi.

🔹 1 oylik obuna — 30 000 so‘m

🔹 2 oylik obuna — 50 000 so‘m

💳 Karta raqami:

9860 1601 3522 3172

Nargiza Samandarova

📞 Qo‘shimcha ma‘lumot olish uchun:

@Meran_education
"""


PROMO_TEXT = """📱 O‘zingizga kerakli ilovani tanlang va obuna promo-kodini xarid qiling:
"""


IBRAT_TEXT = """🎓 IBRAT ACADEMY

📱 Ibrat Academy uchun obuna promo-kodi.

💳 Promo-kod narxi:
🔹 79 000 so‘m

📅 Obuna muddati:
🔹 3 oy

💳 Karta raqami:

9860 1601 3522 3172

Nargiza Samandarova

📌 To‘lovni amalga oshirgandan so‘ng, chekni yuboring.

📞 Qo‘shimcha ma‘lumot uchun:
@Meran_education
"""


MUTOLAA_TEXT = """📚 MUTOLAA

📱 Mutolaa uchun obuna promo-kodi.

💳 Promo-kod narxi:
🔹 49 000 so‘m

📅 Obuna muddati:
🔹 3 oy

💳 Karta raqami:

9860 1601 3522 3172

Nargiza Samandarova

📌 To‘lovni amalga oshirgandan so‘ng, chekni yuboring.

📞 Qo‘shimcha ma‘lumot uchun:
@Meran_education
"""


UZCHESS_TEXT = """♟️ UZCHESS

📱 UZchess uchun obuna promo-kodi.

💳 Promo-kod narxi:
🔹 39 000 so‘m

📅 Obuna muddati:
🔹 3 oy

💳 Karta raqami:

9860 1601 3522 3172

Nargiza Samandarova

📌 To‘lovni amalga oshirgandan so‘ng, chekni yuboring.

📞 Qo‘shimcha ma‘lumot uchun:
@Meran_education
"""


USTOZ_TEXT = """🤖 USTOZ AI

📱 Ustoz AI uchun obuna promo-kodi.

💳 Promo-kod narxi:
🔹 129 000 so‘m

📅 Obuna muddati:
🔹 1 yil

💳 Karta raqami:

9860 1601 3522 3172

Nargiza Samandarova

📌 To‘lovni amalga oshirgandan so‘ng, chekni yuboring.

📞 Qo‘shimcha ma‘lumot uchun:
@Meran_education
"""


ABOUT_TEXT = """ℹ️ BIZ HAQIMIZDA

🎓 MERAN EDUCATION — bilim olish, rivojlanish va zamonaviy ta’lim imkoniyatlarini bir joyda jamlagan ta’lim platformasi.

📚 Bizning asosiy yo‘nalishlarimiz:
— 📖 Adabiy asarlar va o‘quv materiallari
— 📝 Mavzulashtirilgan testlar
— 🎁 Foydali ta’limiy platformalar uchun promo-kodlar

🚀 MERAN EDUCATION — bilim sari birgalikda!

📞 Murojaat uchun:
@Meran_education
"""


WORKS_TEXT = """📚 ASARLAR

Hozircha asarlar ro‘yxati qo‘shilmagan.

Tez orada 36 ta asar Telegram kanalidagi PDF fayllarga havola bilan joylashtiriladi.
"""


KIDS_TEXT = """👶 MERAN KIDS

Ushbu bo‘lim tez orada ishga tushadi. 🚀
"""


# =========================
# MESSAGE HANDLER
# =========================

def handle_message(chat_id, text):

    # =========================
    # START
    # =========================

    if text == "/start":
        user_states[chat_id] = "main"
        send_message(
            chat_id,
            START_TEXT,
            main_keyboard()
        )
        return


    # =========================
    # MAIN MENU
    # =========================

    if text == "📚 O‘quv materiallari":
        user_states[chat_id] = "materials"

        send_message(
            chat_id,
            MATERIALS_TEXT,
            materials_keyboard()
        )
        return


    if text == "👶 MERAN KIDS":
        user_states[chat_id] = "kids"

        send_message(
            chat_id,
            KIDS_TEXT,
            back_keyboard()
        )
        return


    if text == "🎁 Promo kodlar":
        user_states[chat_id] = "promo"

        send_message(
            chat_id,
            PROMO_TEXT,
            promo_keyboard()
        )
        return


    if text == "ℹ️ Biz haqimizda":
        user_states[chat_id] = "about"

        send_message(
            chat_id,
            ABOUT_TEXT,
            back_keyboard()
        )
        return


    # =========================
    # O‘QUV MATERIALLARI
    # =========================

    if text == "📖 Adabiyot":
        user_states[chat_id] = "literature"

        send_message(
            chat_id,
            LITERATURE_TEXT,
            literature_keyboard()
        )
        return


    # =========================
    # ASARLAR
    # =========================

    if text == "📚 Asarlar":
        user_states[chat_id] = "works"

        send_message(
            chat_id,
            WORKS_TEXT,
            back_keyboard()
        )
        return


    # =========================
    # MAVZULASHTIRILGAN TESTLAR
    # =========================

    if text == "📝 Mavzulashtirilgan testlar":

        # Foydalanuvchi Adabiyot menyusida qoladi
        user_states[chat_id] = "literature"

        # Faqat to‘lov xabari chiqadi
        # Avtomatik "🔙 Ortga" xabari YO‘Q
        send_message(
            chat_id,
            TESTS_TEXT,
            receipt_keyboard()
        )
        return


    # =========================
    # PROMO — IBRAT
    # =========================

    if text == "🎓 Ibrat Academy":

        # Promo menyusi holatda qoladi
        user_states[chat_id] = "promo"

        # Faqat mahsulot ma‘lumoti chiqadi
        send_message(
            chat_id,
            IBRAT_TEXT,
            receipt_keyboard()
        )
        return


    # =========================
    # PROMO — MUTOLAA
    # =========================

    if text == "📚 Mutolaa":

        user_states[chat_id] = "promo"

        send_message(
            chat_id,
            MUTOLAA_TEXT,
            receipt_keyboard()
        )
        return


    # =========================
    # PROMO — UZCHESS
    # =========================

    if text == "♟️ UZchess":

        user_states[chat_id] = "promo"

        send_message(
            chat_id,
            UZCHESS_TEXT,
            receipt_keyboard()
        )
        return


    # =========================
    # PROMO — USTOZ AI
    # =========================

    if text == "🤖 Ustoz AI":

        user_states[chat_id] = "promo"

        send_message(
            chat_id,
            USTOZ_TEXT,
            receipt_keyboard()
        )
        return


    # =========================
    # ORTGA
    # =========================

    if text == "🔙 Ortga":

        current_state = user_states.get(chat_id, "main")


        # Adabiyot → O‘quv materiallari
        if current_state == "literature":
            user_states[chat_id] = "materials"

            send_message(
                chat_id,
                MATERIALS_TEXT,
                materials_keyboard()
            )
            return


        # Asarlar → Adabiyot
        if current_state == "works":
            user_states[chat_id] = "literature"

            send_message(
                chat_id,
                LITERATURE_TEXT,
                literature_keyboard()
            )
            return


        # Testlar → Adabiyot
        if current_state == "tests":
            user_states[chat_id] = "literature"

            send_message(
                chat_id,
                LITERATURE_TEXT,
                literature_keyboard()
            )
            return


        # Promo mahsulot → Promo kodlar
        if current_state == "promo":
            user_states[chat_id] = "promo"

            send_message(
                chat_id,
                PROMO_TEXT,
                promo_keyboard()
            )
            return


        # Promo menyusi → Bosh menyu
        if current_state == "promo_main":
            user_states[chat_id] = "main"

            send_message(
                chat_id,
                START_TEXT,
                main_keyboard()
            )
            return


        # O‘quv materiallari → Bosh menyu
        if current_state == "materials":
            user_states[chat_id] = "main"

            send_message(
                chat_id,
                START_TEXT,
                main_keyboard()
            )
            return


        # MERAN KIDS → Bosh menyu
        if current_state == "kids":
            user_states[chat_id] = "main"

            send_message(
                chat_id,
                START_TEXT,
                main_keyboard()
            )
            return


        # Biz haqimizda → Bosh menyu
        if current_state == "about":
            user_states[chat_id] = "main"

            send_message(
                chat_id,
                START_TEXT,
                main_keyboard()
            )
            return


        # Boshqa holatlarda
        user_states[chat_id] = "main"

        send_message(
            chat_id,
            START_TEXT,
            main_keyboard()
        )
        return


# =========================
# FLASK
# =========================

@app.route("/", methods=["GET"])
def home():
    return "MERAN EDUCATION BOT ishlayapti! ✅", 200


@app.route("/webhook", methods=["POST"])
def webhook():

    update = request.get_json()

    if not update:
        return "OK", 200

    if "message" in update:

        message = update["message"]

        chat_id = message["chat"]["id"]

        text = message.get("text", "")

        handle_message(
            chat_id,
            text
        )

    return "OK", 200


# =========================
# RUN
# =========================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
