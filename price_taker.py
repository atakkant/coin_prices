import asyncio
import aiohttp
from constants import *

apis = APIS

endpoints = ENDPOINTS

coins = COINS_LOWERCASE

endpoint = 'all_prices'

async def url_setter(api,endpoint):
    url = api + endpoint
    return url


async def coin_price_taker(session,url):
    coin_list = []
    async with session.get(url) as resp:
        results = await resp.json()
        if isinstance(results,dict) and results.get('data'): #check kucoin response
            pairs = results.get('data').get('ticker')
        elif isinstance(results,list): #binance response for now
            pairs = results

        for pair in pairs:
            symbol = pair.get('symbol').lower().replace('-','')
            if symbol in coins:
                coin_pair = {}
                coin_pair['symbol'] = symbol
                if '-' in pair.get('symbol'): #kucoin
                    coin_pair['exchange'] = 'kucoin'
                    coin_pair['price'] = pair.get('last')
                else:
                    coin_pair['exchange'] = 'binance'
                    coin_pair['price'] = pair.get('price')

                coin_list.append(coin_pair)
    return coin_list


async def take_prices():
    coins = COINS_LOWERCASE
    async with aiohttp.ClientSession() as session:
        loop = asyncio.get_event_loop()
        tasks = []
        for key,value in apis.items():
            url = await url_setter(value,endpoints.get(key).get(endpoint))
            print("Sending request to %s to get the values"%key.capitalize())
            tasks.append(asyncio.ensure_future(coin_price_taker(session,url)))

        all_coins = await asyncio.gather(*tasks)

    return all_coins
