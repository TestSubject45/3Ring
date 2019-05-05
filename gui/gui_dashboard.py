print("  Loading Dashboard")
import sys
sys.path.append('..')
from config import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from funcs import *



class Dashboard(QWidget):

    def refresh(self):
        x = 1

    def newPageHelper(self):
        content = self.newEntryBox.toPlainText()
        title = self.newPageTitle.text()
        noun = self.comboBox.currentText()
        print(noun)
        newPage(self,content,title,noun)

    def __init__(self):
        super().__init__()
        self.name = "Dashboard"

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
        self.newEntryBox = QTextEdit(self)
        self.newEntryBox.resize(500,200)
        self.newPageTitle = QLineEdit(self)
        submitButton = QPushButton("Submit")
        submitButton.clicked.connect(lambda: self.newPageHelper())
        self.comboBox = QComboBox(self)

        for item in nounList[1:len(nounList)]:
            self.comboBox.addItem(item)

        #Add widgets to grid
        grid.addWidget(map_Viewer,1,7,4,5)
        grid.addWidget(world_heading,1,7,1,5)
        grid.addWidget(self.comboBox,3,1,1,1)
        grid.addWidget(self.newPageTitle,4,1,1,2)
        grid.addWidget(self.newEntryBox,5,1,2,5)
        grid.addWidget(submitButton,7,5,1,1)
        