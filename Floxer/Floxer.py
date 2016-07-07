import gtk
#import webkit

class Floxer(gtk.Window):
    def __init__(self,win):
        
        win.set_decorated(False)                    #hide title bar
        win.connect("delete-event", gtk.main_quit)  #kill thread
        win.set_opacity(1)                          #set win opacity [0:1]
        
        win.add_events(gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_PRESS_MASK)     #set event mask
        win.connect('motion_notify_event',self.motion_cb)                           #set mouse motion to callback function
        win.connect('button_press_event',self.click_cb)                             #set mouse click to callback function

        self.drag_flag=True
        
        self.win=win
        win.show_all()
        gtk.main()

    def click_cb(self,window,event):
        if event.button==1 & self.drag_flag:
            self.win.begin_move_drag(event.button, int(event.x_root),int(event.y_root),event.time) #Drag Function

    def motion_cb(self,window,event):
        print event.x, event.y
        
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
