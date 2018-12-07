import unittest
from selenium import webdriver
import os
import time

class SearchTest(unittest.TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "/chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(5)
        self.driver.get("http://testcase.haotest.com:50280")

    def test_search_accept_clue(self):
        u'''已受理线索查询'''
        ele_name = self.driver.find_element_by_name('userName')
        ele_name.send_keys('18410078814')
        ele_pwd = self.driver.find_element_by_name('password')
        ele_pwd.send_keys("123456")
        login_button = self.driver.find_element_by_id('loginBtn')
        login_button.click()
        time.sleep(5)
        self.driver.find_element_by_css_selector('.ivu-menu li:nth-child(2)').click()
        time.sleep(5)
        ele_select_status = self.driver.find_element_by_css_selector('.search-row>div:nth-child(2)')
        ele_select_status.click()

        ele_select_status.find_element_by_css_selector('.ivu-select-dropdown-list li:nth-last-child(2)').click()
        self.driver.find_element_by_css_selector('.search-btn').click()
        time.sleep(5)
        count = len(self.driver.find_elements_by_css_selector('.ivu-table-tbody tr'))
        # .ivu-table-tbody>tr.ivutable-row
        self.assertEqual(5, count)

    def tearDown(self):
        self.driver.quit()