from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


language = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿 O'zb", callback_data="uz"),
        InlineKeyboardButton(text="🇷🇺 Рус", callback_data="ru"),
        InlineKeyboardButton(text="🇬🇧 Eng", callback_data="en")
    ],
])