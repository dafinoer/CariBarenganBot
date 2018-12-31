import logging
import os
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv

from apps.welcome.views import Welcome

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

load_dotenv(verbose=True)

from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)


def main():

    updater = Updater(os.getenv("TOKEN"))

    dispatcher = updater.dispatcher

    # /start - welcome set
    start_handler = CommandHandler('start', Welcome.start)
    dispatcher.add_handler(start_handler)

    #updater.start_polling()

    updater.start_webhook(listen='0.0.0.0',
                      port=8443,
                      url_path='TOKEN',
                      key='private.key',
                      cert='cert.pem',
                      webhook_url='https://example.com:8443/TOKEN')

    updater.idle()

    updater.stop()

if __name__ =='__main__':
    main()




