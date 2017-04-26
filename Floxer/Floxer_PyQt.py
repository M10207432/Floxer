import sys
from PyQt4 import QtGui, QtCore, Qt, QtWebKit
from PyQt4.phonon import Phonon
import livestreamer
import requests
import re

class Floxer(QtGui.QWidget):
    def __init__(self):
        super(Floxer,self).__init__()

        '''-------------------
            parameter
        -------------------'''
        self.webhtml = None
        #self.url1 = "https://www.gamer.com.tw/"
        #self.pos1 = [0,0,400,400]

        self.url2 = "http://disp.cc/b/62-9ZTN"
        self.pos2 = [400,0,800,800]
        '''-------------------
            Setting
        -------------------'''
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)      #disable title bar
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   #Background transparent (CustomizeWindowHint)
        self.setWindowOpacity(0.75)                              #Windows Opacity
        self.setGeometry(10,10,600,600)                       
        
        '''-------------------
            Flow
        -------------------'''
        #self.addWidget()
        #self.webHTML(self.url1)
        #self.webShow(self.url1,self.pos1)

        self.webHTML(self.url2)
        self.webShow(self.url2,self.pos2)
        #self.addVideo("../[Dymy][Shokugeki no Souma Ni no Sara][02][BIG5][1280X720].mp4")
    
        self.show()
        
    def addWidget(self):
        '''---------------
            img load
        ---------------'''
        img=QtGui.QLabel(self)              #add this widget to "self" parent
        img.setGeometry(0,0,600,600)
        
        fire_pixmap = QtGui.QPixmap("fire.png")     #Load img to pixmap
        pixmap=fire_pixmap.scaled(100,100)            #Resize pixmap
        
        img.setPixmap(fire_pixmap)                  #Load pixmap to img label

        '''---------------
            btn load
        ---------------'''
    def addVideo(self,path):
        self.vp=Phonon.VideoPlayer(self)
        self.vp.setGeometry(150,10,300,300)
        media=Phonon.MediaSource(path)
        self.vp.load(media)
        self.vp.play()
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

    def webHTML(self,url):
        web = requests.get(url)
        self.webhtml = web.text

        g = re.findall("<div align=(.*?)</div>",self.webhtml)
        rmtext = "<div align="+g[4]+"</div>"
        print rmtext
        
        self.webhtml = re.sub("<div align=(.*?)</div>", '', web.text)
        
        g1 = re.findall("<div align="+g[4]+"</div>",self.webhtml)
        rmtext = g1
        print rmtext
        
        #self.webhtml = re.sub("PC","FUCK!!!",self.webhtml)

        #web.text =None
        
    def webShow(self,url, pos):
        
        img=QtGui.QLabel(self)              #add this widget to "self" parent
        img.setGeometry(pos[0],pos[1],pos[2],pos[3])
        
        self.web = QtWebKit.QWebView(img)

        #Using Plug to play video
        settings = QtWebKit.QWebSettings
        settings.globalSettings().setAttribute(settings.PluginsEnabled, True)

        #web.resize(400,200)
        #self.web.load(QtCore.QUrl(url))
        if self.webhtml == None:
            "Without HTML"
            self.web.load(QtCore.QUrl(url))    
        else:
            "With HTML Revise"
            self.web.setHtml(self.webhtml,QtCore.QUrl(url))
        self.web.show()

        #web signal
        self.web.loadFinished.connect(self.cusHtml)
        
    def cusHtml(self):
        
        frame = self.web.page().mainFrame()
        html=frame.toHtml()
        #print unicode(frame.toHtml()).encode('utf-8')
        #self.web.setHtml(html,self.web.url())
        
def main():
    app = QtGui.QApplication(sys.argv) 

    F=Floxer()
    
    sys.exit(app.exec_())

def test():
    '''
    streams=livestreamer.streams("https://www.twitch.tv/wei81610")
    stream=streams['source']
    fd=stream.open()
    data=fd.read(1024)
    fd.close()

    print data
    print type(data)
    '''

    app = QtGui.QApplication(sys.argv)
    
    #-----------

    #-----Panel
    panel=QtGui.QWidget()
    panel.setGeometry(10,10,600,600)

    #-----VideoPlayer in panel
    vp=Phonon.VideoPlayer(panel)
    vp.setGeometry(10,10,600,600)
    media=Phonon.MediaSource("../[Dymy][Shokugeki no Souma Ni no Sara][02][BIG5][1280X720].mp4")
    vp.load(media)
    vp.play()

    panel.show()
    #-----------
       
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
    #test()
    
    

