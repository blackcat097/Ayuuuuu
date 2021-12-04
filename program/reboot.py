from O import SUDO_USERS

from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

if UstaD:
    @UstaD.on(events.NewMessage(pattern="/restart"))
    async def restart(e):
        if e.sender_id in SMEX_USERS:
             text = "⭐𝐑𝐄𝐁𝐎𝐎𝐓𝐄𝐃⭐\n🔰𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐓𝐈𝐋𝐋 𝐈𝐓 𝐑𝐄𝐁𝐎𝐎𝐓𝐒...."
             await e.reply(text, parse_mode=None, link_preview=None)
             try:
                await UstaD.disconnect()
             except Exception:
                pass
             os.execl(sys.executable, sys.executable, *sys.argv)
             quit()
