from selenium import webdriver
from selenium.webdriver.common.by import By

# Open the browser and navigate to the Instagram profile
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the page to load
driver.implicitly_wait(10)

# Find elements using XPath
followers_element = driver.find_element(By.XPATH, value = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span')
following_element = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span')

# Extract the text and print the results
followers_count = followers_element.text
following_count = following_element.text

print("Followers:", followers_count)
print("Following:", following_count)

# Close the browser
driver.quit()