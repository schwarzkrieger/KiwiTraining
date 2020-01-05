"""Get weather data from given URL"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_weather(driver, days):
    """Get weather for number of days"""
    if days <= 0 or days > 10:
        return None
    weather_list = []
    for i in range(1, days+1):
        url = "http://www.bbc.com/weather/727011/day" + str(i)
        driver.get(url)
        weather_element = driver.find_element_by_class_name("wr-day__details__weather-type-description")
        weather_text = weather_element.get_attribute('innerHTML')
        temp_element = driver.find_element_by_class_name("wr-value--temperature--c")
        temp_int = int(temp_element.get_attribute('innerHTML').split('°')[0])
        weather_list.append((weather_text, temp_int))
    return weather_list

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    print (get_weather(driver, 5))
