import wx
from funcs import *

class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent,title=title,size=(1500,800))

        self.InitUI()

    def InitMenu(self):
        print("Initializing Menu...")
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT,'Quit','Quit Application')
        menubar.Append(fileMenu,'&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.OnQuit,exitItem)
        print("Finshed")

    def InitUI(self):

        panel = wx.Panel(self,wx.ID_ANY)
        button = wx.Button(panel,wx.ID_ANY,'TEST',(10,10))
        button.Bind(wx.EVT_BUTTON,self.onButton)

        self.InitMenu()

    def onButton(self,e):
        print("Button Clicked")
        
    def OnQuit(self,e):
        print("EX")
        self.Close()
        exit()

print("GUI Loaded")