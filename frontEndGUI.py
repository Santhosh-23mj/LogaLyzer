#!/usr/bin/env python3

"""
FrontEnd Module
"""

import tkinter as tk

class GuiDesign:
	
	def __init__(self, logObj, graphObj):
		self.log = logObj
		self.op  = graphObj
	
	def launchApp(self):
		window = tk.Tk()  # Starting tkinter window
		window.title('Welcome!')  # Setting window title
		window.configure(bg='#293d3d')
		label_head = tk.Label(window, text='LogaLyzer', width=15, underline=4, padx=8, pady=8, borderwidth=10, highlightthickness=3, anchor='center', relief='ridge', fg='#003d66', bg='#80ccff', font=('Russo One', 20)).grid(row=0,column=0, padx=20, pady=25, columnspan=3)  # Displaying heading label
		label_getfile = tk.Label(window, text='Kindly choose the log file:', font=('verdana', 9, 'bold'),fg='#ffffff', bg='#293d3d', anchor='w').grid(row=1,column=0, padx=15)

		fileNameSetButton = tk.Button(window, text='Choose File', font=("Open Sans", 9, "bold"), borderwidth=5, bg='#b3e0ff', command=lambda: self.log.open_file(), cursor='hand2', padx=5, pady=5, anchor='w').grid(row=1, column=1, padx=5, pady=0)  # Setting the filename to variable

		label_getfile = tk.Label(window, text='Click for the results:', font=('verdana', 9, 'bold'),fg='#ffffff', bg='#293d3d', anchor='w').grid(row=2,column=0, padx=15)
		graphGenButton = tk.Button(window, text='Generate Graph', font=("Open Sans", 9, "bold"), borderwidth=5, bg='#b3e0ff', command=self.op.gen_graph, cursor='rtl_logo', padx=5, pady=5).grid(row=2, column=1, padx=20, pady=20)
		self.log.objArray.clear()
		self.log.ipList.clear()
    
		window.mainloop()
