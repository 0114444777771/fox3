import logging
from pyrogram import Client
import config

# إعداد الـ logger
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("مـيـوزك اليــكس")

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        # إنشاء العملاء المساعدين
        self.clients = [
            Client(name=f"MatrixAss{i+1}",
                   api_id=config.API_ID,
                   api_hash=config.API_HASH,
                   session_string=str(getattr(config, f"STRING{i+1}")),
                   no_updates=True)
            for i in range(5)
        ]

    async def start(self):
        LOGGER.info("جـار تـشـغـيـل الـحـسـاب الـمـسـاعـد")

        for i, client in enumerate(self.clients, 1):
            if getattr(config, f"STRING{i}", None):
                await self._start_client(client, i)

    async def _start_client(self, client, index):
        try:
            await client.start()
            try:
                await client.join_chat("DE_FK")
                await client.join_chat("A_l_e_3_x")
                await client.join_chat("F_b_i_u")
            except:
                pass

            assistants.append(index)
            await client.send_message(config.LOGGER_ID, f"» تم تشغيـل الحسـاب المسـاعـد {index} .. بنجـاح ✅")
            setattr(client, "id", client.me.id)
            setattr(client, "name", client.me.mention)
            setattr(client, "username", client.me.username)
            assistantids.append(client.id)
            LOGGER.info(f"تم بدء تشغيل الحساب المساعد {client.name} ...✓")
        except Exception as e:
            LOGGER.error(f"حـدث خـطـاء اثـنـاء تـشـغـيـل الـحـسـاب الـمـسـاعـد {index}: {str(e)}")

    async def stop(self):
        LOGGER.info("جـار ايـقـاف الـحـسـاب الـمـسـاعـد...⁦♡")
        for client in self.clients:
            try:
                await client.stop()
            except Exception as e:
                LOGGER.error(f"فشل إيقاف الحساب: {str(e)}")
