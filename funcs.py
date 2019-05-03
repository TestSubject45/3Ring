print(" Loading functions...")

def changePage(self,index,nounList,stack):
	stack.setCurrentIndex(index)
	self.setWindowTitle(nounList[index])
	print(index)
	print("Changing to",nounList[index])

def writeToFile(filename,filetype,content):
	file = open(filename+'.'+filetype,"w")

	file.write(content)
	file.close()



print(" Functions Loaded")