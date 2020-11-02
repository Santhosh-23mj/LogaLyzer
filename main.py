#!/usr/bin/env python3

"""
Main Function #Driving Code
"""

import logaLyzer as ll
import outputGenerator as og
import frontEndGUI as fg

log   = ll.LogLyzer()
graph = og.outputGenerator(log)
gui   = fg.GuiDesign(log, graph)

gui.launchApp()
