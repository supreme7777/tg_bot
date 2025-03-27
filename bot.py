import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN

# Bot va dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
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

@dp.message(F.text.eq("/start"))
async def start_cmd(message: types.Message):
    await message.answer("Salom! Men sizga yordam bera olmaydigan Telegram botman. Pastdagi tugmalar orqali xizmatlardan foydalaning.", reply_markup=menu_keyboard)

@dp.message(F.text.eq("AI"))
async def services_cmd(message: types.Message):
    await message.answer("- AI yordamida matn yozish\n- Dizayn xizmatlari\n- Freelancer yordam", reply_markup=menu_keyboard)

@dp.message(F.text.eq("Taxta"))
async def taxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text.eq("Shaxta"))
async def shaxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text.eq("Paxta"))
async def paxta_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text.eq("📞 Aloqa"))
async def contact_cmd(message: types.Message):
    await message.answer("Bog‘lanish uchun: @asadbek7r")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
