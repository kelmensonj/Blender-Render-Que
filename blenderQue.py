import os
from tkinter import *
from pathlib import Path


def render(list_box):
	list_box_get = list_box.get(0,END)
	for file_str in list_box_get:
		os.system('blender -b ' + file_str + ' -a')

def clearCanvas():
	global CANVAS
	CANVAS.destroy()
	CANVAS = Canvas(APP)
	CANVAS.pack()
	
def delete(list_box):
	sel = list_box.curselection()
	for index in sel[::-1]:
		list_box.delete(index)
	
def homeReset():
	global CANVAS
	clearCanvas()
	listbox = Listbox(CANVAS)
	listbox.config(width=60, height=15)
	listbox.pack()
	scrollbar = Scrollbar(CANVAS)  
	scrollbar.pack(side = RIGHT, fill = BOTH) 
	listbox.config(yscrollcommand = scrollbar.set) 
	scrollbar.config(command = listbox.yview) 
	blend_files = [pth for pth in Path.cwd().iterdir() if pth.suffix == '.blend']
	for blend in blend_files:
		listbox.insert(END, str(blend).split('/')[-1])
	delete_btn = Button(CANVAS, text = 'Delete Selection', command=lambda: delete(listbox))
	delete_btn.pack()
	top = Button(CANVAS, text='Render', command=lambda: render(listbox))
	top.pack()
	bot = Button(CANVAS, text='Clear All', command=homeReset)
	bot.pack()

APP = Tk()
CANVAS = Canvas(APP)
CANVAS.pack()
APP.title('Blender List Render')
APP.geometry('700x1200')
MENUBAR = Menu(APP)
MENUBAR.add_command(label="Home", command=homeReset)
APP.config(menu=MENUBAR)
homeReset()
APP.mainloop()
