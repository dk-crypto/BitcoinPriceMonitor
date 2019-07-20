from common.AbstractMarket import AbstractMarket
import logging
import requests

class GmoCoin(AbstractMarket):
    market_code = 'GmoCoin'
    end_public = 'https://api.coin.z.com/public'

    def __init__(self):
        super().__init__()

    def is_market_open(self):
        return True

    def get_price(self, prices):
        path = '/v1/ticker?symbol=BTC'
        response = requests.get(GmoCoin.end_public + path).json()
        if not response['status'] == 0:
            logging.error(response)
            self.raise_exception('failed to get prices')
        prices[self.market_code] = {'ask': float(response['data'][0]['ask']), 'bid': float(response['data'][0]['bid'])}
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

