from selenium import webdriver
import time
url = 'https://pythonworld.ru/samouchitel-python'
driver = webdriver.Chrome(executable_path = 'C:\\Users\S_U_S\\Desktop\\Selenium-webdriver\\Learn_Selenium\\drivers\\chromedriver.exe')

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()