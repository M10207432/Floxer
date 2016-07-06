import gtk
#import webkit

class Floxer(gtk.Window):
    def __init__(self,win):
        #win=gtk.Window()
        win.set_decorated(False)                    #hide title bar
        win.connect("delete-event", gtk.main_quit)  #kill thread
        win.show_all()
        gtk.main()

def main():
    print "Gadget Start !!!"
    print "Using GTK"

    '''==================
        Show Window
    =================='''

    '''
    win=gtk.Window()
    win.set_decorated(False)                    #hide title bar
    win.connect("delete-event", gtk.main_quit)  #kill thread
    win.show_all()
    gtk.main()
    '''
    win=gtk.Window()
    F=Floxer(win)

    
    '''==================
    =================='''
    

if __name__=="__main__":
    main()
