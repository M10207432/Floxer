import sys
from PyQt4 import QtGui, QtCore, Qt

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


class Floxer(QtGui.QWidget):
    def __init__(self):
        super(Floxer,self).__init__()
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)      #disable title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   #Background transparent (CustomizeWindowHint)
        self.setGeometry(100,100,400,200)

        self.addWidget()

        self.show()
        
    def addWidget(self):
        img=QtGui.QLabel(self)          #add this widget to "self" parent
        img.setGeometry(10,10,400,200)
        pixmap = QtGui.QPixmap("fire.png")
        img.setPixmap(pixmap)
        
    '''
    def paintEvent(self, e=None): 
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen( QtGui.QPen(QtCore.Qt.gray,3,QtCore.Qt.DashDotLine ) )
        qp.drawRect(0,0,self.rect().width()-1, self.rect().height()-1)  
        qp.end()
    '''
    '''==============================
        Get mouse position
        in press status
    =============================='''
    def mousePressEvent(self, event):   
        self.offset = event.pos()

    '''==============================
        Change window position
        by press offset position
        in press status
    =============================='''
    def mouseMoveEvent(self, event):    
        now_x=event.globalX()
        now_y=event.globalY()
        offset_x = self.offset.x()
        offset_y = self.offset.y()
        self.move(now_x-offset_x, now_y-offset_y)

    def webShow(self,url):
        web = QWebView()
        web.load(QUrl(url))

        #Using Plug to play video
        settings = web.settings()
        settings.setAttribute(settings.PluginsEnabled, True)

        web.show()
        
def main():
    
    app = QApplication(sys.argv) 

    F=Floxer()
    
    sys.exit(app.exec_())
    
    
if __name__=="__main__":
    main()
