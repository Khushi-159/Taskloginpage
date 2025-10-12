import pytest
from Pages.login_page import LoginPage
def test_invalid_email_format(driver):
    login = LoginPage(driver)
    login.enter_email("invalidemail")
    login.enter_password("Valid@123")
    login.click_login()
    assert " '@'" in login.get_email_error()

def test_empty_email(driver):
    login = LoginPage(driver)
    login.enter_email("")
    login.enter_password("Valid@123")
    login.click_login()
    assert "*" in login.get_email_error()

def test_empty_password(driver):
    login = LoginPage(driver)
    login.enter_email("validemail@test.com")
    login.enter_password("")
    login.click_login()
    assert "*" in login.get_password_error()

def test_empty_email_password(driver):
    login = LoginPage(driver)
    login.enter_email("")
    login.enter_password("")
    login.click_login()
    assert "*" in login.get_email_error() and "*" in login.get_password_error()

def test_email_with_spaces(driver):
    login = LoginPage(driver)
    login.enter_email("   ")
    login.enter_password("Valid@123")
    login.click_login()
    assert "*" in login.get_email_error()

def test_short_password(driver):
    login = LoginPage(driver)
    login.enter_email("validemail@test.com")
    login.enter_password("123")
    login.click_login()
    assert "*" in login.get_password_error()

def test_unregistered_email(driver):
    login = LoginPage(driver)
    login.enter_email("newuser@test.com")
    login.enter_password("Valid@123")
    login.click_login()
    assert "*" in login.get_email_error() or "User not found" in login.get_email_error()

def test_special_char_email(driver):
    login = LoginPage(driver)
    login.enter_email("invalid!email@test.com")
    login.enter_password("Valid@123")
    login.click_login()
    assert "*" in login.get_email_error()
