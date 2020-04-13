import os
import schedule
import time

from dotenv import load_dotenv
from app import create_app

load_dotenv()

config_name = os.getenv('CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    from app.helpers.fetchnewnews import fetch_new_news
    schedule.every(6).hours.do(fetch_new_news)
    app.run()
    while True:
        schedule.run_pending()
        time.sleep(1)