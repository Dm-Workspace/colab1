# test_nsp_api.py
import pytest
import requests

def test_homepage_status(base_url):
    """
    Проверяем, что главная страница возвращает 200 OK
    """
    resp = requests.get(base_url)
    assert resp.status_code == 200

def test_homepage_contains_keyword(base_url):
    """
    Проверяем, что на главной странице есть упоминание 'Sunshine'
    """
    resp = requests.get(base_url)
    assert "Sunshine" in resp.text
