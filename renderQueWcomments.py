import os
from tkinter import *
from pathlib import Path

##########^Imports^#########################


def render(list_box): #The function 'render()' is easily the most important in this project. Everything else is just queing up '.blend' files
	list_box_get = list_box.get(0,END) #the tkinter 'get()' function is used here to return a list of all values in 'list_box'
	for file_str in list_box_get:
		os.system('blender -b ' + file_str + ' -a') #the 'os' module lets me access command line. This is one of many powerful blender command line statements
                                                #The Blender Foundation has ample documentation. You could alter this line here and do interesting stuff
                                                #while referencing each blend file in 'list_box_get'
        
 #################^render()^###########################3

def clearCanvas():
	global CANVAS
	CANVAS.destroy() #Just using the tkinter 'destroy()' method to destroy the current 'global CANVAS' object
	CANVAS = Canvas(APP) #Then creating a new 'global CANVAS' object that is the tkinter 'Canvas' object. 'APP' is the tkinter 'Tk()' object in the GUI
	CANVAS.pack()
  
###################^clearCanvas()^################
	
def delete(list_box):
	sel = list_box.curselection() #Here I use the tkinter listbox method 'curselection()'
	for index in sel[::-1]: #This references all selected items in 'sel', stepping backwards from the list item. Fancy
		list_box.delete(index) #Poor naming on my part. 'delete' is used here to reference the tkinter 'delete' method. Different from function 'delete()'
    
###################^delete()^################
	
def homeReset():
	global CANVAS #It says 'global CANVAS' here for clarity. TODO: refactor all my project code into Classes
	clearCanvas() #Calling 'clearCanvas()'
	listbox = Listbox(CANVAS) #Creating tkinter Listbox object withing 'CANVAS'
	listbox.config(width=60, height=15) #Setting listbox parameters'
	listbox.pack() 
	scrollbar = Scrollbar(CANVAS)  
	scrollbar.pack(side = RIGHT, fill = BOTH) 
	listbox.config(yscrollcommand = scrollbar.set) 
	scrollbar.config(command = listbox.yview) #Next I add a scrollbar, and set the command parameter
	blend_files = [pth for pth in Path.cwd().iterdir() if pth.suffix == '.blend'] #List comprehension that finds all '.blend' files in current directory
	for blend in blend_files:
		listbox.insert(END, str(blend).split('/')[-1]) #Inserting each '.blend' file into the listbox, some cleanup. If you're on windows switch the slash
	delete_btn = Button(CANVAS, text = 'Delete Selection', command=lambda: delete(listbox)) #Adding a tkinter 'Button' object to 'CANVAS. 
                                                                                          #On click delete button will pass the entire listbox object
                                                                                          #into the function 'delete()'
	delete_btn.pack()
	top = Button(CANVAS, text='Render', command=lambda: render(listbox)) #Another 'Button' object. Passes listbox into 'render()' function
	top.pack()
	bot = Button(CANVAS, text='Clear All', command=homeReset) #This 'Button' will simply call function 'homeReset()' in order to clear the listbox
	bot.pack()
 
########^homeReset()^################


APP = Tk() #Creating tkinter Tk object, this is what will run the mainloop
CANVAS = Canvas(APP) #Creating Canvas object. I use this to easily refresh the Tk object and create new UI within the same window
CANVAS.pack() #Adding the Canvas to the Tk object 'APP'
APP.title('Blender List Render') #Setting window title
APP.geometry('700x1200') #Setting window size
MENUBAR = Menu(APP) #Creating menubar object
MENUBAR.add_command(label="Home", command=homeReset) #Adding 'Home' button to menubar. The home button calls function 'homeReset'
APP.config(menu=MENUBAR) #Adding 'MENUBAR' to 'APP'
homeReset() #Calling the function 'homeReset'
APP.mainloop() #Calling 'APP' mainloop

#####^GUI^########
