from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Krill ➡️ Lotin"),
            KeyboardButton("Lotin ➡️ Krill")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)