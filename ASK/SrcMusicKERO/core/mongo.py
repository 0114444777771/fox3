from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
import logging

# إعداد logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

# استخدام logging بدلاً من LOGGER
logging.getLogger("ميوزك اليــكس").info("جـارِ الاتصـال بقاعـدة البيانـات . . .")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.myDatabase
    logging.getLogger("ميوزك اليــكس").info("تم الاتصـال بقاعـدة البيانـات ...✓")
except:
    logging.getLogger("ميوزك اليــكس").error("حدث خطأ اثناء الاتصال بقاعدة البيانات.")
    exit()
