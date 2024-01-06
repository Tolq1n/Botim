from loader import dp
from aiogram.types import Message
from .start import translations
from keyboards.default.week_days import week_days_en, week_days_ru, week_days_uz
from .menu_config import json_opener



@dp.message_handler(text=['🗓 Jadval', '🗓 Таблица', '🗓 Table'])
async def table(message: Message):
    data = json_opener()
    print("my data is sdvnsdn ",data)
    lang = data[f"{message.from_user.id}"]
    week_days = week_days_en if lang == 'en' else week_days_ru if lang == 'ru' else week_days_uz
    await message.answer(text=translations['choose_day_of_the_week'][lang], reply_markup=week_days)