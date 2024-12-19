from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# navigate to wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

# find elements by link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the "Search" <input> by name
# search = driver.find_element(By.NAME, value="search")
# sending keyboard input to Selenium
# search.send_keys("Python", Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# find out
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")

# fill out the form
first_name.send_keys("p")
last_name.send_keys("s")
email.send_keys("p@gmail.com")
submit.click()