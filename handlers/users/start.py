from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import random
from keyboards.default.main import main
from keyboards.inline.categories import categories_keyboard
from loader import dp, db, bot
from states.quetions import MainState


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message,state: FSMContext):
    if state:
        await state.finish()
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=main)


@dp.message_handler(text='📚 Mashqlar')
async def mashqlar(message: types.Message):
    markup = await categories_keyboard()
    await message.answer("Kerakli bo'limni tanlang", reply_markup=markup)
    await MainState.one.set()


