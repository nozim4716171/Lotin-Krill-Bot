from aiogram.dispatcher.filters.state import StatesGroup,State


class Example(StatesGroup):
    to_latin = State()
    to_cyrillic = State()