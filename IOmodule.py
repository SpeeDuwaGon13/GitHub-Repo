from .. import loader, utils
from telethon import events


def register(cb):
    cb(IoMod())

class IoMod(loader.Module):
    """19.09.2021 я буду в сильном восторге, если у меня всё получится"""
    strings = {'name': 'IO'}
