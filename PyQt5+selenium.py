from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import threading
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from pyvirtualdisplay import Display
import time


class SeleniumManager(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def start(self):
        threading.Thread(target=self._execute, daemon=True).start()

    def _execute(self):
        options = webdriver.ChromeOptions()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        #options = webdriver.ChromeOptions()
        #options.headless = True
        options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
        options.add_argument(f'user-agent={user_agent}')
        #options.add_argument("--window-size=1920,1080")
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--start-maximized")
        #options.add_argument("--headless")
        #options.add_argument('window-size=1920x1080')
        options.headless = True
        #options.add_argument('--incognito')
        #options.add_argument('--mute-audio')
        driver = webdriver.Chrome(options=options)
        stealth(driver,
            languages=["en-US", "en"],
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
        list = ['https://www.youtube.com/watch?v=0_CDMstFg7M', 'https://www.youtube.com/watch?v=XpH3O6mnZvw']
        driver.get(list[0])
        driver.get_screenshot_as_file('test.png')
        try:
            if driver.find_element(by=By.XPATH, value=("./html[1]/body[1]/ytd-app[1]/ytd-consent-bump-v2-lightbox[1]/tp-yt-paper-dialog[1]/div[4]/div[1]/div[6]/div[1]/ytd-button-renderer[2]/a[1]/tp-yt-paper-button[1]")):
                driver.find_element(by=By.XPATH, value=("./html[1]/body[1]/ytd-app[1]/ytd-consent-bump-v2-lightbox[1]/tp-yt-paper-dialog[1]/div[4]/div[1]/div[6]/div[1]/ytd-button-renderer[2]/a[1]/tp-yt-paper-button[1]")).click()
        except NoSuchElementException:
            None

        wait = ui.WebDriverWait(driver, 300)
        
        while True:
            try:
                if EC.presence_of_element_located((By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'skip AD')]")):  
                    button = driver.find_element(by=By.XPATH, value=".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
                    driver.execute_script("arguments[0].click();", button)
                    driver.get_screenshot_as_file('test1.png')
                    print("ad skipped")
                else:
                    driver.get_screenshot_as_file('test1.png')
                    continue
            except NoSuchElementException:
                time.sleep(2)
            try:
                if driver.find_element(by=By.CSS_SELECTOR, value=".ytp-chrome-controls button[title=Replay]"):
                    driver.get(list[1])

                    print("working")
            except NoSuchElementException:
                time.sleep(2)
        
class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(400,400,300,260)
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Open youtube player")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+O')  #shortcut key
        self.closeButton.setToolTip("Open Youtube player") #Tool tip
        self.closeButton.move(100,0)

        self._manager = SeleniumManager()
        self.closeButton.clicked.connect(self._manager.start)
    def test():
        print("test")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_()) 