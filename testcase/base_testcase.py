from selenium import webdriver
from framework.browser_engine import BrowserEngine
import unittest
import os

class BaseTestCase(unittest.TestCase):

    browser = BrowserEngine()

    def setUp(self):
        self.driver = self.browser.open_browser()

    def tearDown(self):
        self.browser.quit_browser()
