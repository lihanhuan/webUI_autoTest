import os
from selenium import webdriver

dir = os.path.dirname(__file__)
chrome_driver_path = dir + '/chromedriver.exe'
print(chrome_driver_path)
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(5)
# driver.get("http://testcase.haotest.com:50280/login")
driver.get("https://www.seleniumhq.org/")
driver.find_element_by_partial_link_text('edit').click()
driver.find_element_by_link_text('edit').click()
ele_name  = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[1]/div/div[1]/input')
ele_name.send_keys('18410078814')
ele_pwd = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[2]/div/div[1]/input')
ele_pwd.send_keys("123456")
login_button = driver.find_element_by_class_name('ivu-btn')
login_button.click()
driver.find_element_by_link_text("线索管理").click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[2]/span').click()
driver.maximize_window()

eles = driver.find_elements_by_tag_name('tr')
assert len(eles) == 14

