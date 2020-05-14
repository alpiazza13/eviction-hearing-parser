from bs4 import BeautifulSoup
import pytest

import hearing

@pytest.fixture(scope="function")
def soup():
    filepath = hearing.get_test_html_path()
    with open(filepath) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup