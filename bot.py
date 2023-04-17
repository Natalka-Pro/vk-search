from aiogram import Bot, Dispatcher, executor, types

# Ссылка на бота: https://t.me/vk_search_1984_bot

# В одинарных кавычках размещаем токен, полученный от @BotFather.
API_TOKEN = '5832369881:AAEO3bFyKuciITnHQ2bQ91BvWZTulIfDUK8' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Явно указываем в декораторе, на какую команду реагируем. 
@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    # Так как код работает асинхронно, то обязательно пишем await.
    await message.reply(
        "Привет!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")


# Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
@dp.message_handler()
# Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
async def echo(message: types.Message):
    if "ня" in message.text.lower() or "nya" in message.text.lower():
        await message.answer("Мя!")
    else:
        await message.answer(f"""Нет, ты "{message.text}".""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
