import unittest
import time
import Pages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class hudl_login(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/XiaolongHuang/downloads/chromedriver')
    
    def test_Login_wrong_pw(self):
        driver = self.driver
        driver.get("https://www.hudl.com")  # open hudl home page
        Home_Page = Pages.Home_Page(self.driver)
        Home_Page.click_login_button()    # click the login button
        
        Login_Page = Pages.Login_Page(self.driver)
        Login_Page.input_email("hxl0417@hotmail.com")   # input account email
        Login_Page.input_password("abcd1234")  # login with wrong password without capital letter
        Login_Page.click_submit_button()

        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),\"We didn't recognize that email and/or password.\")]")))
        assert "Home - Hudl" not in driver.title


    def test_Login_correct_pw(self):
        driver = self.driver
        driver.get("https://www.hudl.com")  # open hudl home page
        Home_Page = Pages.Home_Page(self.driver)
        Home_Page.click_login_button()  # click the login button
        
        Login_Page = Pages.Login_Page(self.driver)
        Login_Page.input_email("hxl0417@hotmail.com")   # input account email
        Login_Page.input_password("Abcd1234")   #login with correct password with capital letter
        Login_Page.click_submit_button()

        WebDriverWait(driver,10).until(EC.title_is("Home - Hudl"))
        assert "Home - Hudl" in driver.title

    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()