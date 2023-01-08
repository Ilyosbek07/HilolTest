from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Mashqlar")
        ],
        [
            KeyboardButton(text='⚔️ Bellashuv'),
            KeyboardButton(text="❓ Qo'llanma")
        ],
        [
            KeyboardButton(text='🔧 Sozlamalar')
        ]
    ],
    resize_keyboard=True
)