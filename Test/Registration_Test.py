from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Facebook_Login_Register_forgetpassword.Basic_Test.Login_Locaters import Facebook_Web_Address
from Facebook_Login_Register_forgetpassword.Basic_Test.Registration_Locaters import *


def test_Facebook_Validate_Registering_with_Valid_information_by_providing_all_the_fields():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH, Registration_Page).text
    assert 'Sign Up' == signUp_Page
    firstName_spacefild = driver.find_element(By.NAME, FirstName_Element)
    firstName_spacefild.send_keys("Benel")
    sleep(2)
    surname_space = driver.find_element(By.NAME,LastName_Element)
    surname_space.send_keys("Molla")
    sleep(2)
    registerEmail_space = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_space.send_keys("specficname@****.com")
    sleep(2)
    registerReenterEmail_specefild = driver.find_element(By.NAME,Email_Reenter_Element)
    registerReenterEmail_specefild.send_keys("specficname@****.com")
    sleep(2)
    registerPassword_spacefild = driver.find_element(By.NAME, Password_Element)
    registerPassword_spacefild.send_keys("secretcode45152")
    sleep(2)
    birthDay_space = driver.find_element(By.XPATH, BirthDay_Element)
    birthDay_space.send_keys("6")
    sleep(2)
    birthMonth_space = driver.find_element(By.XPATH, BirthMonth_Element)
    birthMonth_space.send_keys("nov")
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH, BirthYear_Element)
    birthYear_box.send_keys("1998")
    sleep(2)
    driver.find_element(By.XPATH, GenderSelect_Element).click()
    sleep(2)
    driver.find_element(By.XPATH, SignUp_Button).click()
    sleep(5)
    email_conformation_Homepage = driver.find_element(By.XPATH,Email_Confirmation).text
    assert 'Enter the code from your email' == email_conformation_Homepage
    enterConfirmationcode = driver.find_element(By.NAME, "code")
    enterConfirmationcode.send_keys("8785458")
    sleep(2)
    driver.find_element(By.XPATH, Continue_Button).click()
    accountConform_page = driver.find_element(By.NAME,"Account Confirmed").text
    assert 'Account Confirmed' == accountConform_page
    driver.find_element(By.XPATH, Ok_Button).click()
    Facebook_Home = driver.current_url
    assert Facebook_Home == Facebook_Web_Address
    driver.close()


def test_Facebook_Registering_Using_Null_on_all_fields():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(5)
    error_Message = driver.find_element(By.XPATH, null_All_spaces).text
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Invalid_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,Registration_Page).text
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("Benel")
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_Element)
    surname_box.send_keys("Molla")
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("benelm1@gmail.com")
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,Email_Reenter_Element)
    registerReEnterEmail_box.send_keys("benelm1@gmail.com")
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("Mycode1245")
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH, BirthDay_Element)
    birthDay_box.send_keys("6")
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH, BirthMonth_Element)
    birthMonth_box.send_keys("nov")
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthYear_Element)
    birthYear_box.send_keys("1998")
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_Element).click()
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_InvalidEmail).text
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_With_Null_Gender():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH, Registration_Page).text
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME, FirstName_Element)
    firstName_box.send_keys("Benel")
    sleep(2)
    surname_box = driver.find_element(By.NAME, LastName_Element)
    surname_box.send_keys("Molla")
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME, EmailInput_Element)
    registerEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,Email_Reenter_Element)
    registerReEnterEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME, Password_Element)
    registerPassword_box.send_keys("secretcode1455")
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH, BirthDay_Element)
    birthDay_box.send_keys("6")
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("nov")
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthYear_Element)
    birthYear_box.send_keys("1998")
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    sleep(5)
    error_Message = driver.find_element(By.XPATH, Error_nullGender).text
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_FirstName():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH, Registration_Page).text
    assert 'Sign Up' == signUp_Page
    surname_box = driver.find_element(By.NAME, LastName_Element)
    surname_box.send_keys("Molla")
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME, EmailInput_Element)
    registerEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME, Email_Reenter_Element)
    registerReEnterEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME, Password_Element)
    registerPassword_box.send_keys("secretcode1455")
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH, BirthDay_Element)
    birthDay_box.send_keys("6")
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH, BirthMonth_Element)
    birthMonth_box.send_keys("nov")
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1998")
    sleep(2)
    driver.find_element(By.XPATH, GenderSelect_Element).click()
    sleep(2)
    driver.find_element(By.XPATH, SignUp_Button).click()
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_nullFirstName).text
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_LastName():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,Registration_Page).text
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("Benel")
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("benhashem35@gmail.com")
    registerReEnterEmail_box = driver.find_element(By.NAME,Email_Reenter_Element)
    registerReEnterEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("secretcode1455")
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthDay_box.send_keys("6")
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH, BirthMonth_Element)
    birthMonth_box.send_keys("nov")
    birthYear_box = driver.find_element(By.XPATH, BirthYear_Element)
    birthYear_box.send_keys("1998")
    sleep(2)
    driver.find_element(By.XPATH, GenderSelect_Element).click()
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_nullLastName).text
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_Birthday():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,Registration_Page).text
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("Benel")
    sleep(2)
    surname_box = driver.find_element(By.NAME, LastName_Element)
    surname_box.send_keys("Molla")
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME, EmailInput_Element)
    registerEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,Email_Reenter_Element)
    registerReEnterEmail_box.send_keys("benhashem35@gmail.com")
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME, Password_Element)
    registerPassword_box.send_keys("secretcode1455")
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH, BirthMonth_Element)
    birthMonth_box.send_keys("nov")
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1998")
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_Element).click()
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    sleep(5)
    error_Message = driver.find_element(By.XPATH, Error_Birthday).text
    assert '' == error_Message
    driver.close()