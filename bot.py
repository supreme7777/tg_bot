import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN
from together import Together

# Together AI mijozini ishga tushirish
client = Together()

# Bot va dispatcher
bot = Bot(TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# Tugmalar menyusi
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="AI")],
        [KeyboardButton(text="Taxta"), KeyboardButton(text="Paxta")],
        [KeyboardButton(text="Shaxta"), KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

@dp.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer("Salom! Men sizga yordam bera olmaydigan Telegram botman. Pastdagi tugmalar orqali xizmatlardan foydalaning.", reply_markup=menu_keyboard)

@dp.message(F.text == "AI")
async def services_cmd(message: types.Message):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": "AI qanday yordam bera oladi?"}],
    )
    ai_response = response.choices[0].message.content
    await message.answer(ai_response, reply_markup=menu_keyboard)

@dp.message(F.text == "Taxta")
async def taxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text == "Shaxta")
async def shaxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text == "Paxta")
async def paxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text == "📞 Aloqa")
async def contact_cmd(message: types.Message):
    await message.answer("Bog‘lanish uchun: @asadbek7r")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
