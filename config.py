print("Loading config file")
from PyQt5.QtWidgets import *
global stack
stack = QStackedLayout()
global nounList
nounList = ['Dashboard','Characters','Items','Locations','Concepts']
global pagesList
pagesList = [
	["Dashboard"],
	["Characters",],
	["Items",],
	["Locations"],
	["Concepts"],
	["Events"],
]

print("Finished loading config file")