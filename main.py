import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, QUrl, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEngineProfile, QWebEnginePage
from adblockparser import AdblockRules

__version__ = 'v1.1'
__author__ = 'Sam.exe'
class YoutubePlayer(QWidget):
    def __init__(self, video_id, parent=None):
        super().__init__()
        self.parent = parent
        self.video_id = video_id
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        topLayout = QHBoxLayout()
        self.layout.addLayout(topLayout)

        label = QLabel('enter video id')
        self.input = QLineEdit()
        self.input.installEventFilter(self)
        self.input.setText(self.video_id)

        topLayout.addWidget(label, 1)
        topLayout.addWidget(self.input, 9)

        self.addWebView(self.input.text())

        buttonLayout =  QHBoxLayout()
        self.layout.addLayout(buttonLayout)

        buttonUpdate = QPushButton('update', clicked=self.updateVideo)
        buttonRemove = QPushButton('delete', clicked=self.removePlayer)
        buttonLayout.addWidget(buttonUpdate)
        buttonLayout.addWidget(buttonRemove)

        def eventFilter(self, source, event):
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.key_Return:
                    self.updateVideo()
            
            return super().eventFilter(source, event)



    def addWebView(self, video_id):
        self.webview = QWebEngineView()
        profile = QWebEngineProfile("my_profile", self.webview)
        #profile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.)
        webpage = QWebEnginePage(profile, self.webview)
        webpage.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)

        self.webview.setPage(webpage)
        self.webview.load(QUrl(f"https://www.youtube.com./watch?v={self.video_id}"))
        #self.webview.setUrl(QUrl(f'https://www.youtube.com/embed/{self.video_id}?autoplay=1'))
        self.layout.addWidget(self.webview)
    
    def updateVideo(self, ):
        video_Id = self.input.text()
        self.webview.load(QUrl(f"https://www.yout-ube.com./watch?v={video_Id}"))

    def removePlayer(self):
        widget = self.sender().parent()
        widget.setParent(None)
        widget.deleteLater()
        self.organizeLayout()
    def organizeLayout(self):
        playerCount = self.parent.video.count()
        players = []

        for i in reversed(range(playerCount)):
            player = self.parent.video.itemAt(i).widget()
            players.append(player)
        for indx, player in enumerate(players[::-1]):
            self.parent.video.addWidget(player, indx % 3, indx // 3)
class YoutubeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Youtube AI test')
        
        self.setMinimumSize(1800, 600)
        self.players = []

        self.layout =  QVBoxLayout()
        self.setLayout(self.layout)

        buttonAddPlayer = QPushButton('&Add player', clicked=self.addplayer)
        self.layout.addWidget(buttonAddPlayer)
        buttonUserAccount = QPushButton('&User Account', clicked=self.GoogleAccount)
        self.layout.addWidget(buttonUserAccount)
        self.video = QGridLayout()
        self.layout.addLayout(self.video)

        self.player =  YoutubePlayer('raTMa8MneTY', parent=self)
        self.video.addWidget(self.player, 0, 0)


        self.layout.addWidget(QLabel(__version__ + 'by' + __author__ , alignment=Qt.AlignBottom | Qt.AlignRight))
    def addplayer(self):
        playerCount = self.video.count()
        row = playerCount % 3
        col = playerCount // 3

        self.player = YoutubePlayer('', parent=self)
        self.video.addWidget(self.player, row, col)
    def GoogleAccount(self):
        self.webview = QWebEngineView()
        
        self.webview = QWebEngineView()
        profile = QWebEngineProfile("my_profile", self.webview)
        webpage = QWebEnginePage(profile, self.webview)
        webpage.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)

        self.webview.setPage(webpage)
        self.webview.load(QUrl(f"https://accounts.google.com/SignOutOptions?hl=nl&continue=https://myaccount.google.com/%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1"))

        self.layout.addWidget(self.webview)      
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = YoutubeWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Window Closed')