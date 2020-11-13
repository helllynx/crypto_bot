import dataclasses
import json
from dataclasses import dataclass

from binance.client import Client


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


@dataclass
class Tick:
    symbol: str
    priceChange: str
    priceChangePercent: str
    weightedAvgPrice: str
    prevClosePrice: str
    lastPrice: str
    lastQty: str
    bidPrice: str
    bidQty: str
    askPrice: str
    askQty: str
    openPrice: str
    highPrice: str
    lowPrice: str
    volume: str
    quoteVolume: str
    openTime: int
    closeTime: int
    firstId: int
    lastId: int
    count: int


class Binance:

    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)

    def get_tick(self, symbol: str) -> Tick:
        return Tick(**self.client.get_ticker(symbol=symbol))
