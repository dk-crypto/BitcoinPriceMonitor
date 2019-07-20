class GetException(Exception):
    pass


class OpenTradeException(Exception):
    pass


class CloseTradeException(Exception):
    pass


class OrderTimeoutException(Exception):
    pass


class PositionMissingExternal(Exception):
    def __init__(self, missing_external_positions):
        self.missing_external_positions = missing_external_positions


class PositionMissingInternal(Exception):
    def __init__(self, missing_internal_positions, t=None, obj=None):
        self.missing_internal_positions = missing_internal_positions
