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
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("AI"))
menu_keyboard.add(KeyboardButton("Taxta"))
menu_keyboard.add(KeyboardButton("Paxta"))
menu_keyboard.add(KeyboardButton("Shaxta"))
menu_keyboard.add(KeyboardButton("📞 Aloqa"))

@dp.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer("Salom! Men sizga yordam bera olmaydigan Telegram botman. Pastdagi tugmalar orqali xizmatlardan foydalaning.", reply_markup=menu_keyboard)

@dp.message(F.text == "AI")
async def services_cmd(message: types.Message):
    await message.answer("- AI yordamida matn yozish\n- Dizayn xizmatlari\n- Freelancer yordam", reply_markup=menu_keyboard)

@dp.message(F.text == "Taxta")
async def premium_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning! '(Склад {1/4} (Начался 7 мин. 7 сек. наз.)'", reply_markup=menu_keyboard)

@dp.message(F.text == "Shaxta")
async def premium_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning! '(Склад {1/4} (Начался 7 мин. 7 сек. наз.)'", reply_markup=menu_keyboard)

@dp.message(F.text == "Paxta")
async def premium_cmd(message: types.Message):
    await message.answer("Premium foydalanuvchilar uchun maxsus xizmatlar mavjud. Batafsil ma’lumot uchun biz bilan bog‘laning! '(Склад {1/4} (Начался 7 мин. 7 сек. наз.)'", reply_markup=menu_keyboard)

@dp.message(F.text == "📞 Aloqa")
async def contact_cmd(message: types.Message):
    await message.answer("Bog‘lanish uchun: @asadbek7r")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
