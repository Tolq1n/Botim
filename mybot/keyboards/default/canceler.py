from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#----------- CHANGE LANGUAGE -----------#

cancel_time_uz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="❌ Bekor qilish"),
        ]
    ],
    resize_keyboard=True
)

cancel_time_ru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="❌ Отмена"),
        ]
    ],
    resize_keyboard=True
)

cancel_time_en = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="❌ Cancel"),
        ]
    ],
    resize_keyboard=True
)