from selenium import webdriver
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    __login_page_username_locator = (By.NAME, 'userName')
    __login_page_password_locator = (By.NAME, 'password')
    __login_page_loginBtn_locator = (By.ID, 'loginBtn')

    # 输入用户名
    def input_username(self, username):
        self.sendkeys(username, *self.__login_page_username_locator)

    # 输入密码
    def input_password(self, password):
        self.sendkeys(password, *self.__login_page_password_locator)

    # 点击登录按钮
    def click_loginBtn(self):
        self.click(*self.__login_page_loginBtn_locator)

    # 登录功能实现
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_loginBtn()

