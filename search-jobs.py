from selenium import webdriver
import time
import os

dir = os.path.dirname(__file__)
chrome_driver_path = dir + '/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")

    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)

    while True:
        jobs = driver.find_elements_by_css_selector('.item_con_list li')

        for job in jobs:
            job_link = job.find_element_by_css_selector('.p_top a span')
            job_link.click()

            driver.switch_to.window(driver.window_handles[1])

            job_company = driver.find_element_by_css_selector('.company')
            job_name = driver.find_element_by_css_selector('.name')
            job_money = driver.find_element_by_css_selector('.salary')
            spans = driver.find_elements_by_css_selector('.job_request p span')
            work_age = spans[2]

            print('公司：',job_company.text,
                  '; 职位名称：',job_name.text,
                  '; 薪资范围：',job_money.text,
                  '; 工作经验：', work_age.text
                  )
            driver.close()
            driver.switch_to.window(window_list)

        # next_page = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '.item_con_pager .pager_container > *:last-child')))
        next_page = driver.find_element_by_css_selector('.item_con_pager .pager_container > *:last-child')
        next_page_class = next_page.get_attribute('class')

        if 'pager_next_disabled' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)

finally:
    time.sleep(10)
    driver.quit()