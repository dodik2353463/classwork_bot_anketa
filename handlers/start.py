from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
import keyboards.start as kb_start


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    """ Обработка команды /start """
    # pylint:disable=C0415
    from main import bot
    await bot.set_my_commands([
        BotCommand(command = 'start', description='Запуск бота'),
        BotCommand(command = 'help', description='Справка'),
        BotCommand(command = 'delete', description='Отчислиться')
    ])

    await msg.answer(text='Страница1', reply_markup=kb_start.kb_next_btn)

@router.callback_query(F.data=='next')
async def next_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        'Страница 2', reply_markup=kb_start.kb_back_btn)

@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(
        text='Страница 1', reply_markup=kb_start.kb_next_btn)