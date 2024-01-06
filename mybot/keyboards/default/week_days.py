from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#----------- CHANGE LANGUAGE -----------#

week_days_uz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Dushanba"),
            KeyboardButton(text="Seshanba")
        ],
        [
            KeyboardButton(text="Chorshanba"),
            KeyboardButton(text="Payshanba")
        ],
        [
            KeyboardButton(text="Juma"),
            KeyboardButton(text="Shanba")
        ],
        [
            KeyboardButton(text="Yakshanba"),
            KeyboardButton(text="⬅️ Orqaga")
        ],
    ],
    resize_keyboard=True
)


week_days_en = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Monday"),
            KeyboardButton(text="Tuesday")
        ],
        [
            KeyboardButton(text="Wednesday"),
            KeyboardButton(text="Thursday")
        ],
        [
            KeyboardButton(text="Friday"),
            KeyboardButton(text="Saturday")
        ],
        [
            KeyboardButton(text="Sunday"),
            KeyboardButton(text="⬅️ Back")
        ],
    ],
    resize_keyboard=True
)

week_days_ru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Понедельник"),
            KeyboardButton(text="Вторник")
        ],
        [
            KeyboardButton(text="Среда"),
            KeyboardButton(text="Четверг")
        ],
        [
            KeyboardButton(text="Пятница"),
            KeyboardButton(text="Суббота")
        ],
        [
            KeyboardButton(text="Воскресенье"),
            KeyboardButton(text="⬅️ Назад")
        ],
    ],
    resize_keyboard=True
)
