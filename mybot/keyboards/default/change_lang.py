from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#----------- CHANGE LANGUAGE -----------#

change_lang_uz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🔄 Tilni o'zgartirish"),
            KeyboardButton(text="⏰ Vaqtni sozlash"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ]
    ],
    resize_keyboard=True
)

change_lang_ru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🔄 Изменить язык"),
            KeyboardButton(text="⏰ Установка времени"),
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
        ]
    ],
    resize_keyboard=True
)

change_lang_en = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🔄 Change the language"),
            KeyboardButton(text="⏰ Setting the time"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]
    ],
    resize_keyboard=True
)

#----------- END CHANGE LANGUAGE ------------#