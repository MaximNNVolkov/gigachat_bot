from aiogram import Router, F
from aiogram.filters.command import Command
from comands.comands import cmd_start, cmd_help
from middlewares.happy_month import ChatActionMiddleware


router = Router()


router.message.register(cmd_start, Command('start'))
router.message.register(cmd_help, Command('help'))
router.message.middleware(ChatActionMiddleware())
