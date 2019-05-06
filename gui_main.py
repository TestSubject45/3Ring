print(" Loading GUI elements and pages")
import sys
sys.path.append('gui/')
from gui_dashboard import *
from noun_template import *
from config import *



class MainWindow(QMainWindow):
	global nounList

	def __init__(self):
		super().__init__()
		global nounList
		# for item in nounList:
		# 	nounList[item][] = ""

		window = QWidget()
		self.resize(1500,700)
		self.move(150,150)
		self.setCentralWidget(window)
		self.stack = QStackedLayout()
		window.setLayout(stack)

		self.InitNouns() 
		self.InitMenu()
		importPages(self)

	def InitNouns(self):	
		dashboard = Dashboard()
		characters = Noun("Characters")
		items = Noun("Items")
		locations = Noun("Locations")
		concepts = Noun("Concepts")

		stack.addWidget(dashboard)
		stack.addWidget(characters)
		stack.addWidget(items)
		stack.addWidget(locations)
		stack.addWidget(concepts)

		self.show()
		changeNoun(self,0)

	def InitMenu(self):
		global stack
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('File')
		editMenu = mainMenu.addMenu('Edit')
		viewMenu = mainMenu.addMenu('View')
		toolsMenu = mainMenu.addMenu('Tools')
		nounsMenu = mainMenu.addMenu('Nouns')

		importButton = QAction(QIcon('exit24.png'),"Import",self)
		importButton.triggered.connect(lambda: importPages(self))
		fileMenu.addAction(importButton)

		exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
		exitButton.triggered.connect(self.close)
		fileMenu.addAction(exitButton)

		dashboardButton = QAction(QIcon('exit24.png'),nounList[0],self)
		dashboardButton.triggered.connect(lambda: changeNoun(self,0))
		nounsMenu.addAction(dashboardButton)

		charactersButton = QAction(QIcon('exit24.png'),nounList[1],self)
		charactersButton.triggered.connect(lambda: changeNoun(self,1))
		nounsMenu.addAction(charactersButton)

		itemsButton = QAction(QIcon('exit24.png'),nounList[2],self)
		itemsButton.triggered.connect(lambda: changeNoun(self,2))
		nounsMenu.addAction(itemsButton)

		locationsButton = QAction(QIcon('exit24.png'),nounList[3],self)
		locationsButton.triggered.connect(lambda: changeNoun(self,3))
		nounsMenu.addAction(locationsButton)

		conceptsButton = QAction(QIcon('exit24.png'),nounList[4],self)
		conceptsButton.triggered.connect(lambda: changeNoun(self,4))
		nounsMenu.addAction(conceptsButton)


		# eventsButton = QAction(QIcon('exit24.png'),nounList[5],self)
		# eventsButton.triggered.connect(lambda: changeNoun(self,5))
		# nounsMenu.addAction(eventsButton)

print(" Finished loading GUI")