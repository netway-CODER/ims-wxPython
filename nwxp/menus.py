"""
Use wx.MenuItem to create item to menu:
1. qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        2. qmi.SetBitmap(wx.Bitmap('exit.png'))
        3. self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        """
import wx
import wx.adv


class MainMenu(wx.MenuBar):
    def __init__(self, parent, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.parent = parent
        self.initMenu()

    def initMenu(self):
        # file menu:
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()
        # submenu import menu:
        importMenu = wx.Menu()
        importMenu.Append(wx.ID_ANY, 'Import bookmarks...')
        importMenu.Append(wx.ID_ANY, 'Import list...')
        importMenu.Append(wx.ID_ANY, 'Import email...')
        fileMenu.Append(wx.ID_ANY, 'I&mport...', importMenu)

        # export submenu:
        exportMenu = wx.Menu()
        exportMenu.Append(wx.ID_ANY, 'Export bookmarks...')
        exportMenu.Append(wx.ID_ANY, 'Export list...')
        exportMenu.Append(wx.ID_ANY, 'Export email...')
        fileMenu.Append(wx.ID_ANY, 'Export...', exportMenu)
        fileMenu.AppendSeparator()
        quitFileItem = fileMenu.Append(wx.ID_EXIT, '&Quit', 'Quit Application')
        self.Bind(wx.EVT_MENU, self.onQuit, quitFileItem)
        self.Append(fileMenu, '&File')

        # help menu:
        helpMenu = wx.Menu()
        aboutHelpItem = helpMenu.Append(wx.ID_ABOUT, '&About', 'About the Application')
        self.Bind(wx.EVT_MENU, self.onAbout, aboutHelpItem)
        self.Append(helpMenu, '&Help')

    def onAbout(self, e):
        description = """ N/A """
        licence = """ N/A """

        info = wx.adv.AboutDialogInfo()

        info.SetIcon(wx.Icon('images/icon_adb.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Netway Computer Inventory Manager')
        info.SetVersion('1.0.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2007 - 2024 Michael Chen')
        info.SetWebSite('http://www.zetcode.com')
        info.SetLicence(licence)
        info.AddDeveloper("Michael Chen")
        info.AddDocWriter('Michael Chen')
        info.AddArtist('Peggy Li')
        info.AddTranslator('Michael Chen')
        wx.adv.AboutBox(info)

    def onQuit(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.parent.Close()
        else:
            e.Veto()