import sys
from PyQt4 import QtGui, QtCore, Qt, QtWebKit

class Floxer(QtGui.QWidget):
    def __init__(self):
        super(Floxer,self).__init__()

        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)      #disable title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   #Background transparent (CustomizeWindowHint)
        self.setWindowOpacity(.75)                              #Windows Opacity
        self.setGeometry(10,10,600,600)                       

        self.addWidget()
        self.webShow("http://youtube.com")

        self.show()
        
    def addWidget(self):
        '''---------------
            img load
        ---------------'''
        img=QtGui.QLabel(self)              #add this widget to "self" parent
        img.setGeometry(10,10,600,600)
        
        fire_pixmap = QtGui.QPixmap("fire.png")     #Load img to pixmap
        pixmap=fire_pixmap.scaled(100,100)            #Resize pixmap
        
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
        img.setGeometry(100,10,400,600)
        
        web = QtWebKit.QWebView(img)
        #web.resize(400,200)
        web.load(QtCore.QUrl(url))

        #Using Plug to play video
        settings = web.settings()
        settings.setAttribute(settings.PluginsEnabled, True)
        
def main():
    app = QtGui.QApplication(sys.argv) 

    F=Floxer()
    
    sys.exit(app.exec_())
    
    
if __name__=="__main__":
    main()
