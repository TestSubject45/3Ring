print("  Loading Dashboard")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonList = ['Characters','Items','Locations','Concepts','Events','','','']
        #I is the number of rows, J is the number or columns
        self.positionList = [(i,j) for i in range (10) for j in range(4)]


        self.InitUI()
#        self.InitMenu()
 

    def InitUI(self):

        #make window and name it
        self.setGeometry(150,150,1500,700)
        self.setWindowTitle("Dashboard")

        #Create grid
        grid = QGridLayout()
        self.setLayout(grid)

        #create widgets
        map_Viewer = QLabel()
        map_Viewer.setPixmap(QPixmap("resources/defaultMap.jpeg"))


        #Loop through list and add buttons to grid
        for position, name in zip(self.positionList, self.buttonList):
            if(name)=='':
                continue
            button = QPushButton(name)

            grid.addWidget(button,*position)

        #Add widgets to grid
        grid.addWidget(map_Viewer,0,7,4,5)

        self.show()

    # def InitMenu(self):
    #     #Menu Headings
    #     mainMenu = self.menuBar()
    #     fileMenu = mainMenu.addMenu('File')
    #     editMenu = mainMenu.addMenu('Edit')
    #     viewMenu = mainMenu.addMenu('View')
    #     toolMenu = mainMenu.addMenu('Tools')

    #     #Menu Buttons
    #     exitButton = QAction(QIcon('exit24.png'),'Exit',self)
    #     exitButton.triggered.connect(self.close)
    #     fileMenu.addAction(exitButton)