print("Loading functions...")
from config import *
import csv
import glob


def changeNoun(self,index):
	global nounList

	stack.setCurrentIndex(index)
	self.setWindowTitle(nounList[index])
	stack.currentWidget().refresh()
	print("Changing to",nounList[index])

def findNounIndex(noun):
	global nounList

	return nounList.index(noun)

def writeToFile(filename,filetype,content):
	filename = filename+'.'+filetype
	print("Writing "+filename)
	with open(filename,"w+") as file:
		if(filetype=="txt"):
			file.write(content)
			file.close()
		elif(filetype=="csv"):
			writer = csv.writer(file,delimiter=",")
			writer.writerows(pagesList)

def readFromFile(filename,filetype):
	filename = filename+"."+filetype
	if(filetype=="csv"):
		with open(filename,'rt') as f:
			reader = csv.reader(f,delimiter=",")
			output = list(reader)
	elif(filetype=="txt"):
		with open(filename) as f:
			output = f.readlines()

	return output

def newPage(self,content,title,noun):
	global pagesList
	try:
		path = "data/"+noun+"/"+title
		pagesList[findNounIndex(noun)].append(title)

		writeToFile(path,"txt",content)
		writeToFile("data/pagesList","csv",pagesList)
		changeNoun(self,findNounIndex(noun))

	except FileNotFoundError as e:
		print(e)

def loadPagesFromFile():
	global pagesList
	try:
		pagesList = readFromFile("data/pagesList","csv")
	except FileNotFoundError as e:
		writeToFile("data/pagesList","csv",pagesList)

def loadPagesIntoList(self,refresh=False):
	global pagesList

	for noun in pagesList:
		if(noun[0]==self.name):
			pages = noun

	if(refresh==True):
		for i in range(0,self.page_widget.count()):
			trash = self.page_widget.takeItem(0)
			trash = None

	for page in pages:
		self.page_widget.addItem(page)
	i = 0
	if(refresh==True):
		while(i<=0):
			trash = self.page_widget.takeItem(0)
			trash = None
			i = i + 1
	if(refresh==False):
		while(i<=1):
			trash = self.page_widget.takeItem(0)
			trash = None
			i = i + 1

	if(self.page_widget.count()<1):
		self.page_widget.addItem("Untitled Page")

	self.page_widget.setCurrentRow(0)

def importPages(self):
	global nounList
	global pagesList

	for item in nounList:
		fileList = glob.glob("data/"+item+"/*.txt")
		for page in fileList:
			page = page.split('/')[2][0:len(page.split('/')[2])-4]
			pagesList[findNounIndex(item)].append(page)
			# print(page.split('/')[2][0:len(page.split('/')[2])-4])
	
loadPagesFromFile()
print("Functions Loaded")

