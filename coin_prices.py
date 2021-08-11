import pandas as pd
import numpy as np
import price_taker
import asyncio
from constants import *
import time

async def list_values():
    all_coins = await price_taker.take_prices()
    return all_coins

async def main():
    result = await list_values()
    data = {}
    for res in result:
        for r in res:
            exchange = r.get('exchange')
            symbol = r.get('symbol')
            price = format(float(r.get('price')),'.2f')
            nice_pair = {symbol:price}
            if data.get(exchange):
                data[exchange].update(nice_pair)
            else:
                data[exchange] = nice_pair

    index = COINS_LOWERCASE

    s = pd.DataFrame(data)
    print(s)

if __name__ == "__main__":
    asyncio.run(main())
