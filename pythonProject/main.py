import asyncio

import docker
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.handlers import message
from aiogram.types import BotCommand
from docker_fun import get_all_cont


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
            BotCommand(command="/start_cont_by_id", description="ad"),
            BotCommand(command="/restart_cont_by_id", description="vds"),
            BotCommand(command="/stop_cont_by_id", description="sdvs"),
            BotCommand(command="/remote_cont_by_id", description="efs"),
            BotCommand(command="/create_image_by_df", description="fewsd"),
            BotCommand(command="/get_all_images", description="sefew")
        ]
    )
    await dp.start_polling(bot)


@dp.message(Command("get_all_container"))
async def bot_get_all_cont(message: types.message):
    list_cont = get_all_cont(client)
    names = ''
    print(type(list_cont[0]))
    # for cont in list_cont:
    #     print(type(cont))
    #     names += cont.name + '  \n'

    await message.answer("hi")




if __name__ == '__main__':
    asyncio.run(main())




