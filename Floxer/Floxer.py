import gtk
#import webkit

class Floxer(gtk.Window):
    def __init__(self,win):
        
        win.set_decorated(False)                    #hide title bar
        win.connect("delete-event", gtk.main_quit)  #kill thread
        win.set_opacity(0.5)                        #set win opacity [0:1]

        win.show_all()
        gtk.main()

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
