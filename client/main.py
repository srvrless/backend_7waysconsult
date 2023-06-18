from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiohttp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")
BACKEND_URL = "http://localhost:8000/api"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def make_backend_request_post(endpoint, query):
    async with aiohttp.ClientSession() as session:
        async with session.post(BACKEND_URL + endpoint + f"?query={query}") as response:
            response_data = await response.json()
            return response_data


async def make_backend_request_get(endpoint):
    async with aiohttp.ClientSession() as session:
        async with session.get(BACKEND_URL + endpoint) as response:
            response_data = await response.json()
            return response_data


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Поиск ссылок", callback_data="search_links"),
        InlineKeyboardButton("Получить ссылки", callback_data="get_links"),
        InlineKeyboardButton("Отмена", callback_data="cancel"),
    )

    await message.reply("Выберите действие:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == "search_links")
async def search_links_callback_handler(callback_query: types.CallbackQuery):
    try:
        await bot.send_message(callback_query.from_user.id, "Введите текст запроса:")
    except Exception as e:
        await callback_query.reply(f"Something went wrong: {e}")


@dp.message_handler()
async def search_links_input_handler(message: types.Message):
    try:
        query = message.text
        response = await make_backend_request_post("/load_links", query)
        await message.reply(str(response))
    except Exception as e:
        await message.reply(f"Something went wrong{e}")


@dp.callback_query_handler(lambda c: c.data == "get_links")
async def get_links_callback_handler(callback_query: types.CallbackQuery):
    try:
        response = await make_backend_request_get("/links")
        await bot.send_message(callback_query.message.chat.id, str(response))
    except Exception as e:
        await bot.send_message(
            callback_query.message.chat.id, f"Something went wrong: {e}"
        )


@dp.callback_query_handler(lambda c: c.data == "cancel")
async def cancel_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.answer("Действие отменено.")


if __name__ == "__main__":
    executor.start_polling(dp)
