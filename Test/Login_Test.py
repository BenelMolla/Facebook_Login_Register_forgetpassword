from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Facebook_Login_Register_forgetpassword.Basic_Test.Login_Locaters import *


def test_Facebook_Login_Functionality_with_Real_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_field)
    sleep(2)
    email.clear()
    email.send_keys(Login_real_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_field)
    sleep(2)
    password.clear()
    password.send_keys(Login_real_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(5)
    Facebook_Homepage = driver.find_element(By.XPATH,HomePage)
    assert 'https://www.facebook.com/' == Facebook_Web_Address
    driver.close()



def test_Facebook_Login_Functionality_with_Invalid_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_field)
    sleep(2)
    email.clear()
    email.send_keys(Login_unreal_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_field)
    sleep(2)
    password.clear()
    password.send_keys(Login_unreal_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button.
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_unreal_Email_and_Password_error).text
    assert 'The email you entered isn’t connected to an account.' == Error_message
    sleep(5)
    driver.close()


def test_Facebook_Login_Functionality_with_Valid_Email_and_Invalid_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_field)
    sleep(2)
    email.clear()
    email.send_keys(Login_real_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_field)
    sleep(2)
    password.clear()
    password.send_keys(Login_unreal_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_realEmail_and_InvalidPassword_error).text
    assert 'The password you have entered isn’t connected to an account' == Error_message
    sleep(5)
    driver.close()


def test_Facebook_Login_Functionality_with_Invalid_Email_and_Valid_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_field)
    sleep(2)
    email.clear()
    email.send_keys(Login_unreal_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_field)
    sleep(2)
    password.clear()
    password.send_keys(Login_real_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_InvalidEmail_and_realPassword_error).text
    assert 'The password you have entered isn’t connected to an account' == Error_message
    sleep(5)
    driver.close()
#
#
def test_Facebook_Login_Functionality_with_null_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_null_EmailAndPassword_error).text
    assert "The email or mobile number you entered isn’t connected to an account. Find your account and log in." == Error_message
    sleep(5)
    driver.close()

