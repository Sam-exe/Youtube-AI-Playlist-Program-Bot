from ast import While
import imp
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
import threading




options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
driver.get("https://youtube.com")

wait = ui.WebDriverWait(driver, 300)
while True:
    try:
        if EC.presence_of_element_located((By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'skip AD')]")):  
            button = driver.find_element(by=By.XPATH, value=".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
            driver.execute_script("arguments[0].click();", button)
            print("ad skipped")
        else:
            continue
    except NoSuchElementException:
        time.sleep(2)
        
