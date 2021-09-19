from .. import loader, utils
from telethon import events


def register(cb):
    cb(ProstoPrivetMod())

class ProstoPrivetMod(loader.Module):
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

        elif text == "ths":
            await message.edit("<b>Это мой первый тестовый модуль :D</b>")
            return

        else:
            await message.edit("<b>Не существует такого аргумента. Черть</b>")
