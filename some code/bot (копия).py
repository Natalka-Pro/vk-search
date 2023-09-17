from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as md

# from vk_requests import get_friends

# Link to the bot: https://t.me/vk_search_1984_bot

# Token from @BotFather
API_TOKEN = '5832369881:AAEO3bFyKuciITnHQ2bQ91BvWZTulIfDUK8' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# class VkSearch(StatesGroup):
#     choosing_food_name = State()
#     choosing_food_size = State()

@dp.message_handler(commands=['help']) 
async def help(message: types.Message):
    with open('help.txt', 'r') as file:
        mes = file.read()
    await message.answer(mes)
    

@dp.message_handler(commands=['start']) 
async def start(message: types.Message):
    await message.answer(
        "Привет!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp.message_handler(commands=['friends_name']) 
async def friends_name(message: types.Message, command):
    if command.args:
        await message.answer(f"Привет, {command.args}")
        # user_id = "https://vk.com/strong_machina"
        # num_friends, list_friends = await get_friends(access_token, user_id)

        # name = "lex"
        # res = find_friends(name, list_friends)
        # await 
    else:
        await message.answer("Пожалуйста, укажите аккаунт и имя после команды /friends_name!")

    # await message.answer(
    #     "Привет!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")
    

@dp.message_handler()
async def echo(message: types.Message):
    if "ня" in message.text.lower() or "nya" in message.text.lower():
        await message.answer("Мя!")
    else:
        await message.answer(f"""Нет, ты "{message.text}".""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
