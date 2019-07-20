import logging
import time
import logging.config

from common.Trader import Trader
logging.config.fileConfig("logging.conf")

trader = Trader()

while(True):
    try:
        prices = trader.get_market_prices()
        trader.write_market_price(prices)
        time.sleep(5)
    except Exception as e:
        logging.error(e)
        time.sleep(10)
