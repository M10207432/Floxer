import gtk
#import webkit

class Floxer(gtk.Window):
    def __init__(self,win):
        
        win.set_decorated(False)                    #hide title bar
        win.connect("delete-event", gtk.main_quit)  #kill thread
        win.set_opacity(0.5)                        #set win opacity [0:1]

        win.add_events(gtk.gdk.POINTER_MOTION_MASK )            #set event mask
        win.connect('motion_notify_event',self.motion_cb)       #set signal to function

        self.win=win
        win.show_all()
        gtk.main()

    def move(self,x,y):
        pass

    def motion_cb(self,window,event):

        if event.state & gtk.gdk.BUTTON1_MASK:        #Press state in motion situation
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
