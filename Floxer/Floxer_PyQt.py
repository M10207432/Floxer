import sys
from PyQt4 import QtGui, QtCore, Qt, QtWebKit

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


class Floxer(QtGui.QWidget):
    def __init__(self):
        super(Floxer,self).__init__()

        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)      #disable title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   #Background transparent (CustomizeWindowHint)
        self.setWindowOpacity(.75)                              #Windows Opacity
        self.setGeometry(100,100,400,200)                       

        self.addWidget()
        self.webShow("http://google.com")

        self.show()
        
    def addWidget(self):
        '''---------------
            img load
        ---------------'''
        img=QtGui.QLabel(self)              #add this widget to "self" parent
        img.setGeometry(10,10,400,200)
        
        fire_pixmap = QtGui.QPixmap("fire.png")     #Load img to pixmap
        pixmap=fire_pixmap.scaled(50,50)            #Resize pixmap
        
        img.setPixmap(fire_pixmap)                  #Load pixmap to img label

        '''---------------
            btn load
        ---------------'''
        
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
        img=QtGui.QLabel(self)              #add this widget to "self" parent
        img.setGeometry(50,10,400,200)
        
        web = QtWebKit.QWebView(img)
        web.load(QUrl(url))

        #Using Plug to play video
        settings = web.settings()
        settings.setAttribute(settings.PluginsEnabled, True)

        web.show()
        
def main():
    app = QtGui.QApplication(sys.argv) 

    F=Floxer()
    
    sys.exit(app.exec_())
    
    
if __name__=="__main__":
    main()
