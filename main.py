import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()

def shorten_link(token, url):
    endpoint = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url': url,
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(url, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'unit': 'month',
        'units': -1,
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    verification_bitlink_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(verification_bitlink_url, headers=headers)
    return response.ok


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Ваша ссылка')
    args = parser.parse_args()

    token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(args.url, token):
            print(count_clicks(args.url, token))
        else:
            print(shorten_link(token, args.url))
    except requests.exceptions.HTTPError as error:
        print(error)
