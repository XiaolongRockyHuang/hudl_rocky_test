import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Base_Page(object):
    """ Base class to initialize the base page that will be called from all pages """

    def __init__(self, driver):
        self.driver = driver

class Home_Page(Base_Page):

    def click_login_button(self):
        """ click the login button and go to the login page """
        element = self.driver.find_element(By.LINK_TEXT,"Log in")
        element.click()

class Login_Page(Base_Page):

    # input email
    def input_email(self,email):
        element = self.driver.find_element(By.ID,"email")
        element.send_keys(email)

    #input password
    def input_password(self,psw):
        element = self.driver.find_element(By.ID,"password")
        element.send_keys(psw)

    #click login button
    def click_submit_button(self):
        element = self.driver.find_element(By.ID,"logIn")
        element.click()



