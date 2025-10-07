import  pytest
from selene import browser


@pytest.fixture()
def set_browser_size():
    browser.config.window_width = 2000
    browser.config.window_height = 2000

    yield

    browser.quit()