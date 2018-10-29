# coding=utf-8
# 代码文件：chapter19/ch19.3.2-3.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="第一个GUI程序!", size=(400, 300))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(parent=self)
        statictext = wx.StaticText(parent=panel, label='Hello World!', pos=(10, 10))


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
