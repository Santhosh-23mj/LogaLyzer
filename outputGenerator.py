#!/usr/bin/env python3

"""
Output Module
#TODO Add a function to export results to HTML
	  Add Graphs for other dicts too!
"""
import csv
import os
import time
import matplotlib.pyplot as plt
from tabulate import tabulate
#plt.rcParams["figure.figsize"] = [4,6]

class outputGenerator:
	
	def __init__(self, logObj):
		self.log = logObj
	
	def gen_graph(self):
		self.prettyPrint()
		fig,ax = plt.subplots()
		ax.bar(self.log.ipReq.keys(), self.log.ipReq.values())
		plt.xticks(rotation=75)
		#fig.set_figheight(6)
		#fig.set_figwidth(5)
		fig.show()
		fig.tight_layout(pad=2.5)
		#self.exportOutput()
		self.log.freeMem()
	
	def writeToCsv(self, filename, data, header):
		with open(filename,"w") as f:
			csv_w = csv.writer(f)
			csv_w.writerow(header)
			zipObj = zip(data.keys(),data.values())
			for row in zipObj:
				csv_w.writerow(list(row))
	
	def exportOutput(self):
		dirName = time.asctime().replace(" ","-")
		if(not os.path.isdir(dirName)):
			os.mkdir(dirName)
		os.chdir(dirName)
		self.writeToCsv("IP-and-Req", self.log.cumIpReq, ["IP Address", "Req Count"])
		self.writeToCsv("Request-Method-and-Count",self.log.cumReq, ["Request Method","Frequency"])
		self.writeToCsv("Response-Status-and-Count", self.log.cumRes, ["Status Code", "Frequency"])
		self.writeToCsv("UA-and-Count",self.log.cumUA, ["User-Agent","Frequency"])
		self.writeToCsv("File-Access-and-Count", self.log.cumFile, ["File Accessed", "Frequency"])
	

	def prettyPrint(self):
		print("\n============== IP, Request Count =======================")
		print(tabulate(zip(self.log.cumIpReq.keys(), self.log.cumIpReq.values()), headers=["IP", "Request Count"], tablefmt="fancy_grid"))
		print("\n============== Request Method, Count ===================")
		print(tabulate(zip(self.log.cumReq.keys(),self.log.cumReq.values()), headers=["Request Method", "Count"], tablefmt="fancy_grid"))
		print("\n============== Status Code, Count ======================")
		print(tabulate(zip(self.log.cumRes.keys(), self.log.cumRes.values()), headers=["Status Code", "Count"], tablefmt="fancy_grid"))
		print("\n============== User Agent, Count =======================")
		print(tabulate(zip(self.log.cumUA.keys(),self.log.cumUA.values()), headers=["User Agent", "Count"], tablefmt="fancy_grid"))
		print("\n============== File Accessed, Count =====================")
		print(tabulate(zip(self.log.cumFile.keys(), self.log.cumFile.values()), headers=["File Accessed", "Count"], tablefmt="fancy_grid"))
