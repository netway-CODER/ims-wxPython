# Create custom dialog here.
import sqlite3
import wx
import settings


class UserDetail(wx.Dialog):
    def __init__(self, parent):
        super(UserDetail, self).__init__(parent)
        self.parent = parent
        self.initUI()
        self.SetTitle("Registration Step 2")
        self.CenterOnParent()

    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # user last name field:
        lastname_sizer = wx.BoxSizer(wx.HORIZONTAL)
        lastname_label = wx.StaticText(self, label="Last Name:")
        lastname_sizer.Add(lastname_label, 0, wx.ALL | wx.CENTER, 5)
        self.last_name = wx.TextCtrl(self)
        lastname_sizer.Add(self.last_name, 0, wx.ALL, 5)
        sizer.Add(lastname_sizer)

        self.SetSizer(sizer)


class Register(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(register, self).__init__(*args, **kwargs)
        self.parent = args[0]
        self.initUI()
        self.SetTitle("register")
        self.CenterOnParent()

    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # username field
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_label = wx.StaticText(self, label='* User Name:')
        user_sizer.Add(user_label, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        self.user.SetFocus()
        user_sizer.Add(self.user, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(user_sizer, 0, wx.ALL, 5)

        # password field
        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)  # buttons
        pwd_label = wx.StaticText(self, label='* Password:')
        self.pwd = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        pwd_sizer.Add(pwd_label, 0, wx.ALL | wx.CENTER, 5)
        pwd_sizer.Add(self.pwd, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(pwd_sizer, 0, wx.ALL, 5)

        # confirm password field:
        pwd_cfm_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pwd_cfm_label = wx.StaticText(self, label='* Confirm Password:')
        self.pwd_cfm = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        pwd_cfm_sizer.Add(pwd_cfm_label, 0, wx.ALL | wx.Center, 5)
        pwd_cfm_sizer.Add(self.pwd_cfm, 0, wx.ALL | wx.Center, 5)
        sizer.Add(pwd_cfm_sizer, 0, wx.ALL, 5)

        # email field:
        email_sizer = wx.BoxSizer(wx.HORIZONTAL)
        email_label = wx.StaticText(self, label="* Email:")
        email_sizer.Add(email_label, 0, wx.ALL, 5)
        self.email = wx.TextCtrl(self)
        email_sizer.Add(self.email, 0, wx.ALL, 5)
        sizer.Add(email_sizer)

        # buttons:
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        next_button = wx.Button(self, label="Next")
        cancel_button = wx.Button(self, label="Cancel")
        button_box.Add(next_button, 0, wx.ALL, 5)
        button_box.Add(cancel_button, 0, wx.ALL, 5)
        sizer.Add(button_box, 1, wx.ALL, 10)

        self.SetSizer(sizer)

        next_button.Bind(wx.EVT_BUTTON, self.onNext)
        cancel_button.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnClose(self, e):
        self.Destroy()

    def onNext(self, e):
        pass


# login dialog
class LoginDialog(wx.Dialog):
    def __init__(self, *parent):
        super(LoginDialog, self).__init__(*parent)
        self.parent = parent
        self.initUI()
        self.SetTitle('Sign-In')
        self.CenterOnParent()

    def initUI(self):
        # pnl = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # username field
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_label = wx.StaticText(self, label='User Name:')
        user_sizer.Add(user_label, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        self.user.SetFocus()
        user_sizer.Add(self.user, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(user_sizer, 0, wx.ALL, 5)

        # password field
        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)  # buttons
        pwd_label = wx.StaticText(self, label='Password:')
        pwd_sizer.Add(pwd_label, 0, wx.ALL | wx.CENTER, 5)
        self.pwd = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        pwd_sizer.Add(self.pwd, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(pwd_sizer, 0, wx.ALL, 5)

        """ register
        register_box = wx.BoxSizer(wx.HORIZONTAL)
        register_label = wx.StaticText(self, label="Not a user?")
        register_box.Add(register_label, 0, wx.ALL, 5)
        register_button = wx.Button(self, label="Sign Up")
        register_box.Add(register_button, 0, wx.ALL | wx.RIGHT, 5)
        sizer.Add(register_box, 1, wx.ALL, 5)
        """

        # buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        login_button = wx.Button(self, label='Sign In')
        cancel_button = wx.Button(self, label='Cancel')
        hbox.Add(login_button, 0, wx.ALL, 5)
        hbox.Add(cancel_button, 0, wx.ALL, 5)
        sizer.Add(hbox, 1, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)

        # register_button.Bind(wx.EVT_BUTTON, self.OnRegist)
        login_button.Bind(wx.EVT_BUTTON, self.onLogin)
        cancel_button.Bind(wx.EVT_BUTTON, self.onCancel)

    def onLogin(self, e):
        db = sqlite3.connect(settings.DATABASE_FILE_NAME)
        result = None
        user = self.user.GetValue()
        if user is not None:
            # print(user)
            try:
                result = db.execute("SELECT password FROM users WHERE user_name = '{}' LIMIT 1;".format(user)).fetchall()
                if result is not []:
                    current_pwd = result[0][0]
                    # print("current_pwd: {}".format(current_pwd))
            except Exception as e:
                print("Error: {}".format(e))
                current_pwd = None
            db.close()
        pwd = self.pwd.GetValue()
        if pwd is not None:
            # print(pwd)
            if pwd == current_pwd:
                settings.CURRENT_USER = user
                self.EndModal(True)
            else:
                wx.MessageBox("Login with {} was False!\nUser is not exists or wrong password.\nPlease try again!".format(user), 'ERROR', wx.OK | wx.ICON_ERROR)
                self.pwd.SetFocus()

    def onCancel(self, e):
        self.EndModal(False)

    def OnRegist(self, e):
        reg = register(self)
        reg.Show()