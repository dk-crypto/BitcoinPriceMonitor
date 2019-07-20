from common.AbstractMarket import AbstractMarket
import logging
import requests

class BitFlyer(AbstractMarket):
    market_code = 'BitFlyer'
    end_public = 'https://api.bitflyer.com/v1/'

    def __init__(self):
        super().__init__()

    def is_market_open(self):
        return True

    def get_price(self, prices):
        path = 'board'
        response = requests.get(BitFlyer.end_public + path).json()
        prices[self.market_code] = {'ask': float(response['asks'][0]['price']), 'bid': float(response['bids'][0]['price'])}
        return prices

    def get_positions(self, market_positions):
        pass

    def open_short(self, bid_price, amount):
        pass

    def open_long(self, ask_price, amount):
        pass

    def check_open_order(self):
        pass

    def close_short(self, ask_price, position_ids, amount):
        pass

    def close_long(self, bit_price, position_ids, amount):
        pass

    def cancel_order(self, order_id):
        pass

    def get_max_position_amount(self):
        pass


