
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QFont

from PyQt5 import QtWidgets, QtGui, QtCore
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
import sys
from selenium_stealth import stealth
import time
import pickle



    
      

    
class test():
    print('test wokr')
    def test2(self):
        return '1'
class PushButton(QWidget):
    
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def start(self):
        threading.Thread(target=self._execute, daemon=True).start()
    def start_setting(self):
        #PushButton().Label()
        threading.Thread(target=self.GoogleSettings, daemon=True).start()
    def GoogleSettings(self):
        options = webdriver.ChromeOptions()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options.add_argument("--window-size=500,500")
        options.add_argument("--app=http://www.google.com")
        options.add_argument('--mute-audio')
        

        #cookies = pickle.load(open("cookies.pkl", "rb"))
        #for cookie in cookies:
        #    driver.add_cookie(cookie)
        driver = webdriver.Chrome(options=options)
        #cookies = pickle.load(open("cookies.pkl", "rb"))
        #for cookie in cookies:
        #    driver.add_cookie(cookie)
        #ui.WebDriverWait(driver, 300)
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
            pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
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
        #cookies = pickle.load(open("cookies.pkl", "rb"))
        #for cookie in cookies:
        #    driver.add_cookie(cookie)
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
        self.Start1 = 0
        driver.get(Youtube_list[self.Start1])
        driver.get_screenshot_as_file('test.png')
        self.label('Starting')

        wait = ui.WebDriverWait(driver, 300)
        #self.hello = Start1
        while True:
            try:
                if driver.find_element(by=By.XPATH, value=("//ytd-button-renderer[2]//a[1]//tp-yt-paper-button[1]")):
                    
                    driver.find_element(by=By.XPATH, value=("//ytd-button-renderer[2]//a[1]//tp-yt-paper-button[1]")).click()
                    print('cookie found')
                    self.logs('Cookie Found')
                    
                    #
            except NoSuchElementException:
                print('cookie not found')
                #self.logs('No cookie screen found')
                time.sleep(2)
            try:
                if EC.presence_of_element_located((By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'skip AD')]")):  
                    button = driver.find_element(by=By.XPATH, value=".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
                    driver.execute_script("arguments[0].click();", button)
                    print("ad skipped")
                    self.logs('Ad Skipped')
                else:
                    self.logs('No Ad')
                    print('not found')
            except NoSuchElementException:
                time.sleep(2)
                print('none found')
            try:
                if driver.find_element(by=By.CSS_SELECTOR, value=".ytp-chrome-controls button[title=Replay]"):
                    self.logs('Video Ended')
                    print('replay found1')
                    if self.Start1 <= len(Youtube_list):
                        print('replay found2')
                        self.Start1 += 1
                        if len(Youtube_list) <= self.Start1:
                            self.logs('stopped')
                            print('stopped')
                            driver.close()
                            self.close
                            

                        else:
                            driver.get(Youtube_list[self.Start1])
                            self.logs('Still Going')
                            
                   
                            
                            
            except NoSuchElementException:
                time.sleep(2)
                print('nonefound')

    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()
    
    def initUI(self):
        self.layout =  QVBoxLayout()
        self.setLayout(self.layout)
        #buttonAddPlayer = QPushButton('&Add player', clicked=self.Label)
        #self.layout.addWidget(buttonAddPlayer)
        self.setWindowTitle("PushButton")
        self.setGeometry(600,600,600,300)
        #Label Video's:
        
        screen = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        print(screen.width())
        xas = screen.width()
        x = 500
        y = screen.height() - screen.height()
        self.move(x, y)
        
        self.test = QLabel(self)
        self.test.setText('Waiting for videos')
        self.test.move(300, 40)
        self.test = QLabel(self)
        self.test.move(300, 20)
        
        windowExample = QtWidgets.QWidget()
        labelA = QtWidgets.QLabel(windowExample)
        labelA.setText('Label Example')
        self.OpenYoutube = QPushButton(self)
        self.OpenYoutube.setText("Open youtube player")          #text
        self.OpenYoutube.setIcon(QIcon("close.png")) #icon
        self.OpenYoutube.setShortcut('Ctrl+O')  #shortcut key
        self.OpenYoutube.setToolTip("Open Youtube player") #Tool tip
        #self.OpenYoutube.move(200,20)
        self.OpenYoutube.setFont(QFont('Arial font', 15))
        self.OpenYoutube.setGeometry(50, 100, 200, 50)
        self.OpenSettingsButton = QPushButton(self)
        self.OpenSettingsButton.setFont(QFont('Arial', 15))
        self.OpenSettingsButton.setText('Open youtube login')
        self.OpenSettingsButton.setGeometry(50, 20, 200, 50)
        #self._manager = SeleniumManager()
        
        self.OpenYoutube.clicked.connect(self.start)
        self.OpenSettingsButton.clicked.connect(self.start_setting)
        
    def label(self, label):
            self.test.setText(label)
            print('done')
    def logs(self, logs):
            self.test.setText(logs)
            
        

        #self.layout = QVBoxLayout(self)
        #self.label = QLabel("My text")

        #self.layout.addWidget(self.label)
        #self.setWindowTitle("My Own Title")
        #self.setLayout(self.layout)
       
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    
    #object_a = SeleniumManager()
    #SeleniumManager.Number(object_a)
    sys.exit(app.exec_()) 
    
    