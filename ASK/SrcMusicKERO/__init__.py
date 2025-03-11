import logging
from SrcMusicKERO.core.bot import Zelzaly
from SrcMusicKERO.core.dir import dirr
from SrcMusicKERO.core.userbot import Userbot
from SrcMusicKERO.misc import dbb, heroku

# إعداد الـ Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger("ميوزك اليــكس")

# إعداد الكود
LOGGER.info("جارِ إعداد المكونات...")

dirr()
dbb()
heroku()

# بدء التشغيل
app = Zelzaly()
userbot = Userbot()

LOGGER.info("تم تحميل المكونات بنجاح.")

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

LOGGER.info("تم تهيئة الـ APIs بنجاح.")
