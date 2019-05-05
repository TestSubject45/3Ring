print("  Loading Noun Template")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from config import *
sys.path.append('..')
from funcs import *


class Noun(QWidget):

    def refresh(self):

        self.page_name.setText('<p style="font-size:28px;">'+str(self.page_widget.currentItem().text())+'</p>')

    def __init__(self,title):
        super().__init__()
        self.name = title

        self.setWindowTitle(title)
        self.InitUI() 
        loadPagesIntoList(self)
        self.refresh()

    def InitUI(self):

        #Create grid
        grid = QGridLayout()
        grid.setColumnMinimumWidth(0,15)
        grid.setRowMinimumHeight(0,15)
        grid.setColumnMinimumWidth(5,15)
        grid.setRowMinimumHeight(6,15)
        self.setLayout(grid)

        #create widgets
        self.page_widget = QListWidget()
        self.page_widget.setMaximumSize(250,600)
        self.page_widget.addItem("halp")
        self.page_widget.setCurrentRow(0)

        self.page_name = QLabel()
        self.page_name.setText('<p style="font-size:28px;">'+str(self.page_widget.currentItem())+'</p>')
        self.page_name.setAlignment(Qt.AlignCenter)
        self.page_name.resize(50,50)

        # world_heading = QLabel(self)
        # world_heading.setText('<p style="font-size:36px;font-family:cursive;">Racen</p>')
        # world_heading.setAlignment(Qt.AlignCenter)
        
        text_box = QTextEdit(self)
        text_box.resize(20,40)

        featured_pic = QLabel()
        featured_pic.setPixmap(QPixmap("resources/150.png"))
        featured_pic.setAlignment(Qt.AlignCenter)

        dashboardButton = QPushButton("Refresh",self)
        dashboardButton.resize(15,15)
        dashboardButton.clicked.connect(lambda: self.refresh())

        #Add widgets to grid
        grid.addWidget(self.page_name,1,1,1,1)
        grid.addWidget(self.page_widget,2,1,2,1)
        grid.addWidget(featured_pic,4,1,2,1)
        #grid.addWidget(world_heading,1,2,1,3)
        grid.addWidget(text_box,1,2,5,3)
        grid.addWidget(dashboardButton,0,1,1,1)