import selenium
from selenium import webdriver
#driver = webdriver.PhantomJS()

options = selenium.webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

# unit = input("Please enter a unit name (exact, including casing): ")
# url = "https://handbook.monash.edu/current/units/" + unit
url = "https://handbook.monash.edu/current/units/FIT4165"

driver.get(url)

learningoutcomes = driver.find_element_by_id("Learningoutcomes")
print(learningoutcomes.text.replace("keyboard_arrow_down", "\n").replace("Expand all", ""))


value = "Prerequisite"
prereq = driver.find_element_by_xpath("//td[.='%s']/following-sibling::textarea" % value)
print(prereq.get_attribute('innerHTML'))

prerequisites = driver.find_elements_by_css_selector(".css-1f1s0ai-StyledAILinkHeaderSection.exq3dcx3")
for element in prerequisites:
    print(element.get_attribute('innerHTML'))

# css-1f1s0ai-StyledAILinkHeaderSection exq3dcx3
# css-1f1s0ai-StyledAILinkHeaderSection exq3dcx3