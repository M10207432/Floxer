import gtk
#import webkit

class Floxer(gtk.Window):
    def __init__(self,win):

        '''--------------------
            Variable
        --------------------'''
        self.win=win
        self.gtk=gtk
        
        '''--------------------
            Setting
        --------------------'''
        self.drag_flag=True             #Drag Windows flag
        self.win.set_decorated(False)   #hide title bar
        self.win.set_opacity(0.5)       #set win opacity [0:1]

        '''--------------------
            Event Callback
        --------------------'''
        self.win.add_events(self.gtk.gdk.POINTER_MOTION_MASK | self.gtk.gdk.BUTTON_PRESS_MASK)     #set event mask
        self.win.connect('motion_notify_event',self.motion_cb)              #set mouse motion to callback function
        self.win.connect('button_press_event',self.click_cb)                #set mouse click to callback function
        self.win.connect("delete-event", self.gtk.main_quit)                #kill thread event
        
        '''--------------------
            Function
        --------------------'''
        self.Set_Widget()       #Widget Function

        #=================Start
        self.win.show_all()
        self.gtk.main()

    def Set_Widget(self):
        #=====Image
        img=self.gtk.Image()
        img.set_from_file("fire.png")
        self.win.add(img)


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
