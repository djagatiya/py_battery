import psutil
from plyer import notification
import logging
import time

from collections import namedtuple

def set_logger():

    today_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("{0}/{1}.log".format("logs", today_date))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

def battery_check(args_sleep_time=-1):

    with open("config.json") as _file:
        conf = eval(_file.read())
    
    logging.info(f"Configuration:{conf}")

    max_level, min_level, sleep_time = conf['max_level'], conf['min_level'], conf['sleep_time']
    if args_sleep_time != -1: sleep_time = args_sleep_time

    timestamp = time.time()
    datetime = time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    
    battery = psutil.sensors_battery()
    logging.info(f'battery={battery}')

    percent = int(battery.percent)
    power_plugged = battery.power_plugged

    message = None
    if percent >= max_level and power_plugged:
        message = "[High] Please unplug charger"
    elif percent < min_level and not power_plugged:
        message = "[Low] Plug the charger"

    if message is not None:
        logging.info(f"Going to alert : {message}")
        notification.notify(
            title="Battery Percentage",
            message=f"{message} : {percent}%",
            timeout=10
        )

    time.sleep(sleep_time)