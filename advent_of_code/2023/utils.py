import argparse

import requests


URL = 'https://adventofcode.com/2023/day/{day}/input'


def cookie_arg() -> str:
    parser = argparse.ArgumentParser(description="Get Cookie...")
    parser.add_argument(
        '--cookie', '-c', type=str, required=True,
        help='Cookie to actually get the input...To get the cookie inspect the page->application->storage->cookies->session.'
    )
    args = parser.parse_args()
    return args.cookie


def get_challenge_input(day) -> str:
    cookie = cookie_arg()

    url = URL.format(day=day)
    cookies = {'session': cookie}
    response = requests.get(url, cookies=cookies)
    return response.text
