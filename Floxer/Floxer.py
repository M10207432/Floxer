import gtk
#import cairo
from math import pi
#import webkit

'''
def transparent_expose(widget, event):
    cr = widget.window.cairo_create()
    cr.set_operator(cairo.OPERATOR_CLEAR)
    region = gtk.gdk.region_rectangle(event.area)
    cr.region(region)
    cr.fill()
    return False
'''

def draw_pixbuf(widget, event):
    path = 'Iron.png'
    pixbuf = gtk.gdk.pixbuf_new_from_file(path)
    widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,5)
 

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
        self.win.modify_bg(self.gtk.STATE_NORMAL, self.gtk.gdk.Color(0, 65535, 0))

        self.win.set_size_request(400,400)

        hbbox = gtk.HButtonBox()
        win.add(hbbox)
        hbbox.connect('expose-event', draw_pixbuf)

        '''
        screen=self.win.get_screen()
        rgba=screen.get_rgba_colormap()
        if rgba ==None:
            rgba=screen.get_rgb_colormap()
        self.win.set_colormap(rgba)
        self.win.connect("expose-event", transparent_expose)
        '''
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
        #self.Set_Widget()       #Widget Function
  
        #=================Start
        self.win.show_all()
        self.gtk.main()

    def Set_Widget(self):
        #=====Image
        
        img=self.gtk.Image()
        img.set_from_file("BayMax.png")
        self.win.add(img)
        
        pass
        

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
