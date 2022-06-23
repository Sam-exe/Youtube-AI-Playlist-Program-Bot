from turtle import done
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QVBoxLayout, QLabel
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
import threading
import sys
from selenium_stealth import stealth
import time


class SeleniumManager(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def start(self):
        threading.Thread(target=self._execute, daemon=True).start()
    def start_setting(self):
        threading.Thread(target=self.GoogleSettings, daemon=True).start()
    def GoogleSettings(self):
        options = webdriver.ChromeOptions()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options.add_argument("--window-size=500,500")
        options.add_argument("--app=http://www.google.com")
        options.add_argument('--mute-audio')
        driver = webdriver.Chrome(options=options)
        ui.WebDriverWait(driver, 300)
        stealth(driver,
            languages=["en-US", "en"],
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
        driver.get('https://www.google.com')
        while True:
            continue
    def _execute(self):
        options = webdriver.ChromeOptions()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options.add_argument("--window-size=500,500")
        #options.add_argument("--headless")
        #options.add_argument('--disable-gpu')
        #options.add_argument("--remote-debugging-port=9222")
        #options.add_argument("--app=http://www.google.com")
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
        Youtube_list = ['https://www.youtube.com/watch?v=0_CDMstFg7M', 'https://www.youtube.com/watch?v=0_CDMstFg7M','https://www.youtube.com/watch?v=0_CDMstFg7M']
        Start = 0
        driver.get(Youtube_list[Start])
        driver.get_screenshot_as_file('test.png')
        

        wait = ui.WebDriverWait(driver, 300)
        
        while True:
            try:
                if driver.find_element(by=By.XPATH, value=("./html[1]/body[1]/ytd-app[1]/ytd-consent-bump-v2-lightbox[1]/tp-yt-paper-dialog[1]/div[4]/div[1]/div[6]/div[1]/ytd-button-renderer[2]/a[1]/tp-yt-paper-button[1]")):
                    driver.find_element(by=By.XPATH, value=("./html[1]/body[1]/ytd-app[1]/ytd-consent-bump-v2-lightbox[1]/tp-yt-paper-dialog[1]/div[4]/div[1]/div[6]/div[1]/ytd-button-renderer[2]/a[1]/tp-yt-paper-button[1]")).click()
            except NoSuchElementException:
                time.sleep(2)
            try:
                if EC.presence_of_element_located((By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'skip AD')]")):  
                    button = driver.find_element(by=By.XPATH, value=".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
                    driver.execute_script("arguments[0].click();", button)
                    driver.get_screenshot_as_file('test1.png')
                    print("ad skipped")
                else:
                    driver.get_screenshot_as_file('test1.png')
                    print('nonefound')
            except NoSuchElementException:
                time.sleep(2)
                print('nonefound')
            try:
                if driver.find_element(by=By.CSS_SELECTOR, value=".ytp-chrome-controls button[title=Replay]"):
                    #driver.get('https://www.youtube.com/watch?v=0_CDMstFg7M')
                    print('replay found1')
                    #driver.get('https://www.youtube.com/watch?v=0_CDMstFg7M')
                    if Start <= len(Youtube_list):
                        print('replay found2')
                        Start += 1
                        
                        if len(Youtube_list) <= Start:
                            print('stopped')
                            driver.close()
                            
                        else:
                            driver.get(Youtube_list[Start])
                            
            except NoSuchElementException:
                time.sleep(2)
                print('nonefound')
        
class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(600,600,600,300)
        screen = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        print(screen.width())
        xas = screen.width()
        x = 500
        y = screen.height() - screen.height()
        self.move(x, y)
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Open youtube player")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+O')  #shortcut key
        self.closeButton.setToolTip("Open Youtube player") #Tool tip
        self.closeButton.move(200,20)
        self.closeButton.setGeometry(200, 150, 100, 40)
        self.OpenSettingsButton = QPushButton(self)
        self.OpenSettingsButton.setText('Open youtube login')
        self.OpenSettingsButton.move(50,20)
        self._manager = SeleniumManager()
        self.closeButton.clicked.connect(self._manager.start)
        self.OpenSettingsButton.clicked.connect(self._manager.start_setting)



        self.layout = QVBoxLayout(self)
        self.label = QLabel("My text")

        self.layout.addWidget(self.label)
        self.setWindowTitle("My Own Title")
        self.setLayout(self.layout)
    def test():
        print("test")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_()) 