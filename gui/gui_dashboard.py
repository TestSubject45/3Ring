print("  Loading Dashboard")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonList = ['Characters','Items','Locations','Concepts','Events','','','']
        #I is the number of rows, J is the number or columns
        self.positionList = [(1,1),(1,2),(1,3),(1,4)]


        self.InitUI() 

    def InitUI(self):

        #Create grid
        grid = QGridLayout()
        grid.setColumnMinimumWidth(0,50)
        grid.setRowMinimumHeight(0,50)
        self.setLayout(grid)

        #create widgets
        map_Viewer = QLabel()
        map_Viewer.setPixmap(QPixmap("resources/defaultMap.jpeg"))
        map_Viewer.setAlignment(Qt.AlignCenter)
        world_heading = QLabel(self)
        world_heading.setText('<p style="font-size:36px;font-family:cursive;">Racen</p>')
        world_heading.setAlignment(Qt.AlignCenter)
        newEntryBox = QTextEdit(self)
        newEntryBox.resize(500,200)
        submitButton = QPushButton("Submit")


        #Loop through list and add buttons to grid
        for position, name in zip(self.positionList, self.buttonList):
            if(name)=='':
                continue
            button = QPushButton(name)

            grid.addWidget(button,*position)

        #Add widgets to grid
        grid.addWidget(map_Viewer,1,7,4,5)
        grid.addWidget(world_heading,1,7,1,5)
        grid.addWidget(newEntryBox,4,1,2,5)
        grid.addWidget(submitButton,6,5,1,1)
        