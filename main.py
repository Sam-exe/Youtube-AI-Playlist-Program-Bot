import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, QUrl, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEngineProfile, QWebEnginePage
from adblockparser import AdblockRules

__version__ = 'v1.1'
__author__ = 'Sam.exe'

with open("easylist.txt", "r",  encoding='utf8') as f:
    raw_rules = f.readlines()
    rules = AdblockRules(raw_rules)

class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if rules.should_block(url):
            print("block::::::::::::::::::::::", url)
            info.block(True)

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
        self.webview.load(QUrl(f"https://www.youtube.com/watch?v={self.video_id}aKCNrkERJ3E"))
        #self.webview.setUrl(QUrl(f'https://www.youtube.com/embed/{self.video_id}?autoplay=1'))
        self.layout.addWidget(self.webview)
    
    def updateVideo(self, ):
        video_Id = self.input.text()
        self.webview.load(QUrl(f"https://www.youtube.com/watch?v={video_Id}aKCNrkERJ3E"))

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
    
    
    @QtCore.pyqtSlot(bool)
    def on_loadFinished(self, ok):
            print('working')
            self.emulate_click(None, QtCore.QPoint(400, 200))

    def emulate_click(self, widget, pos):
        event_press = QtGui.QMouseEvent(
            QtCore.QEvent.MouseButtonPress,
            pos,
            QtCore.Qt.LeftButton,
            QtCore.Qt.LeftButton,
            QtCore.Qt.NoModifier,
        )
        QtCore.QCoreApplication.postEvent(widget, event_press)
        event_release = QtGui.QMouseEvent(
            QtCore.QEvent.MouseButtonRelease,
            pos,
            QtCore.Qt.LeftButton,
            QtCore.Qt.LeftButton,
            QtCore.Qt.NoModifier,
        )
        QtCore.QCoreApplication.postEvent(widget, event_release)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interceptor = WebEngineUrlRequestInterceptor()
    QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setRequestInterceptor(interceptor)
    window = YoutubeWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Window Closed')