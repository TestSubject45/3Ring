from gui import *


app = wx.App()
myFrame = mainFrame(None,title='Hello World!')
myFrame.Show()

app.MainLoop()