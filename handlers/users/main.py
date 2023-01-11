from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from states.quetions import MainState


@dp.callback_query_handler(lambda callback_query: True, state=MainState.finish)
async def finish(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'field':
        await state.update_data(
            {
                'ans_10_status': 'bad'
            }
        )
        data = await state.get_data()
        text = '1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟\n'
        bad = '========================\n\n' \
              '🔽 ❓Xatolaringiz va ☑️ javoblari: 🔽\n\n'

        if data.get('ans_1_status') == 'good':
            if data.get('user_ans_1') == data.get('ans_1'):
                text += '✅'
            else:
                text += '❌'
                bad += f"1.❌ {data.get('ans_1_text')}\n" \
                       f"☑️ {data.get('ans_1')}\n\n"
        else:
            text += '❓'
            bad += f"1.❓ {data.get('ans_1_text')}\n" \
                   f"☑️ {data.get('ans_1')}\n\n"
        if data.get('ans_2_status') == 'good':
            if data.get('user_ans_2') == data.get('ans_2'):
                text += '✅'
            else:
                text += '❌'
                bad += f"2.❌ {data.get('ans_2_text')}\n" \
                       f"☑️ {data.get('ans_2')}\n\n"
        else:
            text += '❓'
            bad += f"2.❓ {data.get('ans_2_text')}\n" \
                   f"☑️ {data.get('ans_2')}\n\n"

        if data.get('ans_3_status') == 'good':
            if data.get('user_ans_3') == data.get('ans_3'):
                text += '✅'
            else:
                text += '❌'
                bad += f"3.❌ {data.get('ans_3_text')}\n" \
                       f"☑️ {data.get('ans_3')}\n\n"
        else:
            text += '❓'
            bad += f"3.❓ {data.get('ans_3_text')}\n" \
                   f"☑️ {data.get('ans_3')}\n\n"

        if data.get('ans_4_status') == 'good':
            if data.get('user_ans_4') == data.get('ans_4'):
                text += '✅'
            else:
                text += '❌'
                bad += f"4.❌ {data.get('ans_4_text')}\n" \
                       f"☑️ {data.get('ans_4')}\n\n"
        else:
            text += '❓'
            bad += f"4.❓ {data.get('ans_4_text')}\n" \
                   f"☑️ {data.get('ans_4')}\n\n"

        if data.get('ans_5_status') == 'good':
            if data.get('user_ans_5') == data.get('ans_5'):
                text += '✅'
            else:
                text += '❌'
                bad += f"5.❌ {data.get('ans_5_text')}\n" \
                       f"☑️ {data.get('ans_5')}\n\n"
        else:
            text += '❓'
            bad += f"5.❓ {data.get('ans_5_text')}\n" \
                   f"☑️ {data.get('ans_5')}\n\n"

        if data.get('ans_6_status') == 'good':
            if data.get('user_ans_6') == data.get('ans_6'):
                text += '✅'
            else:
                text += '❌'
                bad += f"6.❌ {data.get('ans_6_text')}\n" \
                       f"☑️ {data.get('ans_6')}\n\n"
        else:
            text += '❓'
            bad += f"6.❓ {data.get('ans_6_text')}\n" \
                   f"☑️ {data.get('ans_6')}\n\n"

        if data.get('ans_7_status') == 'good':
            if data.get('user_ans_7') == data.get('ans_7'):
                text += '✅'
            else:
                text += '❌'
                bad += f"7.❌ {data.get('ans_7_text')}\n" \
                       f"☑️ {data.get('ans_7')}\n\n"
        else:
            text += '❓'
            bad += f"7.❓ {data.get('ans_7_text')}\n" \
                   f"☑️ {data.get('ans_7')}\n\n"

        if data.get('ans_8_status') == 'good':
            if data.get('user_ans_8') == data.get('ans_8'):
                text += '✅'
            else:
                text += '❌'
                bad += f"8.❌ {data.get('ans_8_text')}\n" \
                       f"☑️ {data.get('ans_8')}\n\n"
        else:
            text += '❓'
            bad += f"8.❓ {data.get('ans_8_text')}\n" \
                   f"☑️ {data.get('ans_8')}\n\n"

        if data.get('ans_9_status') == 'good':
            if data.get('user_ans_9') == data.get('ans_9'):
                text += '✅'
            else:
                text += '❌'
                bad += f"9.❌ {data.get('ans_9_text')}\n" \
                       f"☑️ {data.get('ans_9')}\n\n"
        else:
            text += '❓'
            bad += f"9.❓ {data.get('ans_9_text')}\n" \
                   f"☑️ {data.get('ans_9')}\n\n"

        if data.get('ans_10_status') == 'good':
            if data.get('user_ans_3') == data.get('ans_3'):
                text += '✅'
            else:
                text += '❌'
                bad += f"10.❌ {data.get('ans_10_text')}\n" \
                       f"☑️ {data.get('ans_10')}\n\n"
        else:
            text += '❓'
            bad += f"10.❓ {data.get('ans_10_text')}\n" \
                   f"☑️ {data.get('ans_10')}\n\n"

        await callback.message.answer(text=f"🧾#natija {callback.from_user.full_name}\n\n"
                                           f"{text}\n\n"
                                           f"{bad}")

        await state.finish()
    else:
        await state.update_data(
            {
                'user_ans_10': f"{callback.data}",
                'ans_10_status': 'good'
            }
        )
        data = await state.get_data()
        text = '1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟\n'
        bad = '========================\n\n' \
              '🔽 ❓Xatolaringiz va ☑️ javoblari: 🔽\n\n'

        if data.get('ans_1_status') == 'good':
            if data.get('user_ans_1') == data.get('ans_1'):
                text += '✅'
            else:
                text += '❌'
                bad += f"1.❌ {data.get('ans_1_text')}\n" \
                       f"☑️ {data.get('ans_1')}\n\n"
        else:
            text += '❓'
            bad += f"1.❓ {data.get('ans_1_text')}\n" \
                   f"☑️ {data.get('ans_1')}\n\n"
        if data.get('ans_2_status') == 'good':
            if data.get('user_ans_2') == data.get('ans_2'):
                text += '✅'
            else:
                text += '❌'
                bad += f"2.❌ {data.get('ans_2_text')}\n" \
                       f"☑️ {data.get('ans_2')}\n\n"
        else:
            text += '❓'
            bad += f"2.❓ {data.get('ans_2_text')}\n" \
                   f"☑️ {data.get('ans_2')}\n\n"

        if data.get('ans_3_status') == 'good':
            if data.get('user_ans_3') == data.get('ans_3'):
                text += '✅'
            else:
                text += '❌'
                bad += f"3.❌ {data.get('ans_3_text')}\n" \
                       f"☑️ {data.get('ans_3')}\n\n"
        else:
            text += '❓'
            bad += f"3.❓ {data.get('ans_3_text')}\n" \
                   f"☑️ {data.get('ans_3')}\n\n"

        if data.get('ans_4_status') == 'good':
            if data.get('user_ans_4') == data.get('ans_4'):
                text += '✅'
            else:
                text += '❌'
                bad += f"4.❌ {data.get('ans_4_text')}\n" \
                       f"☑️ {data.get('ans_4')}\n\n"
        else:
            text += '❓'
            bad += f"4.❓ {data.get('ans_4_text')}\n" \
                   f"☑️ {data.get('ans_4')}\n\n"

        if data.get('ans_5_status') == 'good':
            if data.get('user_ans_5') == data.get('ans_5'):
                text += '✅'
            else:
                text += '❌'
                bad += f"5.❌ {data.get('ans_5_text')}\n" \
                       f"☑️ {data.get('ans_5')}\n\n"
        else:
            text += '❓'
            bad += f"5.❓ {data.get('ans_5_text')}\n" \
                   f"☑️ {data.get('ans_5')}\n\n"

        if data.get('ans_6_status') == 'good':
            if data.get('user_ans_6') == data.get('ans_6'):
                text += '✅'
            else:
                text += '❌'
                bad += f"6.❌ {data.get('ans_6_text')}\n" \
                       f"☑️ {data.get('ans_6')}\n\n"
        else:
            text += '❓'
            bad += f"6.❓ {data.get('ans_6_text')}\n" \
                   f"☑️ {data.get('ans_6')}\n\n"

        if data.get('ans_7_status') == 'good':
            if data.get('user_ans_7') == data.get('ans_7'):
                text += '✅'
            else:
                text += '❌'
                bad += f"7.❌ {data.get('ans_7_text')}\n" \
                       f"☑️ {data.get('ans_7')}\n\n"
        else:
            text += '❓'
            bad += f"7.❓ {data.get('ans_7_text')}\n" \
                   f"☑️ {data.get('ans_7')}\n\n"

        if data.get('ans_8_status') == 'good':
            if data.get('user_ans_8') == data.get('ans_8'):
                text += '✅'
            else:
                text += '❌'
                bad += f"8.❌ {data.get('ans_8_text')}\n" \
                       f"☑️ {data.get('ans_8')}\n\n"
        else:
            text += '❓'
            bad += f"8.❓ {data.get('ans_8_text')}\n" \
                   f"☑️ {data.get('ans_8')}\n\n"

        if data.get('ans_9_status') == 'good':
            if data.get('user_ans_9') == data.get('ans_9'):
                text += '✅'
            else:
                text += '❌'
                bad += f"9.❌ {data.get('ans_9_text')}\n" \
                       f"☑️ {data.get('ans_9')}\n\n"
        else:
            text += '❓'
            bad += f"9.❓ {data.get('ans_9_text')}\n" \
                   f"☑️ {data.get('ans_9')}\n\n"

        if data.get('ans_10_status') == 'good':
            if data.get('user_ans_3') == data.get('ans_3'):
                text += '✅'
            else:
                text += '❌'
                bad += f"10.❌ {data.get('ans_10_text')}\n" \
                       f"☑️ {data.get('ans_10')}\n\n"
        else:
            text += '❓'
            bad += f"10.❓ {data.get('ans_10_text')}\n" \
                   f"☑️ {data.get('ans_10')}\n\n"

        await callback.message.answer(text=f"🧾#natija {callback.from_user.full_name}\n\n"
                                           f"{text}\n\n"
                                           f"{bad}")
        await state.finish()
