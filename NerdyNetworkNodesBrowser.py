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

        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.Browser.back)
        navbar.addAction(back_btn)

        forth_btn = QAction('>', self)
        forth_btn.triggered.connect(self.Browser.forward)
        navbar.addAction(forth_btn)

        reload_icon = QMovie("reload_btn_icon.gif")
        reload_btn = QAction(reload_icon, 'Reload', self)
        reload_btn.triggered.connect(self.Browser.reload)
        navbar.addAction(reload_btn)

        home_icon = QIcon("home_btn_icon.png")
        home_btn = QAction(home_icon, 'Home', self)
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