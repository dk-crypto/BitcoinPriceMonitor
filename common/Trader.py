import csv
import datetime
import threading
import queue
import logging
from market.GmoCoin import GmoCoin
from market.Quoinex import Quoinex
from market.BitFlyer import BitFlyer


class Trader:
    PRICE_DIFF_FILE_NAME = '../data/priceDiff_{date}.csv'

    OPEN_ORDER_SLEEP_SEC = 3
    OPEN_ORDER_WAIT_THRESHOLD = 40  # 2 mins
    QUERY_SLEEP_SEC = 1.5

    def __init__(self):
        self.markets = {Quoinex.market_code: Quoinex(),
                        GmoCoin.market_code: GmoCoin(),
                        BitFlyer.market_code: BitFlyer()}

    # Gets prices from each markets
    # return {market_code:{'ask':100,'bid':100},...}
    def get_market_prices(self):
        threads = []
        prices = {}
        for market in self.markets.values():
            thread = threading.Thread(target=market.get_price, args=(prices,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        self.raise_exception_from_queue()
        return prices

    def clear_exception_queue(self):
        for market in self.markets.values():
            market.exec_queue = queue.Queue()

    def raise_exception_from_queue(self):
        for market in self.markets.values():
            if not market.exec_queue.empty():
                e = market.exec_queue.get(block=False)
                raise e

    # Gets price differences in case of open trades
    # Returns ((market_code, max_bid), (market_code, min_ask))
    def price_diff_open(self, prices):
        asks = {}
        bids = {}
        for code, price in prices.items():
            asks[code] = price['ask']
            bids[code] = price['bid']

        min_ask = min(asks.items(), key=lambda x: x[1])
        max_bid = max(bids.items(), key=lambda x: x[1])
        return (max_bid, min_ask)

    # Gets price differences to close positions
    # Returns float diff. smaller value is better
    def price_diff_close(self, prices, open_short_market, open_long_market):
        diff = prices[open_short_market]['ask'] - prices[open_long_market]['bid']
        return diff

    def write_market_price(self, prices):
        file_name = Trader.PRICE_DIFF_FILE_NAME.format(date=datetime.date.today())
        f = open(file_name, 'a')
        writer = csv.writer(f, lineterminator='\n')
        sorted_prices = sorted(prices.items(),
                     key=lambda x: x[1]['ask'])
        row = [datetime.datetime.today()]
        for items in sorted_prices:
            row.append(items[0])
            row.append(items[1]['bid'])
            row.append(items[1]['ask'])
            logging.info(items)
        writer.writerow(row)
        f.close()
