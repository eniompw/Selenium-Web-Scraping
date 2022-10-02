from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://uk.finance.yahoo.com")
cookies = driver.find_element(By.XPATH, '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button')
cookies.click()
input = driver.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]')
input.send_keys("TSLA")
input.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)
output = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')

print(output.text)
driver.quit()
