import sys
from typing import List, Tuple

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_seen = sys.maxsize
    profit = 0
    for price in prices:
        profit_sell_today = price - min_price_seen
        profit = max(profit_sell_today, profit)
        min_price_seen = min(min_price_seen, price)

    return profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
