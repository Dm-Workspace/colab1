# conftest.py
import os
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="Базовый URL тестируемого сайта"
    )

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    """
    Сначала берём CLI-опцию --base-url,
    иначе — переменную окружения BASE_URL,
    иначе — дефолт https://nsp.com.ua
    """
    return (
        pytestconfig.getoption("base_url")
        or os.getenv("BASE_URL")
        or "https://nsp.com.ua"
    )
