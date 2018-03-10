import pytest
from urllib.request import urlopen


def test_price_get_code_200():
    url = 'http://127.0.0.1:8000/api/v1/prices'
    get_code = urlopen(url).getcode()
    assert 200 == get_code


def test_price_list():
    pass
