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

        #Create Panel and sizers
        panel = wx.Panel(self,wx.ID_ANY)
        MainSizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        LeftSizer = wx.BoxSizer(orient=wx.VERTICAL)
        homeButtonSizer = wx.GridSizer(4,4,10,20)

        
        #Initialize Buttons
        SubmitButton = wx.Button(panel,wx.ID_ANY,'Submit',(10,50))

        button1 = wx.Button(panel,wx.ID_ANY,'TEMP1',(30,50))
        button2 = wx.Button(panel,wx.ID_ANY,'TEMP2',(30,50))
        button3 = wx.Button(panel,wx.ID_ANY,'TEMP3',(30,50))
        button4 = wx.Button(panel,wx.ID_ANY,'TEMP4',(30,50))
        button5 = wx.Button(panel,wx.ID_ANY,'TEMP5',(30,50))
        button6 = wx.Button(panel,wx.ID_ANY,'TEMP6',(30,50))
        button7 = wx.Button(panel,wx.ID_ANY,'TEMP7',(30,50))
        button8 = wx.Button(panel,wx.ID_ANY,'TEMP8',(30,50))



        #initialize textbox and bind button to it
        self.textbox = wx.TextCtrl(panel,size=(600,200),style=wx.TE_MULTILINE)
        SubmitButton.Bind(wx.EVT_BUTTON,self.onButton)

        #Add objects to sizers
        homeButtonSizer.Add(button1,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button2,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button3,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button4,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button5,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button6,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button7,1,wx.FIXED_MINSIZE,10)
        homeButtonSizer.Add(button8,1,wx.FIXED_MINSIZE,10)


        LeftSizer.AddSpacer(50)
        LeftSizer.Add(homeButtonSizer,1,wx.EXPAND,10)
        LeftSizer.Add(self.textbox,0,wx.FIXED_MINSIZE,10)
        LeftSizer.Add(SubmitButton,0,wx.ALL|wx.FIXED_MINSIZE,10)

        MainSizer.AddSpacer(50)
        MainSizer.Add(LeftSizer,1,wx.EXPAND,10)
        MainSizer.AddSpacer(800)





        panel.SetSizer(MainSizer)
        #Call other function to init menu
        self.InitMenu()

    def onButton(self,event):
        inpt = self.textbox.GetValue()
        print(inpt)
        
    def OnQuit(self,event):
        print("EX")
        self.Close()
        exit()

print("GUI Loaded")