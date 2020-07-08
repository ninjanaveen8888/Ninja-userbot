"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/27932853966c10bede626.png"
INDIANBOT_IS_ALIVE = ("**Ninja Naveen's Userbot** \nBOT Status : `Pro Like Ninja Naveen`\n\n"
                     f"`My Pro owner`: {DEFAULTUSER}\n\n"
                     "**NinjaBot Version** : `3.14`\n"
                     "`Database Status:` **ALL OK**\n\n`Ninja Naveen's Pro Userbot\n`"
                     "**Database** : `All Set and are Working Flawlessly!`\n\n"
                     "**Join the Bot Creator's Channel** : [💠Royal Giveaways💠](t.me/royal_giveaway)\n\n"
                     "**USERBOT By** [🔥Ninja Naveen🔥](t.me/NinjaNaveen)\n\n"
                     "[Deploy Ninja Bot](https://heroku.com/deploy?template=https://github.com/ninjanaveen/fridayuserbot)" 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, INDIANBOT_IS_ALIVE) 
