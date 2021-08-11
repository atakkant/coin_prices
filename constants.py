#list of top ten top ten coins

COINS = ['BTCUSDT','ETHUSDT','BNBUSDT','ADAUSDT','XRPUSDT','DOGECOINUSDT','DOTUSDT','UNIUSDT','BCHUSDT','LINKUSDT','XTZUSDT','ATOMUSDT']

COINS_LOWERCASE = [coin.lower() for coin in COINS]

APIS = {
    'binance':'https://api1.binance.com',
    'kucoin': 'https://api.kucoin.com'
    }


ENDPOINTS = {
    'binance': {
        'exchange_info':'/api/v3/exchangeInfo',#get all pairs
        'all_prices':'/api/v3/ticker/price', #get all pairs
        },
    'kucoin': {
        'exchange_info':'/api/v1/symbols',#get all pairs
        'all_prices':'/api/v1/market/allTickers', #get all pairs
        }
    }
