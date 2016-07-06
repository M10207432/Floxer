import gtk
#import webkit

class Floxer(gtk.Window):
    def __init__(self,win):
        
        win.set_decorated(False)                    #hide title bar
        win.connect("delete-event", gtk.main_quit)  #kill thread
        win.set_opacity(0.5)                        #set win opacity [0:1]

        win.add_events(gtk.gdk.BUTTON_PRESS_MASK)   #set mouse event
        win.connect('button-press-event',self.mouse_callback)
        
        
        win.show_all()
        gtk.main()


    def move(self,x,y):
        pass

    def mouse_callback(self,window,event):
        print "x=", event.x, "y=", event.y
        
def main():
    print "Gadget Start !!!"

    '''==================
        Show Window
    =================='''
    win=gtk.Window()
    F=Floxer(win)

    
    '''==================
    =================='''
    

if __name__=="__main__":
    main()
