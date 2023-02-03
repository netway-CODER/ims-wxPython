import wx
from mainWindow import MainWindow


def main():
    app = wx.App()
    window = MainWindow(None)
    window.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/