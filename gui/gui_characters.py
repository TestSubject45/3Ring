print("  Loading Characters")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Characters(QWidget):
    def __init__(self):
        super().__init__()

        self.InitUI() 

    def InitUI(self):

        #make main widget and name it
#        self.setGeometry(150,150,1500,700)
        self.setWindowTitle("Characters")

        #Create grid
        grid = QGridLayout()
        grid.setColumnMinimumWidth(0,50)
        grid.setRowMinimumHeight(0,50)
        self.setLayout(grid)

        #create widgets
        testLabel = QLabel("FUCK YEAH")
        testLabel.setAlignment(Qt.AlignCenter)

        #Add widgets to grid
        grid.addWidget(testLabel,1,1,2,5)
