import os

import pytest

from tidal_downloader.tidal import TidalAccount


@pytest.fixture()
def account():
    account = TidalAccount(
        os.getenv('tidal_login'),
        os.getenv('tidal_passwd')
    )
    return account

@pytest.fixture()
def client():
    ...
