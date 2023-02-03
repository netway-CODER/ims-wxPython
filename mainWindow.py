import wx

from nwxp.dialogs import *
from nwxp.menus import *
from nwxp.toolbars import MainToolbar


class MainWindow(wx.Frame):

    def __init__(self, parent, *args, **kwargs):
        super(MainWindow, self).__init__(parent, *args, **kwargs)
        self.initUI()
        self.SetTitle('Netway Computer Application')
        self.SetSize((800, 600))
        self.SetBackgroundColour('gray')
        self.Center()

    def initUI(self):

        # add menu
        mMenu = MainMenu(self)
        self.SetMenuBar(mMenu)

        # toolbar
        tb = MainToolbar(self, style=wx.TB_VERTICAL)
        self.SetToolBar(tb)

        # main panel:
        panel = wx.Panel(self)
        #panel.SetBackgroundColour('#4f5049')

        # main layout:
        vBox = wx.BoxSizer(wx.VERTICAL)

        btn1 = wx.Button(panel, label="Button 1", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnBtn1Click, btn1)
        btn2 = wx.Button(panel, label="Button 2", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onBtn2Click, id=btn2.GetId())
        btn3 = wx.Button(panel, label="Button 3", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onBtn3Click, id=btn3.GetId())
        # another style to create a button
        btn4 = wx.Button(panel, wx.ID_ANY, 'Exit', (70, 30))
        self.Bind(wx.EVT_BUTTON, self.onQuit, id=btn4.GetId())

        vBox.Add(btn1, border=10)
        vBox.Add(btn2, border=10)
        vBox.Add(btn3, border=10)
        vBox.Add(btn4, border=10)
        panel.SetSizer(vBox)

    def OnBtn1Click(self, e):
        nWindow = wx.Frame(None, title='btn1 was clicked')
        nWindow.Show()

    def onBtn2Click(self, e):
        dial = AbsDialog(None)
        dial.ShowModal()

    def onBtn3Click(self, e):
        with LoginDialog(self) as dial:
            if dial.ShowModal() == wx.ID_OK:
                print('the dialog was open successfully!')

    def onQuit(self, e):
        self.Close(True)

    def empOnClicked(self):
        wx.MessageBox('working', 'info', wx.OK|wx.ICON_INFORMATION)