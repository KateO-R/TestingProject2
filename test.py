import pytest
import requests

from main import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/abcd1234.jpg'}
    ]

    cat_image_url = get_random_cat_image()
    assert cat_image_url == 'https://cdn2.thecatapi.com/images/abcd1234.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    cat_image_url = get_random_cat_image()
    assert cat_image_url is None



