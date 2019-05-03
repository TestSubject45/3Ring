print("  Loading Noun Template")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
sys.path.append('..')
from funcs import *


class Noun(QWidget):


    def __init__(self,title):
        super().__init__()

        self.setWindowTitle(title)
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
        page_name = QLabel()
        page_name.setText('<p style="font-size:28px;">Hek</p>')
        page_name.setAlignment(Qt.AlignCenter)
        page_name.resize(50,50)

        # world_heading = QLabel(self)
        # world_heading.setText('<p style="font-size:36px;font-family:cursive;">Racen</p>')
        # world_heading.setAlignment(Qt.AlignCenter)
        
        textBox = QTextEdit(self)
        textBox.resize(20,40)

        featured_pic = QLabel()
        featured_pic.setPixmap(QPixmap("resources/150.png"))
        featured_pic.setAlignment(Qt.AlignCenter)

        page_widget = QListWidget()
        page_widget.setMaximumSize(250,600)
        page_widget.addItem("Help")

        dashboardButton = QPushButton("Dashboard",self)
        dashboardButton.resize(15,15)
##        dashboardButton.clicked.connect(self.changePage(0))

        #Add widgets to grid
        grid.addWidget(page_name,1,1,1,1)
        grid.addWidget(page_widget,2,1,2,1)
        grid.addWidget(featured_pic,4,1,2,1)
        #grid.addWidget(world_heading,1,2,1,3)
        grid.addWidget(textBox,1,2,5,3)
        grid.addWidget(dashboardButton,0,1,1,1)
        