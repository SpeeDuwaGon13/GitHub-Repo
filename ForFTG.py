from .. import loader, utils
from telethon import events


def register(cb):
    cb(ProstoPrivetMod())

class ProstoPrivetMod(loader.Modue):
    """тестовый модуль"""
    strings = {'name': 'FirstPosition'}

    async def vsaycmd(self, message):
        """Используй .vsay <аргумент> (abme, ths)"""
        text = utils.get_args_raw(message)

        if not text:
            await message.edit("<b>вы забыли вписать аргумент</b>")
            return

        await message.edit("<b>Одно мгновение...</b>")

        if text == "abme":
            await message.edit("<b>Я начинающий создатель модулей</b>")
            return

        if text == "ths":
            await message.edit("<b>Это мой первый тестовый модуль :D</b>")
            return
