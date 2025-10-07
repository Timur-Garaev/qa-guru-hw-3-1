
from selene import browser, be, have

def test_google_search(set_browser_size):
    browser.open('https://duckduckgo.com')
    browser.element('input[id="searchbox_input"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('section[data-testid="mainline"]').should(have.text('https://qa.guru'))


def test_google_search_fail(set_browser_size):
    browser.open('https://duckduckgo.com')
    browser.element('input[id="searchbox_input"]').should(be.blank).type('ывалоыаовырацйовцй').press_enter()
    browser.element('section[data-testid="mainline"]').should(have.text('ничего не найдено'))