from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from aiogram.types import Message
from .start import translations
from keyboards.default.week_days import week_days_en, week_days_ru, week_days_uz
from .menu_config import json_opener



@dp.message_handler(text=['🔗 Ulashish', '🔗 Делиться', '🔗 Share'])
async def table(message: Message):
    data = json_opener()
    print("my data is sdvnsdn ",data)
    lang = data[f"{message.from_user.id}"]
    a = {
        "uz":f"uchun kalit `asd-fgh-hjk`",
        "ru":f"Ключ для бота `asd-fgh-hjk`",
        "en":f"Key for the bot `asd-fgh-hjk`"
    }

    share = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=translations['share'][lang], switch_inline_query=a[lang])
            ]
        ]
    )
    await message.answer(text=translations['choose_day_of_the_week'][lang], reply_markup=share)