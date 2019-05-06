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
        global pagesList
        
        self.page_name.setText('<p style="font-size:28px;">'+str(self.page_widget.currentItem().text())+'</p>')

        pageWidgetCount = self.page_widget.count()
        pageListCount = len(pagesList[findNounIndex(self.name)])
        #refresh page list
        # print(self.name)
        # print("Page Widget Count "+str(pageWidgetCount))
        # print("Page List Count "+str(pageListCount))
        # print()

        if(pageWidgetCount!=pageListCount):
            loadPagesIntoList(self,True)    


    def readPage(self,pageName):
        pageContent = readFromFile("data/"+self.name+"/"+pageName,"txt")

        self.text_box.clear()

        for item in pageContent:
            self.text_box.insertPlainText(item)

        self.refresh()


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
        grid.setColumnMinimumWidth(1,150)        
        grid.setRowMinimumHeight(0,15)
        grid.setColumnMinimumWidth(5,15)
        grid.setRowMinimumHeight(6,15)
        self.setLayout(grid)

        #create widgets
        self.page_widget = QListWidget()
        self.page_widget.setMaximumSize(250,600)
        self.page_widget.addItem("placeholder")
        self.page_widget.setCurrentRow(0)
        self.page_widget.itemActivated.connect(lambda: self.readPage(self.page_widget.currentItem().text()))

        self.page_name = QLabel()
        self.page_name.setText('<p style="font-size:28px;">'+str(self.page_widget.currentItem())+'</p>')
        self.page_name.setAlignment(Qt.AlignCenter)
        self.page_name.resize(50,50)

        self.page_title = QLineEdit()

        # world_heading = QLabel(self)
        # world_heading.setText('<p style="font-size:36px;font-family:cursive;">Racen</p>')
        # world_heading.setAlignment(Qt.AlignCenter)
        
        self.text_box = QTextEdit(self)
        self.text_box.acceptRichText()
        self.text_box.resize(20,40)

        featured_pic = QLabel()
        featured_pic.setPixmap(QPixmap("resources/150.png"))
        featured_pic.setAlignment(Qt.AlignCenter)

        dashboardButton = QPushButton("Refresh",self)
        dashboardButton.resize(15,15)
        dashboardButton.clicked.connect(lambda: self.refresh())

        saveButton = QPushButton("Save",self)
        saveButton.resize(5,15)
        saveButton.clicked.connect(lambda: writeToFile(str("data/"+self.name+"/"+self.page_widget.currentItem().text()),"txt",self.text_box.toPlainText()))

        #Add widgets to grid
        grid.addWidget(self.page_name,1,1,1,1)
        grid.addWidget(self.page_widget,2,1,2,1)
        grid.addWidget(featured_pic,4,1,2,1)
        #grid.addWidget(world_heading,1,2,1,3)
        grid.addWidget(self.text_box,1,2,5,3)
        grid.addWidget(dashboardButton,0,1,1,1)
        grid.addWidget(saveButton,6,4,1,1)
        