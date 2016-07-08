import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

def main():
    app = QApplication(sys.argv)

    web = QWebView()
    web.load(QUrl("https://www.twitch.tv/"))

    #Using Plug to play video
    settings = web.settings()
    settings.setAttribute(settings.PluginsEnabled, True)

    web.show()
     
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()
