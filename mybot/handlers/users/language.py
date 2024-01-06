from aiogram.types import CallbackQuery
from loader import dp
import time as times
import json
from keyboards.default.menu_keyboard import menu_en, menu_ru, menu_uz
from keyboards.inline.inline_lang import language
from .start import translations

def save_user_info(user_id, language):
    data = {}
    
    with open("user_info.json", "w") as file:
        file.write(json.dumps({user_id: language}))

        

@dp.callback_query_handler(text=["uz", "ru", "en"])
async def select_language(call: CallbackQuery):
    language = call.data
    user_id = call.message.chat.id
    save_user_info(user_id, language)
    
    if language == "uz":
        menu_markup = menu_uz
    elif language == "ru":
        menu_markup = menu_ru
    else:
        menu_markup = menu_en

    await call.message.delete()
    await call.message.answer(text=translations['select_menu'][language], reply_markup=menu_markup)