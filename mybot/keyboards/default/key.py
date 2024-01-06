from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



key_uz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="👑 Mening kalitim"),
            KeyboardButton(text="🆕 Yangi kalit"),
        ],
        [
            KeyboardButton(text="🔗 Ulashish"),
            KeyboardButton(text="⬅️ Orqaga"),
        ]
    ],
    resize_keyboard=True
)

key_ru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="👑 Мой ключ"),
            KeyboardButton(text="🆕 Новый ключ"),
        ],
        [
            KeyboardButton(text="🔗 Делиться"),
            KeyboardButton(text="⬅️ Назад"),
        ]
    ],
    resize_keyboard=True
)

key_en = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="👑 My key"),
            KeyboardButton(text="🆕 New key")
        ],
        [
            KeyboardButton(text="🔗 Share"),
            KeyboardButton(text="⬅️ Back"),
        ]
    ],
    resize_keyboard=True
)