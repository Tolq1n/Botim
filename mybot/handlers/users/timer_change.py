import re
from aiogram  import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.types import Message
from .start import translations
from states.time_conf import TimeChanger
from . menu_config import json_opener
from keyboards.default.canceler import cancel_time_en, cancel_time_ru, cancel_time_uz
from keyboards.default.change_lang import change_lang_en, change_lang_ru, change_lang_uz

@dp.message_handler(text=['⏰ Установка времени', '⏰ Vaqtni sozlash', '⏰ Setting the time'])
async def timer_changer(message: Message):
    data = json_opener()
    lang = data[f"{message.from_user.id}"]
    cancel = cancel_time_en if lang == 'en' else cancel_time_ru if lang == 'ru' else cancel_time_uz
    await bot.send_message(message.from_user.id, text=translations["change_time"][lang], reply_markup=cancel)
    await TimeChanger.mytimer.set()


@dp.message_handler(state=TimeChanger.mytimer)
async def answer_time(message: types.Message, state:FSMContext):
    REGEX = r'^(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
    data = json_opener()
    lang = data[f"{message.from_user.id}"]
    change_lang = change_lang_en if lang == 'en' else change_lang_ru if lang == 'ru' else change_lang_uz
    if re.match(REGEX, message.text):
        texter = (message.text).split(':')
        if len(texter[0]) != 2:
            message_text = '0' + texter[0] + ':' + texter[1]
        else:
            message_text = message.text
        print(message_text)
        await state.finish()
        await message.answer(text=translations["choose_action"][lang], reply_markup=change_lang)
    else:
        if message.text.startswith('❌Отменить') == True or message.text.startswith('❌ Bekor qilish') == True or message.text.startswith('❌ Cancel') == True:
            await message.answer(text=translations["canceled"][lang], reply_markup=change_lang)
        else:
            await message.answer(text=translations["correct_time"][lang], reply_markup=change_lang)
        
        await state.finish()