from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Facebook_Login_Register_forgetpassword.Basic_Test.Login_Locaters import Facebook_Web_Address
from Facebook_Login_Register_forgetpassword.Basic_Test.Forget_password_locater import *


def test_Facebook_ForgetPassword_Functionality_with_Valid_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword_lane).click()
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH, FindYourAccount_).text
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    identifyEmail = driver.find_element(By.XPATH, Identify_email_Elementlane)
    sleep(2)
    identifyEmail.clear()
    identifyEmail.send_keys(ForgetPassword_Valid_Email)
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()
    sleep(2)
    IdentifyYourAccount_Page = driver.find_element(By.XPATH,IdentifyYourAccount_Elementlane).text
    assert "Identify your account" == IdentifyYourAccount_Page
    sleep(2)
    driver.find_element(By.XPATH,MyAccount_Button).click()
    sleep(2)
    ResetYourPassword_Page = driver.find_element(By.XPATH, ResetYourPasswordPage_Elementlane).text
    assert 'Reset Your Password' == ResetYourPassword_Page
    driver.find_element(By.XPATH, SendCode_Via_messageButton_Elementlane).click()
    sleep(2)
    driver.find_element(By.XPATH,ResetPassword_continueButton).click()
    sleep(2)
    securityCodePage = driver.find_element(By.XPATH, EnterSecurityCodePage_Elementlane).text
    assert "Enter security code" == securityCodePage
    sleep(2)
    recovery_code_entry = driver.find_element(By.XPATH, RecoveryCodeEntry_Elementlane)
    sleep(2)
    recovery_code_entry.clear()
    recovery_code_entry.send_keys("ben14725825")
    sleep(2)
    driver.find_element(By.XPATH,ResetPassword_continueButton).click()
    sleep(2)
    newPassword_Page = driver.find_element(By.XPATH, NewPasswordPage_Elementlane).text
    assert "Choose a new password" == newPassword_Page
    newpassword_entry = driver.find_element(By.NAME, "password_new")
    newpassword_entry.send_keys("Refill_password_new")
    sleep(2)
    driver.find_element(By.XPATH, NewPassword_ContinueButton).click()
    sleep(2)
    Facebook_Home = driver.current_url
    assert Facebook_Home == Facebook_Web_Address
    driver.close()


def test_Facebook_ForgetPassword_Functionality_with_Invalid_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword_lane).click()
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH, FindYourAccount_).text
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    identifyEmail = driver.find_element(By.XPATH, Identify_email_Elementlane)
    sleep(2)
    identifyEmail.clear()
    identifyEmail.send_keys(ForgetPassword_Invalid_Email)
    sleep(2)
    driver.find_element(By.XPATH, Email_Search_Button).click()
    sleep(2)
    errorMessage = driver.find_element(By.XPATH, NoSearchResults_errorMessage).text
    assert "No search results" == errorMessage
    driver.close()


def test_Facebook_ForgetPassword_Functionality_with_Null_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword_lane).click()
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH, FindYourAccount_).text
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()
    sleep(2)
    IdentifyYourAccount_Page = driver.find_element(By.XPATH, Please_FillIn_OneField_ErrorMessage).text
    assert "Please fill in at least one field" == IdentifyYourAccount_Page
    driver.close()