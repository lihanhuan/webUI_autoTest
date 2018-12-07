import unittest
from selenium import webdriver
import os
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "/chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(5)
        self.driver.get("http://testcase.haotest.com:50280")

    def test_login(self):
        u'''测试登录用例，账号：xx 密码xx'''
        ele_name = self.driver.find_element_by_xpath('userName')
        ele_name.send_keys('18410078814')
        ele_pwd = self.driver.find_element_by_name('password')
        ele_pwd.send_keys("123456")
        login_button = self.driver.find_element_by_id('loginBtn')
        login_button.click()
        time.sleep(5)

        self.assertIn('home', self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


