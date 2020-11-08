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
		"""
		This function generates graphs based on the statistics presented from the
		logalyzer module

		Returns
	    -------
	    None.

	    """
		fig,ax = plt.subplots()
		ax.bar(self.log.ipReq.keys(), self.log.ipReq.values())
		plt.xticks(rotation=75)
		#fig.set_figheight(6)
		#fig.set_figwidth(5)
		fig.show()
		fig.tight_layout(pad=2.5)
	
	def genOutput(self):
		"""
        This function calls all other functions based on the output requested by
        the user.

        Returns
        -------
        None.

        """
		self.prettyPrint()
		self.gen_graph()
		self.exportOutput()
		self.log.freeMem()

    
	def writeToCsv(self, filename, data, header):
		"""
		This function writes the data from the logalyzer module to seperate CSV files
        
	    Parameters
	    ----------
	    filename : str
	        The name of the file to write.
	    data : dict
	        A dictionary of the data that is to be written to the CSV file.
	    header : list
	        The data that is to be written as the header of the CSV file.

	    Returns
	    -------
	    None.

	    """
		with open(filename,"w") as f:
			csv_w = csv.writer(f)
			csv_w.writerow(header)
			zipObj = zip(data.keys(),data.values())
			for row in zipObj:
				csv_w.writerow(list(row))
	
	
	def writeToHTML(self):
		"""
		This function writes the data from the Logalyzer module to a HTML file

	    Returns
	    -------
	    None.

	    """
		htmlPage = """
	<!DOCTYPE html>
	<html>
	<head>
	<title>
	Logalyzer - Results
	</title>
	</head>
	<body>
	<center>
	<i> <h3> IP Addresses and The Frequency </h3> </i>
	"""
		# Code to add rows
		htmlPage += """
	<i> <h3> Request Method and The Frequency </h3> </i>
	"""
		# Code to add rows
		htmlPage += """
	<i> <h3> Status Code and The Frequency </h3> </i>
	"""
		# Code to add rows
		htmlPage += """
	<i> <h3> User Agent and The Frequency </h3> </i>
	"""
		# Code to add rows
		htmlPage += """
	<i> <h3> Accessed File and The Frequency </h3> </i>
	"""
		# Code to add rows
		htmlPage += """
	</center>
	</body>
	</html>
	"""
		with open("output.html","w") as f:
			f.write(htmlPage)
		
		
	
	def exportOutput(self):
		"""
		This function creates a directory based on timestamp and calls other functions to
        write data from Logalyzer module to HTML and CSV files.

	    Returns
	    -------
	    None.

	    """
	    # Replacing : with - to make the Folder name Windows Compatible
		dirName = time.asctime().replace(" ","-").replace(":","-")
		if(not os.path.isdir(dirName)):
			os.mkdir(dirName)
		os.chdir(dirName)
		self.writeToCsv("IP-and-Req.csv", self.log.cumIpReq, ["IP Address", "Req Count"])
		self.writeToCsv("Request-Method-and-Count.csv",self.log.cumReq, ["Request Method","Frequency"])
		self.writeToCsv("Response-Status-and-Count.csv", self.log.cumRes, ["Status Code", "Frequency"])
		self.writeToCsv("UA-and-Count.csv",self.log.cumUA, ["User-Agent","Frequency"])
		self.writeToCsv("File-Access-and-Count.csv", self.log.cumFile, ["File Accessed", "Frequency"])
		self.writeToHTML()
	

	def prettyPrint(self):
		"""
		This function pretty prints the data from Logalyzer module on Terminal.

	    Returns
	    -------
	    None.

	    """
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
