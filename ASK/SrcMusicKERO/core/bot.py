from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from logging import LOGGER


class Zelzaly(Client):
    def __init__(self):
        LOGGER("ميوزك الــيكـس").info(f"جارِ بدء تشغيل البوت . . .")
        super().__init__(
            name="SrcMusicKERO",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        # طباعة معلومات البوت
        print("✅ تم تشغيل البوت بنجاح!")
        print(f"🆔 معرف البوت: {self.me.id}")
        print(f"👤 اسم البوت: {self.me.first_name} {self.me.last_name or ''}")
        print(f"📛 يوزر البوت: @{self.me.username}")

        # طباعة قيمة LOGGER_ID
        print(f"📌 معرف مجموعة السجلات: {config.LOGGER_ID}")

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» تم تشغيل الميـوزك لـ البوت {self.me.mention} :</b><u>\n\n"
                     f"- ɪᴅ : <code>{self.me.id}</code>\n"
                     f"- ɴᴀᴍᴇ : {self.me.first_name} {self.me.last_name or ''}\n"
                     f"- ᴜsᴇʀɴᴀᴍᴇ : @{self.me.username}",
            )
            print("✅ تم إرسال رسالة إلى مجموعة السجلات بنجاح!")
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            print("❌ خطأ: تأكد من إضافة البوت كمشرف في مجموعة السجلات.")
            LOGGER(__name__).error("» قم باضافة البـوت مشـرفـاً بكافة الصلاحيات في مجموعـة السجـل")
            exit()
        except Exception as ex:
            print(f"❌ خطأ غير متوقع: {type(ex).__name__} - {ex}")
            LOGGER(__name__).error(f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}.")
            exit()

        try:
            a = await self.get_chat_member(config.LOGGER_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                print("❌ البوت ليس مشرفًا في مجموعة السجلات!")
                LOGGER(__name__).error("» قم برفـع البـوت مشـرفـاً بكافة الصلاحيات في مجموعـة السجـل")
                exit()
            print("✅ البوت لديه صلاحيات المشرف في مجموعة السجلات!")
        except Exception as ex:
            print(f"❌ خطأ عند التحقق من صلاحيات البوت: {type(ex).__name__} - {ex}")
            exit()

        LOGGER("ميوزك اليــكس").info(f"تم بدء تشغيل البوت {self.name} ...✓")

    async def stop(self):
        await super().stop()
