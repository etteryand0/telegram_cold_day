import sys
import time
import datetime

from bot import Bot
from logger import Logging
from parsing import parse

# set logging
log = Logging()
log.sys()


# read dotenv variables
try:
    with open('.env', 'r') as handler:
        lines = [ i.strip() for i in handler.readlines() ]
except FileNotFoundError as e:
    log.tell(str(e))
    sys.exit()

env = dict()
for line in lines:
    items = line.split('=')
    env |= dict([items])

log.tell('Succesfuly read .env file')


# init telegram bot
try:
    bot = Bot(env['TELEGRAM_BOT_TOKEN'],
              env['TELEGRAM_ADMIN_ID'],
              env['TELEGRAM_CHAT_ID'])
except KeyError as e:
    log.tell('.env KeyError: ' + str(e))
    sys.exit()


del log

# main bot loop
while True:
    log = Logging()

    # get weather
    for _ in range(5):
        meta, weather = parse()

        if meta:
            break

        log.tell(str(weather))

        admin_debug = bot.debug_error(str(weather))
        if admin_debug != 200:
            log.tell('Can`t administer admin. ' + str(admin_debug))

        time.sleep(10)
        log.tell('Trying to bypass error. Sleep for 10 seconds')
    else:
        log.tell('Aborting due to ugms14.ru network issues')
        sys.exit()

    # check if information was updated at 6 am
    hour = meta.split(' в ')[1].split(' час')[0].strip()
    if hour == '03' or hour == '3':
        log.tell('Information hadn`t updated yet. Current info hour is ' + hour)
        
        del log
        time.sleep(60*5)

        continue
    else:
        log.tell('Information updated! Current info hour is ' + hour)
    
    text = str()

    weather[1] = 'Температура: ' + weather[1]
    weather[2] = 'Ветер: ' + weather[2]

    if int( weather[1].split(': ')[1][:-1] ) <= -48:
        text += '*СПАТЬ!*\n'
        weather[1] = f'`{weather[1]}`'
        weather[2] = f'_{weather[2]}_'

    text += '{}\n{}. {}, {}'.format(
                meta, 
                weather[0], 
                weather[1], 
                weather[2])

    
    # send message to channel
    for _ in range(5):
        traceback = bot.send_msg(text)
        # TODO: other request verification
        if str(traceback) == '200':
            log.tell(f'Succesfuly sent weather information to channel "{bot.chat_id[0]}"')
            break
        
        log.tell('Something went wrong. ' + str(traceback))
        bot.debug_error(str(traceback))

        time.sleep(10)
    else:
        log.tell('Aborting due to api network issues')
        sys.exit()


    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    tomorrow = tomorrow.replace(hour=6, minute=15, second=0, microsecond=0)

    timedelta = tomorrow - now
    
    sleep = int(timedelta.total_seconds())

    if sleep > 86400:
        tomorrow = now
        tomorrow = tomorrow.replace(hour=6, minute=15, second=0, microsecond=0)

        timedelta = tomorrow - now
        sleep = int(timedelta.total_seconds())
    
    log.tell('Sleep for '+str(timedelta))
    
    del log
    time.sleep(sleep)
