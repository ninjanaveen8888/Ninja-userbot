"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
INDIANBOT_IS_ALIVE = ("**Ninja Naveen's Userbot** \nBOT Status : ` **`Pro Like Ninja Naveen**\n\n"
                     f"`My Pro owner`: {DEFAULTUSER}\n\n"
                     "`Bot Version:` [1.0](NinjaHackers.tk)\n`Python:` **3.7.4**\n"
                     "`Database Status:` **ALL OK**\n\n`Ninja Naveen's Pro Userbot\n`"
                     "**Bot Creator:** [🇮🇳INDIAN BHAI](t.me/pureindialover)\n"
                     "**Co-Owner:** [🇮🇳AKASH](t.me/AKASH_AM1)\n\n"
                     "**Modified By:** [Ninja Naveen](t.me/ninjanaveen)\n\n"
                     "     [🇮🇳Deploy This Bot](https://github.com/ninjanaveen/IndianBot)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, INDIANBOT_IS_ALIVE) 
