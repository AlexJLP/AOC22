import requests
import browser_cookie3

def get_input(day=1):
    cj = browser_cookie3.firefox()
    r = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies=cj)
    assert r.ok
    return r.text[:-1]  # single trailing newline for some reason, just delete it
