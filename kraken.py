import time
import requests
import urllib.parse
import hashlib
import hmac
import base64
import json

currency_symbol = {
    "EUR" : "€",
    "USD" : "$"
}

def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

def exec(msg, user, predicted_cmd):

    cfg = user.get_module_config("kraken-module")
    command = predicted_cmd.split("-")
    api_key = cfg['api_key']
    api_sec = cfg['api_sec']
    your_currency = cfg['currency']

    status = requests.get('https://api.kraken.com/0/public/SystemStatus').json()

    print(msg)
    print(command)

    if status['result']['status'] == "online":
        if command[0] == "user":
             # Construct the request and print the result
            resp = kraken_request('https://api.kraken.com/0/private/TradeBalance',
            {"nonce": str(int(1000*time.time())),
            "asset": your_currency},
            api_key, api_sec).json()
            return {"cod": 200, "msg": f"Deine Kraken Balance ist {float(resp['result']['eb']):.2f}{currency_symbol[your_currency]}"}
        elif command[0] == "market":
            resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair=XBT{your_currency}').json()
            return {"cod": 200, "msg": f"Es ist zur Zeit {float(resp['result'][f'XXBTZ{your_currency}']['o']):.2f}{currency_symbol[your_currency]} wert"}
        else:
            return {"cod": 500, "msg": "Unbekannter Command"}
    else:
        return {"cod": 404, "msg": "Kraken Api is not online"}