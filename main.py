from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


import time

email = "minster.lukas@gmail.com"
password = "XX"

chrome_path = r"C:\Users\pc\PycharmProjects\Web Development_DONE/chromedriver.exe"

service=Service(chrome_path)

driver=webdriver.Chrome(service=service)

x_path='//*[@id="s-138260025"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path'

driver.maximize_window()
driver.get("http://tinder.com")

time.sleep(5)
cookie = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")
cookie.click()
time.sleep(2)

login=driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login.click()
time.sleep(2)
login=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
login.click()
time.sleep(2)

#Switch to Google login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
cookies = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]")
cookies.click()
time.sleep(2)
login = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
login.click()
login.send_keys(email)
pw = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
pw.click()
pw.send_keys(password)
pw.send_keys(Keys.ENTER)
time.sleep(5)
driver.switch_to.window(base_window)
print("2")
allow_location = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
print("1")
allow_location.click()
print("1")
notification = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]/span")
notification.click()
time.sleep(5)
heart = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span")

for _ in range(100):
    try:
        heart.click()
        time.sleep(2)
    except:
        try:
            # when there is a match:
            okay = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button/svg")
            okay.click()
            time.sleep(2)
        except:
            # reject setting tinder as home screen:
            not_interested = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/button[2]")
            not_interested.click()
            time.sleep(2)

