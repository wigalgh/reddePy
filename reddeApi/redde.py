import requests
import json
import sys
import random


class ReddeApi:
    receive_url = "https://api.reddeonline.com/v1/receive"
    cashout_url = "https://api.reddeonline.com/v1/cashout"


    def __init__(self, api_key, app_id):
        self.apikey = api_key
        self.appid = app_id


    """Generate a  number of fixed length """
    def clientReferenceNumber(self, stringLength=6):
        numbers = "0123456789"
        return ''.join(random.choice(numbers) for i in range(stringLength))


    """Generate a random alpha numeric of fixed length """
    def randomClientID(self, stringLength=6):
        alphaNumeric = "0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
        return ''.join(random.choice(alphaNumeric) for i in range(stringLength))


    def api_request(self, headers, url, params, http_call='post'):

            if http_call == 'post':
                try:
                    response = requests.post(
                        url, json=params, headers=headers, timeout=3)
                    response.raise_for_status()
                except requests.exceptions.HTTPError as httpErr:
                    print("Http Error:", httpErr)
                except requests.exceptions.ConnectionError as connErr:
                    print("Error Connecting:", connErr)
                except requests.exceptions.Timeout as timeOutErr:
                    print("Timeout Error:", timeOutErr)
                except requests.exceptions.RequestException as reqErr:
                    print("Something Else:", reqErr)
                    sys.exit(1)

            else:
                raise ValueError('Invalid http_call parameter')
            try:
                result = response.json()
            except ValueError:
                result = {'error': 'No JSON content returned'}
            if response.status_code != 200 or 'error' in result:
                print("Check this error", response.status_code)
            else:
                return result


    def sendMoney(self, amount, walletnumber, client_ref, client_id, network):
        headers = {
             'Content-Type': "application/json;charset=UTF-8",
             'ApiKey': self.apikey
        }
        payload = {
            'amount': amount,
            'appid': self.appid,
            'clientreference': client_ref,
            'clienttransid': client_id,
            'description': 'Registered Member',
            'nickname': 'wigal',
            'paymentoption': network,
            'vouchercode': '',
            'walletnumber': walletnumber
        }

        data = self.api_request(headers, self.cashout_url, payload, 'post')
        return data


    def receiveMoney(self, amount, walletnumber, client_ref, client_id, network):
        headers = {
             'Content-Type': "application/json;charset=UTF-8",
             'ApiKey': self.apikey
        }

        payload = {
            'amount': amount,
            'appid': self.appid,
            'clientreference': client_ref,
            'clienttransid': client_id,
            'description': 'Registered Member',
            'nickname': 'wigal',
            'paymentoption': network,
            'vouchercode': '',
            'walletnumber': walletnumber
        }
        
        data = self.api_request(headers, self.receive_url, payload, 'post')
        return data