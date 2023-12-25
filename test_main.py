from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_button_exist(browser):
    browser.get('https://projecmainpy-aeyjgpknumzhxbptpk5dwh.streamlit.app')
    assert browser.find_element(By.ID, 'alternate-favicon').is_displayed()
#--проверяет что что то отображаеться
#----id="alternate-favicon" ---submit-id-submit
