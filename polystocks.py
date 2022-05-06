#!/usr/bin/env python3

from yahoo_fin import stock_info as si
import argparse

class PolyStocks():
    def __init__(self):
        self.symbols = ['TSLA', 'BITF', 'AAPL', 'AMD']
        self.round_to = 2
        
    def watch_list(self):
        result = '| '
        for symbol in self.symbols:
            try:
                data = str(round(si.get_live_price(symbol), self.round_to))
                result += f'{symbol} - ${data} | '
            except:
                result += f'{symbol} - $0.00 | '
        print(result)
        return result

    def biggest_gainer(self):
        gainers = si.get_day_gainers()
        result = str(gainers.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(gainers.at[0, 'Symbol']), self.round_to))
        return result


    def biggest_loser(self):
        losers = si.get_day_losers()
        result = str(losers.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(losers.at[0, 'Symbol']), self.round_to))
        return result


polystocks = PolyStocks()
polystocks.watch_list()
