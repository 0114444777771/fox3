import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.StreamHandler(),  # إزالة FileHandler مؤقتًا
    ],
)

LOGGER = logging.getLogger("TestLogger")
LOGGER.info("اختبار التسجيل بدون ملف")
