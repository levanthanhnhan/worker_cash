from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from clickWatch import click_watch_video

user_data = "C:\\Users\\NHANLE\\Documents\\Projects\\selenium\\worker_cash\\UserData"

# Create chromeoptions instance
options = webdriver.ChromeOptions()

# Provide location where chrome stores profiles
options.add_argument(r"--user-data-dir=" + user_data)
options.add_argument(r"--disk-cache-size=0")

path = ("./chromedriver.exe")
service = Service(path)
browser = webdriver.Chrome(service=service, options=options)

browser.delete_all_cookies()

browser.get("https://worker.cash/")
wait = WebDriverWait(browser, 60)

# # Login
# btn_login_with_google = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div[2]/a[2]/div/div")))
# btn_login_with_google.click()

# # Login with account exist (option 2)
# account = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div[1]/div/div[2]")))
# account.click()

# Click start earning
btn_start_earn = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div[2]/div/div[1]/ul/li[2]/a/span")))
btn_start_earn.click()

 # Store the ID of the original window
original_window = browser.current_window_handle

sleep(1)
# watch_count = wait.until(EC.visibility_of_element_located((By.ID, "curLimit"))).text
is_exist_watch_count = browser.execute_script("return parseInt(document.getElementById('curLimit').innerHTML) > 0")
while(is_exist_watch_count):
    click_watch_video(browser, original_window, wait)
    browser.switch_to.window(original_window)
    is_exist_watch_count = browser.execute_script("return parseInt(document.getElementById('curLimit').innerHTML) > 0")

