# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#import pytest
#
# @pytest.fixture()
# def browser():
#     options = Options()
#     options.add_argument('--headless')
#     chrome_browser = webdriver.Chrome(options=options)
#     return chrome_browser
#
# def test_button_exist(browser):
#     browser.get('https://projecmainpy-aeyjgpknumzhxbptpk5dwh.streamlit.app') #---favicon
#     assert browser.find_element(By.XPATH, './*" + "//a').is_displayed()
#
#
# #--проверяет что что то отображаеться
# #----id="alternate-favicon" ---submit-id-submit
# #----https://docs.streamlit.io/library/advanced-features/app-testing/get-started
#

from streamlit.testing.v1 import AppTest
#
def test_project_main():
    at = AppTest.from_file("projec_main.py").run()
    assert not at.exception

    # at.text_input('text').input('text').run()
    # assert at.warning[0].value == 'Sorry, the text did not match'
#     #at.secrets['db_username'] = 'myuser'
#     #at.run()
#     # at.number_input[0].increment().run()
#     # at.button[0].click().run()
#     # assert at.markdown[0].value <= 0.01
#     #assert AppTest.from_file("projec_main.py").run()
#
#
#     #at.text_input('db_username').input('VoroninMaxim').run()
#     #assert at.warning[0].value == 'Try again.'
#
#     #assert at.button[0].value == True
#     # at.button[0].click().run()
#     # assert at.button[0].value == True
#
#     assert "My Text Toxicity App" in at.title[1].value

# def test():
#     from streamlit.testing.v1 import AppTest
#     at = AppTest.from_file("projec_main.py")
#     at.run()
#

# from streamlit.testing.v1 import AppTest
#
# def repro():
#     import streamlit as st
#     st.container()
#
# def test_repro():
#     at = AppTest.from_function(text2toxicity).run()



####----web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
####----https://docs.streamlit.io/library/advanced-features/app-testing/cheat-sheet