import wx

class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title,size=(1500, 800))

        self.InitUI()


    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT,'Quit','Quit Application')
        menubar.Append(fileMenu,'&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU,self.OnQuit,exitItem)

        nounBox = wx.BoxSizer(wx.HORIZONTAL)

        self.display = wx.TextCtrl(self,style=wx.TE_RIGHT)
        nounBox.Add(self.display,flag=wx.EXPAND|wx.TOP|wx.BOTTOM,border=4)

    def OnQuit(self,e):
        self.Close()

print("GUI Loaded")