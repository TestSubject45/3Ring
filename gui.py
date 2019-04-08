import wx
from funcs import *

class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent,title=title,size=(500,300))

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
        button = wx.Button(panel,wx.ID_ANY,'TEST',(50,150))
        
        self.textbox = wx.TextCtrl(panel,size=(200,100),style=wx.TE_MULTILINE)

        button.Bind(wx.EVT_BUTTON,self.onButton)

        self.InitMenu()

    def onButton(self,event):
        inpt = self.textbox.GetValue()
        print(inpt)
        
    def OnQuit(self,event):
        print("EX")
        self.Close()
        exit()

print("GUI Loaded")