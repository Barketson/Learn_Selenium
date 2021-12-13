from selenium import webdriver
import time
url = 'http://localhost/litecart/admin/login.php'
driver = webdriver.Chrome(executable_path = 'C:\\Users\S_U_S\\Desktop\\Selenium-webdriver\\Learn_Selenium\\drivers\\chromedriver.exe')

try:
    driver.get(url=url)
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()