#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messb

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
	
    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello, everyone.')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text = 'Hello', command = self.hello)
        self.quitButton.pack()
		
    def hello(self):
        name = self.nameInput.get() or 'everyOne'
        messb.showinfo('Message', "hello %s" % name)		
		
app = Application()
app.master.title("Hello")
app.mainloop()