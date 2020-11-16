APP = Tk() #Creating tkinter Tk object, this is what will run the mainloop
CANVAS = Canvas(APP) #Creating Canvas object. I use this to easily refresh the Tk object and create new UI within the same window
CANVAS.pack() #Adding the Canvas to the Tk object 'APP'
APP.title('Blender List Render') #Setting window title
APP.geometry('700x1200') #Setting window size
MENUBAR = Menu(APP) #Creating menubar object
MENUBAR.add_command(label="Home", command=homeReset) #Adding 'Home' button to menubar. The home button calls function 'homeReset'
APP.config(menu=MENUBAR)
homeReset()
APP.mainloop()

#####^GUI^########
