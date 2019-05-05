print("Loading config file")
from PyQt5.QtWidgets import *
global stack
stack = QStackedLayout()
global nounList
nounList = ['Dashboard','Characters','Items','Locations','Concepts']
global pagesList
pagesList = [
	["Dashboard"],
	["Characters","Aziel","Frankfurt"],
	["Items","ROd of sun","ROd of Son","Rod, son of dave"],
	["Locations","GatesWatch"],
	["Concepts"],
	["Events"],
]

print("Finished loading config file")