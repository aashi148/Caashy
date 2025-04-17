import requests

def get_exchange_rates(base='USD'):
    url = f'https://api.exchangerate-api.com/v4/latest/{base}'
    response = requests.get(url)
    return response.json()

def get_crypto_price(coin='bitcoin'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
    response = requests.get(url)
    return response.json()[coin]['usd']

def get_financial_quote():
    url = "https://api.quotable.io/random?tags=finance"
    response = requests.get(url)
    return response.json()['content']
