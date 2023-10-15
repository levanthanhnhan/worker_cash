from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

def click_watch_video(browser, original_window, wait):
    # Click watch video
    browser.switch_to.window(original_window)
    browser.refresh()
    btn_start_earn = wait.until(EC.visibility_of_element_located((By.ID, "btn_card_run")))
    btn_start_earn.click()

    # Loop through until we find a new window handle
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break

    # Switch iframe youtube
    iframe = wait.until(EC.visibility_of_element_located((By.ID, "task_video")))
    browser.switch_to.frame(iframe)

    # Play video
    btn_play_video = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/button")))
    btn_play_video.click()

    # Switch parent iframe youtube
    browser.switch_to.parent_frame()

    # Loop wait time countdown return youtube close tab
    while(browser.execute_script("return window.location.origin;") != 'https://www.youtube.com'):
        print(browser.execute_script("return window.location.origin;"))

        # iframe = wait.until(EC.visibility_of_element_located((By.ID, "task_video")))
        # browser.switch_to.frame(iframe)

        # sleep(3)
        # is_captcha = browser.execute_script(" return document.getElementById('captcha').style.getPropertyValue('background') != '' ")
        # if is_captcha:
        #     browser.switch_to.parent_frame()
        #     browser.close()
        
    browser.close()