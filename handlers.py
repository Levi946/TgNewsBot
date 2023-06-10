from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard1, game_news_key, tech_news_key, cb

from main import bot, dp


@dp.message_handler(Command('news'))
async def show(message: Message):
    await message.answer(text='Выберите категорию новостей', reply_markup=keyboard1)

@dp.callback_query_handler(text_contains='phone')
async def game_news(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Новости об играх. Выберите интересующий вас сайт', reply_markup=game_news_key)

@dp.callback_query_handler(text_contains='mac')
async def tech_news(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Новости о технологиях. Выберите интересующий вас сайт', reply_markup=tech_news_key)

@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)


