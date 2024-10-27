import asyncio

import docker
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import BotCommand
from aiogram.fsm.context import FSMContext
from docker_fun import get_all_cont, get_cont_id_by_name, get_cont_name_by_id, start_cont_by_id_or_name, \
    restart_cont_by_id_or_name, \
    stop_cont_by_id_or_name, remove_cont_by_id_or_name, run_cont_by_image
from status import DockerStates


BOT_TOKEN = "7508771900:AAFMfci5_swEKJ_eD1K0FiCx_zOr_wiUaeI"
bot = Bot(token= BOT_TOKEN)
dp = Dispatcher()
form_router = Router()
dp.include_router(form_router)
client = docker.from_env()

async def main() -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="/get_all_container", description="a"),
            BotCommand(command="/get_cont_id_by_name", description="av"),
            BotCommand(command="/get_cont_name_by_id", description="av"),
            BotCommand(command="/build_cont", description="ad"),
            BotCommand(command="/start_cont", description="ad"),
            BotCommand(command="/restart_cont", description="vds"),
            BotCommand(command="/stop_cont", description="sdvs"),
            BotCommand(command="/remote_cont", description="efs"),
        ]
    )
    await dp.start_polling(bot)


@dp.message(Command("get_all_container"))
async def bot_get_all_cont(message: types.message):
    list_cont = get_all_cont(client)
    names = ''
    for cont in list_cont:
        names += cont.name + '  \n'
    await message.answer(names)

@dp.message(Command("get_cont_id_by_name"))
async def bot_get_cont_id_by_name(message: types.message, state: FSMContext):
    await message.answer("Введите имя контейнера:")
    await state.set_state(DockerStates.get_cont_id_by_name)
@dp.message(DockerStates.get_cont_id_by_name)
async def get_name(message: types.message, state: FSMContext):
    id = get_cont_id_by_name(client,message.text)
    if id == "not exist":
        await message.answer("ошибка в имени, такого контейнера нет")
    else:
        await message.answer(f'id: {id}')
    await state.clear()

@dp.message(Command("get_cont_name_by_id"))
async def bot_get_cont_name_by_id(message: types.message, state: FSMContext):
    await message.answer("Введите id контейнера:")
    await state.set_state(DockerStates.get_cont_name_by_id)
@dp.message(DockerStates.get_cont_name_by_id)
async def get_id(message: types.message, state: FSMContext):
    name = get_cont_name_by_id(client, message.text)
    if name == 'not exist':
        await message.answer("ошибка в id, такого контейнера нет")
    else:
        await message.answer(f'name: {name}')
    await state.clear()


@dp.message(Command("start_cont"))
async def bot_start_cont(message: types.message, state: FSMContext):
    await message.answer("Введите имя или id контейнера:")
    await state.set_state(DockerStates.start_cont)
@dp.message(DockerStates.start_cont)
async def start_cont(message: types.message, state: FSMContext):
    id_or_name = message.text
    f = start_cont_by_id_or_name(client, id_or_name)
    await message.answer(f)
    await state.clear()


@dp.message(Command("build_cont"))
async def bot_build_cont(message: types.message, state: FSMContext):
    await message.answer("Введите имя или id image:")
    await state.set_state(DockerStates.build_cont)
@dp.message(DockerStates.build_cont)
async def build_cont(message: types.message, state: FSMContext):
    image = message.text
    f = run_cont_by_image(client, image)
    await message.answer(f)
    await state.clear()


@dp.message(Command("restart_cont"))
async def bot_restart_cont(message: types.message, state: FSMContext):
    await message.answer("Введите имя или id контейнера:")
    await state.set_state(DockerStates.restart_cont)
@dp.message(DockerStates.restart_cont)
async def restart_cont(message: types.message, state: FSMContext):
    id_or_name = message.text
    f = restart_cont_by_id_or_name(client, id_or_name)
    await message.answer(f)
    await state.clear()


@dp.message(Command("stop_cont"))
async def bot_stop_cont(message: types.message, state: FSMContext):
    await message.answer("Введите имя или id контейнера:")
    await state.set_state(DockerStates.stop_cont)
@dp.message(DockerStates.stop_cont)
async def stop_cont(message: types.message, state: FSMContext):
    id_or_name = message.text
    f = stop_cont_by_id_or_name(client, id_or_name)
    await message.answer(f)
    await state.clear()



@dp.message(Command("remote_cont"))
async def bot_remove_cont(message: types.message, state: FSMContext):
    await message.answer("Введите имя или id контейнера:")
    await state.set_state(DockerStates.remote_cont)
@dp.message(DockerStates.remote_cont)
async def remove_cont(message: types.message, state: FSMContext):
    id_or_name = message.text
    f = remove_cont_by_id_or_name(client, id_or_name)
    await message.answer(f)
    await state.clear()



if __name__ == '__main__':
    asyncio.run(main())




