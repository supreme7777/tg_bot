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
        [KeyboardButton(text="🛍 Xizmatlar")],
        [KeyboardButton(text="💎 Premium obuna")],
        [KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

@dp.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer("Salom! Men sizga yordam bera oladigan Telegram botman. Pastdagi tugmalar orqali xizmatlardan foydalaning.", reply_markup=menu_keyboard)

@dp.message(F.text == "🛍 Xizmatlar")
async def services_cmd(message: types.Message):
    await message.answer("Bu yerda xizmatlaringizni sanab o‘tish mumkin. Masalan:\n- AI yordamida matn yozish\n- Dizayn xizmatlari\n- Freelancer yordamchi", reply_markup=menu_keyboard)

@dp.message(F.text == "💎 Premium obuna")
async def premium_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning!", reply_markup=menu_keyboard)

@dp.message(F.text == "📞 Aloqa")
async def contact_cmd(message: types.Message):
    await message.answer("Bog‘lanish uchun: @username")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
