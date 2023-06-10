import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, loop=loop, storage=storage)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Для поиска новостей введите команду /news')


async def shutdown(dp):
    await storage.close()
    await bot.close()

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_shutdown=shutdown)