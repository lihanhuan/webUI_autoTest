from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import unittest

logger = Logger(logger='BasePage').getlog()

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            element = self.driver.find_element(*loc)
            logger.info("找到页面元素-->%s", loc)
            return element
        except:
            logger.error("%s 页面中未能找到 %s 元素" % (self, loc))

    # 输入
    def sendkeys(self, text, *loc):
        el = self.find_element(*loc)
        try:
            el.send_keys(text)
            logger.info("输入内容%s", text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)


    # 点击元素
    def click(self, *loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("The element %s  was clicked." % el.text)
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)

    def get_page_url(self):
         logger.info("Current page url is %s" % self.driver.current_url)
         return self.driver.current_url
