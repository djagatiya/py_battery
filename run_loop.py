from battery import set_logger, battery_check
import logging

set_logger()

logging.info("========== Starting ============")

while True:
    battery_check()
