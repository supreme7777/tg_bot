import asyncio
import logging
import openai
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from openai import OpenAI
from config import TOKEN, OPENAI_API_KEY

# OpenAI mijozini sozlash
client = OpenAI(api_key=OPENAI_API_KEY)

# Bot va dispatcher
dp = Dispatcher()
bot = Bot(TOKEN)
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

# OpenAI bilan ishlov berish funksiyasi
async def process_text(text, task="edit"):
    prompt = f"'{text}' matnini {task} qilib yoz."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content

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

@dp.message()
async def handle_text(message: types.Message):
    user_text = message.text
    processed_text = await process_text(user_text, "tahrirlash")
    await message.answer(f"📌 Tahrirlangan matn:\n\n{processed_text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
