import gtk
#import webkit

def main():
    print "Gadget Start !!!"
    print "Using GTK"

    '''==================
        Show Window
    =================='''
    win=gtk.Window()
    win.connect("delete-event", gtk.main_quit) #kill thread
    win.show_all()
    gtk.main()

    '''==================
    =================='''
    

if __name__=="__main__":
    main()
