from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    x = int(x_element.text)
    x_element = browser.find_element(By.ID, 'num2')
    y = int(x_element.text)
    z = x+y
    z = str(z)
   # x = x[-3:]
    print(z)

    input1 = browser.find_element(By.ID, 'dropdown').click()
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)
    


    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()