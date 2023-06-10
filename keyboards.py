from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_TECHNEWS, URL_GAMENEWS, URL_GAMENEWS2, URL_TECHNEWS2

cb = CallbackData('buy', 'id', 'name', 'price')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Новости об играх', callback_data='buy:0:phone:1000'),
            InlineKeyboardButton(text='Новости о технологиях', callback_data='buy:1:mac:999999')
        ],
        [
            InlineKeyboardButton(text='Закрыть', callback_data='cancel')
        ]
    ]
)

game_news_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Перейти на StopGame', url=URL_GAMENEWS),
            InlineKeyboardButton('Перейти на VgTimes', url=URL_GAMENEWS2)
        ]
    ]
)

tech_news_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Перейти на Gazeta', url=URL_TECHNEWS),
            InlineKeyboardButton('Перейти на Hi-News', url=URL_TECHNEWS2)
        ]
    ]
)