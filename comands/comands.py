import app_logger as log
from aiogram import types
from defs.classes import User
from defs.token_access import take_response, MessageGenerator
from aiogram.fsm.context import FSMContext
from fsm.fsm_base import StateUser


log = log.get_logger(__name__)


async def cmd_start(message: types.Message):#, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка старт. ' + u.info_user())
    await message.answer('OK start')


async def cmd_help(message: types.Message):#, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка хэлп ' + u.info_user())
    await message.answer('OK help')


async def user_msg(message: types.Message):
    u = User(message.from_user)
    log.info('сообщение от пользователя' + u.info_user())
    res = await take_response(message.text)
    await message.answer(res)


async def cmd_role(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка роли'+ u.info_user())
    await state.set_state(StateUser.change_role)
    await message.answer('введите роль бота, например: Ты консультант по недвижимости')


async def change_role(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка роли'+ u.info_user())
    mg = MessageGenerator(message.text)
    await state.clear()
