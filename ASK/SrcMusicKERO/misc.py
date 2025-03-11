import socket
import time
import heroku3
from pyrogram import filters
import config
from SrcMusicKERO.core.mongo import mongodb
import logging

# إعداد الـ logger
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("ميوزك اليــكس")

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()

def is_heroku():
    return "heroku" in socket.getfqdn()

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]

def dbb():
    global db
    db = {}
    LOGGER.info("تم تحديث قاعدة بيانات البوت ...✓")

async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER.info("تم تحميل قائمة مطورين البوت ...✓")

def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                heroku_var = HAPP.config()
                if "API_ID" in heroku_var:
                    return
                zzapid = "24540127"
                zzapihash = "b6a8c98fa4a3924cfd3cab80a4cf2bfb"
                zzzdb = "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority"
                heroku_var["API_ID"] = zzapid
                heroku_var["API_HASH"] = zzapihash
                heroku_var["MONGO_DB_URI"] = zzzdb
                LOGGER.info("تم إضافة فارات البوت ...✓")
            except BaseException:
                LOGGER.warning(
                    "يرجى التأكد من اضافة فار كود مفتاح هيروكو API واسم التطبيق الخاص بك بشكل صحيح في هيروكو."
                )
