import unittest
from testcase.base_testcase import BaseTestCase
from pageobjects.login_page import LoginPage
import time
from framework.logger import Logger

logger = Logger(logger='TestLogin').getlog()

class TestLogin(BaseTestCase):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login('18410078814','123456')
        time.sleep(5)
        try:
            assert 'home' in login_page.get_page_url()
            logger.info('login sucess.')
        except Exception as e:
            logger.error('login Fail.%s', format(e))

if __name__ == '__main__':
    unittest.main()