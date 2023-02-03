"""
Create custom dialog here.
The AbsDialog is the source code copy from tutorial, need to modify later.
"""
import wx


class AbsDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(AbsDialog, self).__init__(*args, **kwargs)
        self.initUI()
        self.SetSize((250, 200))
        self.SetTitle("Custom Dialog")
        self.Center()

    def initUI(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Display a group of RadioButton:
        sb = wx.StaticBox(pnl, label='Colors')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(pnl, label='256 Colors',
                               style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(pnl, label='16 Colors'))
        sbs.Add(wx.RadioButton(pnl, label='2 Colors'))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(pnl, label='Custom'))
        hbox1.Add(wx.TextCtrl(pnl), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1,
                 flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnClose(self, e):
        self.Destroy()


# login dialog
class LoginDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)
        self.initUI()
        self.SetTitle('User Login')
        self.CenterOnParent()

    def initUI(self):
        pnl = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # username field
        userSzr = wx.BoxSizer(wx.HORIZONTAL)
        userLbl = wx.StaticText(self, label='User Name:')
        userSzr.Add(userLbl, 0, wx.ALL|wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        self.user.SetFocus()
        userSzr.Add(self.user, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(userSzr, 0, wx.ALL, 5)

        # password field
        pwdSzr = wx.BoxSizer(wx.HORIZONTAL)        # buttons
        pwdLbl = wx.StaticText(self, label='Password:')
        pwdSzr.Add(pwdLbl, 0, wx.ALL|wx.CENTER, 5)
        self.pwd = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        pwdSzr.Add(self.pwd, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(pwdSzr, 0, wx.ALL, 5)

        # buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        loginButton = wx.Button(self, label='Login')
        cancelButton = wx.Button(self, label='Cancel')
        hbox.Add(loginButton, 0, wx.ALL, 5)
        hbox.Add(cancelButton, 0, wx.ALL, 5)
        sizer.Add(hbox, 1, wx.ALL|wx.CENTER, 10)

        self.SetSizer(sizer)

        loginButton.Bind(wx.EVT_BUTTON, self.onLogin)
        cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)

    def onLogin(self, e):
        pass

    def onCancel(self, e):
        self.Destroy()