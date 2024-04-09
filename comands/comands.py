import asyncio

import app_logger as log
from aiogram import types
from defs.classes import User


log = log.get_logger(__name__)


async def cmd_start(message: types.Message):#, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка старт. ' + u.info_user())
    await message.answer('OK start')


async def cmd_help(message: types.Message):#, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка хэлп ' + u.info_user())
    await message.answer('OK help')
