from common.AbstractMarket import AbstractMarket
from quoine.exceptions import QuoineAPIException, QuoineRequestException
from quoine.client import Quoinex as qx

# NEED python-quoine

class Quoinex(AbstractMarket):
    market_code = 'Quoinex'
    # product ID = 5 BTCJPY
    BTC_JPY_PROD_ID = 5
    # 'funding_currency': 'JPY'

    def __init__(self):
        super().__init__()
        self.client =qx(0,'Not needed to get prices')

    def is_market_open(self):
        pass

    def get_price(self, prices):
        product = []
        try:
            product = self.client.get_product(Quoinex.BTC_JPY_PROD_ID)
        except (QuoineRequestException, QuoineAPIException) as e:
            self.raise_exception("Quoinex failed to get prices", e)

        prices[self.market_code] = {'ask': float(product['market_ask']), 'bid': float(product['market_bid'])}
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
