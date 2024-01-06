from loader import dp
from aiogram.types import Message
from .start import translations
import json
from keyboards.inline.inline_lang import language
from keyboards.default.change_lang import change_lang_en, change_lang_ru, change_lang_uz

def json_opener():
    with open("user_info.json", "r") as file:
        return json.load(file)

@dp.message_handler(text=['⚙️ Настройки', '⚙️ Configuration', '⚙️ Sozlamalar'])
async def configuration(message: Message):
    data = json_opener()
    print("my data is sdvnsdn ",data)
    lang = data[f"{message.from_user.id}"]
    chang_lang = change_lang_en if lang == 'en' else change_lang_ru if lang == 'ru' else change_lang_uz
    await message.answer(text=translations['choose_action'][lang], reply_markup=chang_lang)


@dp.message_handler(text=["🔄 Изменить язык", "🔄 Tilni o'zgartirish", "🔄 Change the language"])
async def lang_configuration(message: Message):
    data = json_opener()
    lang = data[f"{message.from_user.id}"]
    await message.answer(text=translations['choose_language'][lang], reply_markup=language)
    