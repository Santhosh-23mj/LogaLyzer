#!/usr/bin/python3

"""
Main Function #Driving Code
"""

import logaLyzer as ll
import graphGenerator as gg
import frontEndGUI as fg

log   = ll.LogLyzer()
graph = gg.GraphGenerator(log)
gui   = fg.GuiDesign(log, graph)

gui.launchApp()
