import random

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from loader import db, dp
from states.quetions import MainState


@dp.callback_query_handler(lambda callback_query: True, state=MainState.one)
async def show_item(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'back':
        await callback.message.delete()
        await callback.message.answer('Bosh Menu')
        await state.finish()
    else:
        category = callback.data.split('_')
        await state.update_data(
            {'category': category[1]}
        )

        counter = await db.count_quetions(id=category[1])
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=int(category[1]), que_id=number)
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"1.{item['savol']}"
            else:
                text = f"1.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_1': f"{item['javobi']}",
                    'ans_1_text': f"{item['savol']}"
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.two.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.two)
async def show_item2(callback: CallbackQuery, state: FSMContext):
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
                       f"2.{item['savol']}"
            else:
                text = f"2.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_2': f"{item['javobi']}",
                    'ans_2_text': f"{item['savol']}",
                    'ans_1_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.three.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        # markup = await categories_keyboard()
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"2.{item['savol']}"
            else:
                text = f"2.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_2': f"{item['javobi']}",
                    'ans_2_text': f"{item['savol']}",
                    'ans_1_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.three.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.three)
async def show_item3(callback: CallbackQuery, state: FSMContext):
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
                       f"3.{item['savol']}"
            else:
                text = f"3.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_3': f"{item['javobi']}",
                    'ans_3_text': f"{item['savol']}",
                    'ans_2_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.four.set()
    else:
        data = await state.get_data()
        id = data.get('category')
        counter = await db.count_quetions(id=id)
        number = random.randint(1, counter)
        quetions = await db.get_product(cat_id=id, que_id=number)
        # markup = await categories_keyboard()
        markup = InlineKeyboardMarkup(row_width=2)

        for item in quetions:
            if item["photo"]:
                text = f"<a href=\"{item['photo']}\">&#8205;</a>" \
                       f"3.{item['savol']}"
            else:
                text = f"3.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_3': f"{item['javobi']}",
                    'ans_3_text': f"{item['savol']}",
                    'ans_2_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.four.set()


@dp.callback_query_handler(lambda callback_query: True, state=MainState.four)
async def show_item4(callback: CallbackQuery, state: FSMContext):
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
                       f"4.{item['savol']}"
            else:
                text = f"4.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_4': f"{item['javobi']}",
                    'ans_4_text': f"{item['savol']}",
                    'ans_3_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.five.set()
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
                       f"4.{item['savol']}"
            else:
                text = f"4.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_4': f"{item['javobi']}",
                    'ans_4_text': f"{item['savol']}",
                    'ans_3_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.five.set()

@dp.callback_query_handler(lambda callback_query: True, state=MainState.five)
async def show_item5(callback: CallbackQuery, state: FSMContext):
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
                       f"5.{item['savol']}"
            else:
                text = f"5.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_5': f"{item['javobi']}",
                    'ans_5_text': f"{item['savol']}",
                    'ans_4_status': 'bad'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.six.set()
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
                       f"5.{item['savol']}"
            else:
                text = f"5.{item['savol']}"

            if item['manbaa']:
                text += f"\n\n{item['manbaa']}"

            markup.row(
                InlineKeyboardButton(text=f"{item['javob_1']}", callback_data='1')
            )
            markup.insert(
                InlineKeyboardButton(text=f"{item['javob_2']}", callback_data='2')
            )
            if item['javob_3']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_3']}", callback_data='3')
                )
            if item['javob_4']:
                markup.insert(
                    InlineKeyboardButton(text=f"{item['javob_4']}", callback_data='4')
                )

            markup.add(
                InlineKeyboardButton(text='Bilmayman', callback_data='field')
            )
            await state.update_data(
                {
                    'ans_5': f"{item['javobi']}",
                    'ans_5_text': f"{item['savol']}",
                    'ans_4_status': 'good'
                }
            )
            await callback.message.edit_text(text=text, reply_markup=markup)
            await MainState.six.set()
