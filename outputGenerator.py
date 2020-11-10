#!/usr/bin/env python3

"""
Output Module
# TODO Add a function to export results to HTML
	  Add Graphs for other dicts too!
"""
from logaLyzer import LogLyzer, Data
from tabulate import tabulate
import csv
import os
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['figure.figsize'] = (11.7, 8.27)


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
        mast = []
        for i in self.log.objArray:
            mast.append({"IP": i, "GET": int(list(i.req.values())[0]), "RES200": i.res.get(
                "200", 0), "RES404": i.res.get("404", 0)})
        result_df = pd.DataFrame.from_dict(mast)
        date_df = pd.DataFrame.from_dict(LogLyzer.cumDate.items())
        hour = {}
        for i, j in LogLyzer.cumTms.items():
            for h, k in j.items():
                if h not in hour.keys():
                    hour[h] = k
            else:
                hour[h] += k
        hour_df = pd.DataFrame.from_dict(hour.items())

        sns.set_style('darkgrid')

        plt.figure(1)
        sns.barplot(x="IP", y="GET", data=result_df, palette='deep')
        plt.plot(result_df['GET'], 'go--')
        plt.xlabel("IP address")
        plt.ylabel("No.of Requests")
        plt.title("No.of Requests based on IP address")
        plt.xticks(rotation=75)
        plt.tight_layout(pad=2.5)

        plt.figure(2)
        sns.barplot(x=0, y=1, data=hour_df, palette='rocket')
        plt.xlabel("Hours")
        plt.ylabel("No.of Requests")
        plt.title("No.of Requests based on hours")
        plt.tight_layout(pad=2.5)

        plt.figure(3)
        sns.barplot(x=date_df[0], y=date_df[1], palette='vlag')
        plt.xlabel("Dates")
        plt.ylabel("No.of Requests")
        plt.title("No.of Requests based on Date")
        plt.xticks(rotation=75)
        plt.tight_layout(pad=2.5)

        fig, ax = plt.subplots()
        x = np.arange(len(result_df.index))
        bar_width = 0.4
        plt.figure(4)
        b1 = ax.bar(x, result_df['RES200'], width=bar_width, color='g')
        b2 = ax.bar(x + bar_width, result_df['RES404'], width=bar_width, color='r')
        ax.set_xticks([p - 0.1*bar_width for p in range(len(result_df.index))])
        ax.set_xticklabels(result_df['IP'])
        plt.xlabel("IP address")
        plt.ylabel("No.of Responses")
        plt.title("No.of Responses based on Response Type & IP address")
        plt.legend(["SUCCESS", "ERROR"])
        plt.xticks(rotation=75)
        plt.tight_layout(pad=2.5)
        plt.show()

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
        with open(filename, "w") as f:
            csv_w = csv.writer(f)
            csv_w.writerow(header)
            zipObj = zip(data.keys(), data.values())
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
        with open("output.html", "w") as f:
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
        dirName = time.asctime().replace(" ", "-").replace(":", "-")
        if(not os.path.isdir(dirName)):
            os.mkdir(dirName)
        os.chdir(dirName)
        self.writeToCsv("IP-and-Req.csv", self.log.cumIpReq, ["IP Address", "Req Count"])
        self.writeToCsv("Request-Method-and-Count.csv", self.log.cumReq,
                        ["Request Method", "Frequency"])
        self.writeToCsv("Response-Status-and-Count.csv",
                        self.log.cumRes, ["Status Code", "Frequency"])
        self.writeToCsv("UA-and-Count.csv", self.log.cumUA, ["User-Agent", "Frequency"])
        self.writeToCsv("File-Access-and-Count.csv", self.log.cumFile,
                        ["File Accessed", "Frequency"])
        self.writeToHTML()

    def prettyPrint(self):
        """
        This function pretty prints the data from Logalyzer module on Terminal.

    Returns
    -------
    None.

    """
        print("\n============== IP, Request Count =======================")
        print(tabulate(zip(self.log.cumIpReq.keys(), self.log.cumIpReq.values()),
                       headers=["IP", "Request Count"], tablefmt="fancy_grid"))
        print("\n============== Request Method, Count ===================")
        print(tabulate(zip(self.log.cumReq.keys(), self.log.cumReq.values()),
                       headers=["Request Method", "Count"], tablefmt="fancy_grid"))
        print("\n============== Status Code, Count ======================")
        print(tabulate(zip(self.log.cumRes.keys(), self.log.cumRes.values()),
                       headers=["Status Code", "Count"], tablefmt="fancy_grid"))
        print("\n============== User Agent, Count =======================")
        print(tabulate(zip(self.log.cumUA.keys(), self.log.cumUA.values()),
                       headers=["User Agent", "Count"], tablefmt="fancy_grid"))
        print("\n============== File Accessed, Count =====================")
        print(tabulate(zip(self.log.cumFile.keys(), self.log.cumFile.values()),
                       headers=["File Accessed", "Count"], tablefmt="fancy_grid"))
