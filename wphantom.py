import selenium
from selenium import webdriver  
#driver = webdriver.PhantomJS()

options = selenium.webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)

driver.get("https://handbook.monash.edu/current/units/FIT4165")

# element = driver.find_elements_by_class_name("css-1smylv8-Box-Flex")
# print(element[0].text)

learningoutcomes = driver.find_element_by_id("Learningoutcomes")
print(learningoutcomes.text.replace("keyboard_arrow_down", "\n"))