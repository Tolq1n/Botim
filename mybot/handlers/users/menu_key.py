from loader import dp
from aiogram.types import Message
from .start import translations
from keyboards.default.key import key_en, key_ru, key_uz
from .menu_config import json_opener



@dp.message_handler(text=['🔑 Kalit', '🔑 Ключ', '🔑 Key'])
async def table(message: Message):
    data = json_opener()
    print("my data is sdvnsdn ",data)
    lang = data[f"{message.from_user.id}"]
    key = key_en if lang == 'en' else key_ru if lang == 'ru' else key_uz
    await message.answer(text=translations['choose_action'][lang], reply_markup=key)