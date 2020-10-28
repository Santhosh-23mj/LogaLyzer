#!/usr/bin/env python3

"""
Output Module
"""
import matplotlib.pyplot as plt

class GraphGenerator:
	
	def __init__(self, logObj):
		self.log = logObj
	
	def gen_graph(self):
		fig,ax = plt.subplots()
		ax.bar(self.log.ipReq.keys(), self.log.ipReq.values())
		fig.show()
