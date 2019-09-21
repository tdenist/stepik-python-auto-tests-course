from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
	
    input1 = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);",input1)
    input1.send_keys(y)
	
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()