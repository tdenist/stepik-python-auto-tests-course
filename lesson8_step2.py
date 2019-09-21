from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(a)+int(b)))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()