
import queue
from abc import ABCMeta, abstractmethod
from exception.TradeException import *
import logging

class AbstractMarket(metaclass=ABCMeta):

    def __init__(self):
        self.error_count = 0
        self.error_threshold = 3
        self.exec_queue = queue.Queue()

    def is_open_available(self):
        if self.error_count > self.error_threshold:
            logging.fatal("Reached Error Threshold !! Exiting..")
            exit(0)
        return True

    def is_close_available(self):
        if self.error_count > self.error_threshold:
            logging.fatal("Reached Error Threshold !! Exiting..")
            exit(0)
        return True

    def raise_exception(self, message, exception=None):
        if not exception is None:
            logging.error(exception)
        self.exec_queue.put(GetException(message))
        raise GetException(message)

    def raise_failed_open_exception(self, message, exception=None):
        if not exception is None:
            logging.error(exception)
        self.error_count = self.error_count + 1
        self.exec_queue.put(OpenTradeException(message))
        raise OpenTradeException(message)

    def raise_failed_close_exception(self, message, exception=None):
        if not exception is None:
            logging.error(exception)
        self.error_count = self.error_count + 1
        self.exec_queue.put(CloseTradeException(message))
        raise CloseTradeException(message)

    @abstractmethod
    def is_market_open(self):
        pass

    @abstractmethod
    # prices = {market_code:{'ask':100,'bid':100},...}
    def get_price(self, prices):
        pass

    @abstractmethod
    #  market_positions =
    #  {'GmoCoin': {'cash':1000, 'long': {'total': 0.0052, 'position_ids': [[12345]], 'positions': {12345:0.01}}, 'short': {'total': 0.01, 'position_ids': [12909313]}}}
    def get_positions(self, market_positions):
        pass

    @abstractmethod
    def open_short(self, bid_price, amount):
        pass

    @abstractmethod
    def open_long(self, ask_price, amount):
        pass

    @abstractmethod
    def check_open_order(self):
        pass

    @abstractmethod
    def close_short(self, ask_price, position_ids, amount):
        pass

    @abstractmethod
    def close_long(self, bit_price, position_ids, amount):
        pass

    @abstractmethod
    def cancel_order(self, order_id):
        pass

    @abstractmethod
    def get_max_position_amount(self):
        pass

