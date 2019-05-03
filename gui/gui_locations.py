print("  Loading Locations")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Locations(QWidget):
    def __init__(self):
        super().__init__()
        
        self.InitUI() 

    def InitUI(self):

        #Create grid
        grid = QGridLayout()
        grid.setColumnMinimumWidth(0,15)
        grid.setRowMinimumHeight(0,15)
        grid.setColumnMinimumWidth(5,15)
        grid.setRowMinimumHeight(6,15)
        self.setLayout(grid)

        #create widgets
        location_name = QLabel()
        location_name.setText('<p style="font-size:28px;">Gateswatch</p>')
        location_name.setAlignment(Qt.AlignCenter)
        location_name.resize(50,50)

        # world_heading = QLabel(self)
        # world_heading.setText('<p style="font-size:36px;font-family:cursive;">Racen</p>')
        # world_heading.setAlignment(Qt.AlignCenter)
        
        textBox = QTextEdit(self)
        textBox.resize(20,40)

        map_pic = QLabel()
        map_pic.setPixmap(QPixmap("resources/150.png"))
        map_pic.setAlignment(Qt.AlignCenter)

        list_widget = QListWidget()
        list_widget.setMaximumSize(250,600)
        list_widget.addItem("Help")

        #Add widgets to grid
        grid.addWidget(location_name,1,1,1,1)
        grid.addWidget(list_widget,2,1,2,1)
        grid.addWidget(map_pic,4,1,2,1)
        #grid.addWidget(world_heading,1,2,1,3)
        grid.addWidget(textBox,1,2,5,3)
        