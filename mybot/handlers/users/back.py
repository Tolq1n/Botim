from loader import dp
from aiogram.types import Message
from .start import translations
from keyboards.default.menu_keyboard import menu_en, menu_ru, menu_uz
# from keyboards.default.week_days import week_days_en, week_days_ru, week_days_uz
from . menu_config import json_opener



@dp.message_handler(text=['⬅️ Orqaga', '⬅️ Назад', '⬅️ Back'])
async def table(message: Message):
    data = json_opener()
    print("my data is sdvnsdn ",data)
    lang = data[f"{message.from_user.id}"]
    menu_markup = menu_en if lang == 'en' else menu_ru if lang == 'ru' else menu_uz
    await message.answer(text=translations['select_menu'][lang], reply_markup=menu_markup)