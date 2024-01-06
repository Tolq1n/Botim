from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#----------- MENU -----------#


menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 Jadval'),
            KeyboardButton(text='🔑 Kalit'),
        ],
        [
            KeyboardButton(text='⚙️ Sozlamalar'),
            KeyboardButton(text="ℹ️ Qo'llanma"),
        ],

    ],
    resize_keyboard=True
)


menu_ru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🗓 Таблица'),
            KeyboardButton(text='🔑 Ключ'),
        ],
        
        [
            KeyboardButton(text='⚙️ Настройки'),
            KeyboardButton(text='ℹ️ Руководство'),
        ],
    ],
    resize_keyboard=True
)

menu_en = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🗓 Table'),
            KeyboardButton(text='🔑 Key'),
        ],
        [
            KeyboardButton(text='⚙️ Configuration'),
            KeyboardButton(text='ℹ️ Manual'),
        ],
    ],
    resize_keyboard=True
)

#----------- END MENU -----------#
