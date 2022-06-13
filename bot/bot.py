import time
import logging

from aiogram import Bot, Dispatcher, executor, types

from config.bot_token import TOKEN


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'Hello, {user_name}!'
    logging.info(f'first start from user_name = {user_name}, user_id = {user_id}')
    await message.reply(text)

    
@dp.message_handler()
async def make_echo(message):
    user_name = message.from_user.first_name
    chat_id = message.from_user.id
    echo = message.text
    await bot.send_message(chat_id, echo)
    with open(f'data/{user_name}_{chat_id}.txt', 'a') as f:
        f.write(f'{time.asctime()} - {echo}\n')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)