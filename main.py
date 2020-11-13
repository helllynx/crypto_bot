from core.binance import Binance

import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

api_key = config["Binance"]["api_key"]
secret = config["Binance"]["secret"]

binance = Binance(api_key, secret)

tick = binance.get_tick("ETHBUSD")

print(tick)

