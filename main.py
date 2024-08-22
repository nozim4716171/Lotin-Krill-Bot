from aiogram import Bot,Dispatcher,executor,types
from config import BOT_TOKEN
from example import to_cyrillic,to_latin
from states import Example
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from buttons import main_menu
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext


logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}",
                        reply_markup=main_menu)
    
    
@dp.message_handler(text="Krill ➡️ Lotin")
async def krill_to_latin_handler(message: types.Message):
    await message.answer("Керакли сўзни киритинг👇: ",reply_markup=ReplyKeyboardRemove())  
    await Example.to_latin.set()
    
@dp.message_handler(state=Example.to_latin)
async def to_latin_handler(message: types.Message, state: FSMContext):
    text = message.text
    result = to_latin(text)
    await message.answer(result,reply_markup=main_menu)
    await state.finish()
    
    
    
@dp.message_handler(text="Lotin ➡️ Krill")
async def latin_to_krill_handler(message: types.Message):
    await message.answer("Kerakli so'zni kiriting👇: ",reply_markup=ReplyKeyboardRemove())  
    await Example.to_cyrillic.set()
    
@dp.message_handler(state=Example.to_cyrillic)
async def to_krill_handler(message: types.Message, state: FSMContext):
    text = message.text
    result = to_cyrillic(text)
    await message.answer(result,reply_markup=main_menu)
    await state.finish()
    
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    


