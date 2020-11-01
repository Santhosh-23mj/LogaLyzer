#!/usr/bin/env python3

"""
Output Module
"""
import matplotlib.pyplot as plt
#plt.rcParams["figure.figsize"] = [4,6]

class GraphGenerator:
	
	def __init__(self, logObj):
		self.log = logObj
	
	def gen_graph(self):
		fig,ax = plt.subplots()
		ax.bar(self.log.ipReq.keys(), self.log.ipReq.values())
		plt.xticks(rotation=75)
		#fig.set_figheight(6)
		#fig.set_figwidth(5)
		fig.show()
		fig.tight_layout(pad=2.5)
