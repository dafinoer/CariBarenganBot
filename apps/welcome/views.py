import logging
import pendulum

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

logger = logging.getLogger(__name__)


class Welcome:

    @staticmethod
    def start(bot, update):

        username_data = update.message.from_user.username

        now = pendulum.now('Asia/Jakarta')

        greating = ''

        logger.debug('time {}'.format(now))

        print(type(now.hour))

        if now.hour > 4 and now.hour <= 10:
            greating = 'Selamat Pagi'
        elif now.hour > 10 and now.hour <= 14:
            greating = 'Selamat Siang'
        elif now.hour > 14 and now.hour <= 18:
            greating = 'Selamat Sore'
        else:
            greating = 'Selamat Malam'

        bot.send_message(chat_id=update.message.chat_id, text="Hi {} dan {}, ini adalah bot share cost "
                         .format(update.message.from_user.username, greating))
