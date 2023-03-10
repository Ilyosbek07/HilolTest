import random

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from loader import db, dp
from states.quetions import MainState


@dp.callback_query_handler(lambda callback_query: True, state=MainState.six)
async def show_item6(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'field':
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"6.{item['savol']}"
            else:
                text = f"6.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_5': f"{callback.data}",
                    'ans_6': f"{ans_text}",
                    'ans_6_text': f"{item['savol']}",
                    'ans_5_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.seven.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"6.{item['savol']}"
            else:
                text = f"6.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_5': f"{callback.data}",
                    'ans_6': f"{ans_text}",
                    'ans_6_text': f"{item['savol']}",
                    'ans_5_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.seven.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.seven)
async def show_item7(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'field':
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"7.{item['savol']}"
            else:
                text = f"7.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"
            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'ans_7': f"{ans_text}",
                    'ans_7_text': f"{item['savol']}",
                    'ans_6_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.eight.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"7.{item['savol']}"
            else:
                text = f"7.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_6': f"{callback.data}",
                    'ans_7': f"{ans_text}",
                    'ans_7_text': f"{item['savol']}",
                    'ans_6_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.eight.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.eight)
async def show_item8(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'field':
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"8.{item['savol']}"
            else:
                text = f"8.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"
            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_7': f"{callback.data}",
                    'ans_8': f"{ans_text}",
                    'ans_8_text': f"{item['savol']}",
                    'ans_7_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.nine.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"8.{item['savol']}"
            else:
                text = f"8.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"
            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_7': f"{callback.data}",
                    'ans_8': f"{ans_text}",
                    'ans_8_text': f"{item['savol']}",
                    'ans_7_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.nine.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.nine)
async def show_item9(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'field':
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"9.{item['savol']}"
            else:
                text = f"9.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_8': f"{callback.data}",
                    'ans_9': f"{ans_text}",
                    'ans_9_text': f"{item['savol']}",
                    'ans_8_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.ten.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"9.{item['savol']}"
            else:
                text = f"9.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"
            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_8': f"{callback.data}",
                    'ans_9': f"{ans_text}",
                    'ans_9_text': f"{item['savol']}",
                    'ans_8_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.ten.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.ten)
async def show_item10(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'field':
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"10.{item['savol']}"
            else:
                text = f"10.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_9': f"{callback.data}",
                    'ans_10': f"{ans_text}",
                    'ans_10_text': f"{item['savol']}",
                    'ans_9_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.finish.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"10.{item['savol']}"
            else:
                text = f"10.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            javob_1 = f"{item['javob_1']}"
            javob_2 = f"{item['javob_2']}"
            markup.row(
                InlineKeyboardButton(text=javob_1, callback_data=javob_1)
            )
            markup.insert(
                InlineKeyboardButton(text=javob_2, callback_data=javob_2)
            )
            if item['javob_3']:
                javob_3 = f"{item['javob_3']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_3, callback_data=javob_3)
                )
            if item['javob_4']:
                javob_4 = f"{item['javob_4']}"

                markup.insert(
                    InlineKeyboardButton(text=javob_4, callback_data=javob_4)
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            ans_id = f'javob_{item["javobi"]}'
            ans_text = f"{item[ans_id]}"
            await state.update_data(
                {
                    'user_ans_9': f"{callback.data}",
                    'ans_10': f"{ans_text}",
                    'ans_10_text': f"{item['savol']}",
                    'ans_9_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.finish.set()


