print(" Loading GUI elements and pages")
import sys
sys.path.append('gui/')
from gui_dashboard import *
from gui_characters import *


class MainWindow(QMainWindow):


	def changePage(self,index):
		self.stack.setCurrentIndex(index)
		print("Changing to " + index)

	def __init__(self):
		super().__init__()
		window = QWidget()
		self.resize(1500,700)
		self.move(150,150)
		self.setCentralWidget(window)
		self.stack = QStackedLayout()
		window.setLayout(self.stack)

		self.InitPages() 
		self.InitMenu()

	def InitPages(self):
		dashboard = Dashboard()
		characters = Characters()

		self.stack.addWidget(dashboard)
		self.stack.addWidget(characters)

		self.show()

	def InitMenu(self):
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('File')
		editMenu = mainMenu.addMenu('Edit')
		viewMenu = mainMenu.addMenu('View')
		searchMenu = mainMenu.addMenu('Search')
		toolsMenu = mainMenu.addMenu('Tools')
		pagesMenu = mainMenu.addMenu('Pages')

		charactersButton = QAction(QIcon('exit24.png'), 'Characters', self)
		charactersButton.triggered.connect(lambda: self.changePage(1))
		pagesMenu.addAction(charactersButton)


print(" Finished loading GUI elements and pages too")