import numpy as np
import cv2
import requests
from sseclient import SSEClient
from selenium import webdriver

"""==========================
    Get XHR(XmlHttpRequest)
    =>The data obj trnasfer from
    wenserver to webbrowser
    =>This object is providing by
    JavaScript
    => The "AJAX" technique is
    generate the XHR object
=========================="""
def Request_Web():
    url = "https://tv.line.me/v/1581122_%E9%85%B8%E7%94%9C%E4%B9%8B%E5%91%B3-ep4-1"
    
    driver = webdriver.PhantomJS(executable_path =
                                 "./element_install/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver.get(url)
    driver.implicitly_wait(3)
    
    pageSource = driver.page_source
    print pageSource
    driver.close()
    
    
    
def TSplayer():
    print "Transport Stream"

    videofile = "./element_install/v3.mp4"

    cap = cv2.VideoCapture(videofile)
    lev_cnt = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        try:
            cv2.imshow('frame', frame)
        except:
            lev_cnt += 1
            print lev_cnt
        if lev_cnt > 2:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
    
def main():
    #TSplayer()
    Request_Web()
    
    
if __name__ == "__main__":
    main()
