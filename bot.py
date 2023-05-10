from aiogram import Bot, Dispatcher, executor, types
from vk_requests import get_friends
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# aiogram==2.25.1
# Link to the bot: https://t.me/vk_search_1984_bot

# Token from @BotFather
API_TOKEN = '5832369881:AAEO3bFyKuciITnHQ2bQ91BvWZTulIfDUK8' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help']) 
async def help(message: types.Message):
    with open('help.txt', 'r') as file:
        mes = file.read()
    await message.answer(mes)
    

@dp.message_handler(commands=['start']) 
async def start(message: types.Message):
    await message.answer(
        "Привет!\nЕсли не знаешь, что сказать, напиши /help.")


@dp.message_handler(commands=['friends_name']) 
async def friends_name(message: types.Message, command):
    if command.args:
        await message.answer(f"Сейчас посчитаю друзей у {command.args}")

        access_token = 'eaae23abeaae23abeaae23abdbe9bdb8f1eeaaeeaae23ab8e923c275dce8f0a13fa6e39'
        # user_id = "https://vk.com/strong_machina"
        user_id = command.args
        num_friends, list_friends = await get_friends(access_token, user_id)
        await message.answer(f"Ответ: {num_friends} друзей")
    else:
        await message.answer("Пожалуйста, укажите аккаунт после команды /friends_name!")


@dp.message_handler()
async def echo(message: types.Message):
    if "ня" in message.text.lower() or "nya" in message.text.lower():
        await message.answer("Мя!")
    else:
        await message.answer(f"""Нет, ты "{message.text}".""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)