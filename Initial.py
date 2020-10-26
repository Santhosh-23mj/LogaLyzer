#!/usr/bin/env python3

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

class Data:
    def __init__(self, ip):
        self.ip   = ip
        self.req  = {}
        self.res  = {}
        self.UA   = []
        self.file = {}
        self.tms  = {}
    
    def __repr__(self):
        return self.ip
        
class LogLyzer:
    
    objArray = []
    ipList   = []
    f = None
    ipReq = {}

    def gen_graph(self):
        fig,ax = plt.subplots()
        ax.bar(self.ipReq.keys(), self.ipReq.values())
        fig.show()

    def graphGen_command():
        fig.show()
    
    def open_file(self):
        f = filedialog.askopenfile(mode='r')
        self.readFile(f)
        
        for obj in self.objArray:
            print(obj.ip)
            print(obj.req)
            self.ipReq[obj.ip] = sum(list(obj.req.values()))
            print(obj.res)
            print(obj.UA)
            print(obj.file)
            print(obj.tms)
            print("\n")
        
    def readFile(self, f):
        while True:
            line = f.readline().replace("\"","").strip()
            if(not line):
                break
            else:
                temp = line.split()
                if( temp[0] not in self.ipList ):
                    self.ipList.append(temp[0])
                    obj = Data(temp[0])
                    obj.req[temp[5]] = obj.req.get(temp[5],0) + 1
                    obj.res[temp[8]] = obj.res.get(temp[8],0) + 1
                    obj.file[temp[6]] = obj.file.get(temp[6],0) + 1
                    obj.UA.append(' '.join(temp[11:]))
                    obj.tms[temp[3].replace("[","")] = obj.tms.get(temp[3].replace("[",""),0) + 1
                    self.objArray.append(obj)
                else:
                    index = self.ipList.index(temp[0])
                    self.objArray[index].req[temp[5]] = self.objArray[index].req.get(temp[5], 0) + 1
                    self.objArray[index].res[temp[8]] = self.objArray[index].res.get(temp[8], 0) + 1
                    self.objArray[index].file[temp[6]] = self.objArray[index].file.get(temp[6], 0) + 1
                    if( ' '.join(temp[11:]) not in self.objArray[index].UA ):
                        self.objArray[index].UA.append(' '.join(temp[11:]))
                    self.objArray[index].tms[temp[3].replace("[","")] = self.objArray[index].tms.get(temp[3].replace("[",""), 0) + 1


def main():

    fileName = []
    log = LogLyzer()

    window = tk.Tk()  # Starting tkinter window
    window.title('Welcome!')  # Setting window title
    window.configure(bg='#293d3d')
    label_head = tk.Label(window, text='LogaLyzer', width=15, underline=4, padx=8, pady=8, borderwidth=10, highlightthickness=3, anchor='center', relief='ridge', fg='#003d66', bg='#80ccff', font=('Russo One', 20)).grid(row=0,column=0, padx=20, pady=25, columnspan=3)  # Displaying heading label
    label_getfile = tk.Label(window, text='Kindly choose the log file:', font=('verdana', 9, 'bold'),fg='#ffffff', bg='#293d3d', anchor='w').grid(row=1,column=0, padx=15)

    fileNameSetButton = tk.Button(window, text='Choose File', font=("Open Sans", 9, "bold"), borderwidth=5, bg='#b3e0ff', command=lambda: log.open_file(), cursor='hand2', padx=5, pady=5, anchor='w').grid(row=1, column=1, padx=5, pady=0)  # Setting the filename to variable

    label_getfile = tk.Label(window, text='Click for the results:', font=('verdana', 9, 'bold'),fg='#ffffff', bg='#293d3d', anchor='w').grid(row=2,column=0, padx=15)
    graphGenButton = tk.Button(window, text='Generate Graph', font=("Open Sans", 9, "bold"), borderwidth=5, bg='#b3e0ff', command=log.gen_graph, cursor='rtl_logo', padx=5, pady=5).grid(row=2, column=1, padx=20, pady=20)
    
    window.mainloop()

main()
