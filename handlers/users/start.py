from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main import main
from keyboards.inline.categories import categories_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=main)


@dp.message_handler(text='📚 Mashqlar')
async def mashqlar(message: types.Message):
    markup = await categories_keyboard()
    await message.reply("Kerakli bo'limni tanlang", reply_markup=markup)

