import sys
from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4 import Qt
from PyQt4.phonon import Phonon

import livestreamer
import requests
import re

        
class Floxer(QtGui.QWidget):
    def __init__(self):
        super(Floxer,self).__init__()

        '''-------------------
            Config
        -------------------'''
        self.url = ["http://disp.cc/b/62-a2BY"]
        self.webhtml = None
        self.browser = []
        self.urledit = QtGui.QLineEdit()
        self.grid = QtGui.QGridLayout()
        [self.browser.append(QtWebKit.QWebView()) for i in range(len(self.url))]
        self.zoomfactor = 0.1
        self.main_w = -1
        self.main_h = -1
        self.main_size = 0
        '''-------------------
            Layout Setting
        -------------------'''
        settings = QtWebKit.QWebSettings
        settings.globalSettings().setAttribute(settings.PluginsEnabled, True)
        
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)      #disable title bar
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   #Background transparent (CustomizeWindowHint)
        self.setWindowOpacity(1)                              #Windows Opacity
        self.setGeometry(10,10,600,600)                       

        self.grid.addWidget(self.urledit, 1, 0)
        self.grid.addWidget(self.browser[0], 2, 0)
        
        #[self.grid.addWidget(browser, i + 2, 0, 3, 3) for i,browser in enumerate(self.browser)]
        
        self.urledit.returnPressed.connect(self._urlcallback) #link url callback function
        self.setLayout(self.grid)

        self.resizeEvent=self._resizeCB
        '''-------------------
            Flow
        -------------------'''
        html_obj = open("./html/t1.htm",'rb')
        html_file = html_obj.read()
        
        for i, browser in enumerate(self.browser):
            url = self.url[int(i)]
            self.cusHtml(i, "1554index")
            
            #browser.setHtml( html_file,QtCore.QUrl(url))
            #browser.load(QtCore.QUrl(url))
            
    def _resizeCB(self,evt):
        if not(self.main_w == -1 and self.main_h == -1):
            size = evt.size().height() * evt.size().width()
            ratio = float(size)/float(self.main_size)
            self.browser[0].setZoomFactor(ratio)
            print ratio
            
        if self.main_w == -1 and self.main_h == -1:
            self.main_w = evt.size().width()
            self.main_h = evt.size().height()
            self.main_size = self.main_h * self.main_w
        
    def _urlcallback(self):
        raw_url = self.urledit.text()
        
        #self.webHTML(raw_url)
        #self.browser.setHtml(self.webhtml,QtCore.QUrl(raw_url))
        #self.browser.load(url)
        #print url
        
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
        print url
        web = requests.get(url)
        self.webhtml = None
        
        #g = re.findall("div align=(.*?)</div>",self.webhtml)
        #rmtext = "<div align="+g[4]+"</div>"
        #print rmtext
        
        self.webhtml = re.sub("EZikIT3", '123', web.text)
        #self.webhtml = re.sub("location", '1', self.webhtml)
        
        if self.webhtml.find("script") > 0:
            print "Get reload at ",self.webhtml.find("script")
            s = self.webhtml.find("script")
            print self.webhtml[s:s+100]
            
        else:
            print "Not find"
            
        #g1 = re.findall("<div align="+g[4]+"</div>",self.webhtml)
        #rmtext = g1
        
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
            print "Without HTML"
            self.web.load(QtCore.QUrl(url))    
        else:
            print "With HTML Revise"
            self.web.setHtml(self.webhtml,QtCore.QUrl(url))
            
        #self.web.show()

        #web signal
        #self.web.loadFinished.connect(self.cusHtml)
        
    def cusHtml(self, i, text):
        print "Load html"
        web = requests.get(self.url[i])
        #self.browser[i].load(QtCore.QUrl(self.url[i]))
        #frame = self.browser[i].page().mainFrame()
        #html=frame.toHtml()
        #raw_html = unicode(frame.toHtml()).encode('utf-8')
        
        html = re.sub(text, '123', web.text)
        #html = re.sub(text, '123', web.text)
        #web.text = re.sub("", '123', web.text)

        html = re.sub("rVa0MO3", "FUCK", html)
        self.browser[i].setHtml(html,QtCore.QUrl(self.url[i]))
        
def main():
    app = QtGui.QApplication(sys.argv) 

    F=Floxer()
    F.show()
    
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
    
    

