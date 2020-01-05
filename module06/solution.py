"""Get weather data from given URL"""
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC



def get_weather(driver, days):
    """Get weather for number of days"""
    if days <= 0 or days > 10:
        return None
    weather_list = []
    weather_text = []
    temp_int = []
    odd = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    url = "http://www.bbc.com/weather/727011/"
    driver.get(url)
    weather_elements = \
        driver.find_elements_by_class_name("wr-day__details__weather-type-description")
    for weather_element in weather_elements:
        weather_text.append(weather_element.get_attribute('innerHTML'))
    temp_elements = driver.find_elements_by_class_name("wr-value--temperature--c")
    for temp_element in temp_elements:
        temp_int.append(temp_element.get_attribute('innerHTML').split('°')[0])
#    print(weather_text)
#    print(temp_int)
    for i in range(1, days+1):
        weather_list.append((weather_text[i], int(temp_int[odd[i]])))
    return weather_list

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    print(get_weather(driver, 5))
    driver.quit()
