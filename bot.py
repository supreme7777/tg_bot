import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN

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
    await message.answer("- AI yordamida matn yozish\n- Dizayn xizmatlari\n- Freelancer yordam", reply_markup=menu_keyboard)

@dp.message(F.text == "Taxta")
async def taxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_
