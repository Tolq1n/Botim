from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import json
from loader import dp
from keyboards.default.menu_keyboard import menu_en, menu_ru, menu_uz
from keyboards.inline.inline_lang import language

# Load translation files
with open("translations.json", "r") as file:
    translations = json.load(file)

def json_opener():
    with open("user_info.json", "r") as file:
        return json.load(file)
    


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    user_id = message.from_user.id

    try:
        data = json_opener()
        lang = data[f"{user_id}"]
        menu_button=f'menu_{lang}'
        print(menu_button)
        menu_markup = menu_en if lang == 'en' else menu_ru if lang == 'ru' else menu_uz
        await message.answer(text = translations['select_menu'][lang], reply_markup=menu_markup)
    except Exception as err:
        print(err)
        try:
            lang = message.from_user.language_code
            await message.answer(text = f"Salom, {message.from_user.full_name}\n {translations['choose_language'][lang]}", reply_markup=language)
        except:
            await message.answer(text = f"Salom, {message.from_user.full_name}\n {translations['choose_language']['ru']}", reply_markup=language)


