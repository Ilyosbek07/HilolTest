from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db


async def categories_keyboard():
    # Eng yuqori 0-qavat ekanini ko'rsatamiz
    CURRENT_LEVEL = 0

    # Keyboard yaratamiz
    markup = InlineKeyboardMarkup(row_width=1)

    # Bazadagi barcha kategoriyalarni olamiz
    categories = await db.get_categories()
    # Har bir kategoriya uchun quyidagilarni bajaramiz:
    for category in categories:
        # Tugma matnini yasab olamiz
        button_text = f"{category['nomi']}"
        call_back = f"category_{category['call_back']}"
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=call_back)
        )
    markup.insert(
        InlineKeyboardButton(text='🔙 Bosh Sahifa', callback_data='back')
    )
    # Keyboardni qaytaramiz
    return markup
