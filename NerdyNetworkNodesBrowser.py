import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        # browser
        super(MainWindow, self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.Browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_icon =QIcon("backward_btn_icon.png")
        back_btn = QAction(back_icon, "Backward", self)
        back_btn.triggered.connect(self.Browser.back)
        navbar.addAction(back_btn)

        forward_icon = QIcon("forward_btn_icon.png")
        forward_btn = QAction(forward_icon, "Forward", self)
        forward_btn.triggered.connect(self.Browser.forward)
        navbar.addAction(forward_btn)

        reload_gif = QIcon("reload_btn_icon.gif")
        reload_btn = QAction(reload_gif, "Reload", self)
        reload_btn.triggered.connect(self.Browser.reload)
        navbar.addAction(reload_btn)

        home_icon = QIcon("home-btn_icon.png")
        home_btn = QAction(home_icon, "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.Browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.Browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.Browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Nerdy Networks Nodes Browser")
window = MainWindow()
app.exec_()