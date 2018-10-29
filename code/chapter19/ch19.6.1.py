# coding=utf-8
# 代码文件：chapter19/ch19.6.1.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态文本和按钮', size=(300, 200))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(parent=self)
        # 创建垂直方向的Box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.statictext = wx.StaticText(parent=panel, label='StaticText1', style=wx.ALIGN_CENTRE_HORIZONTAL)
        b1 = wx.Button(parent=panel, label='OK')
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)

        b2 = wx.ToggleButton(panel, -1, 'ToggleButton')
        self.Bind(wx.EVT_BUTTON, self.on_click, b2)

        bmp = wx.Bitmap('icon/1.png', wx.BITMAP_TYPE_PNG)
        b3 = wx.BitmapButton(panel, -1, bmp)
        self.Bind(wx.EVT_BUTTON, self.on_click, b3)

        # 添加静态文本和按钮到Box布局管理器
        vbox.Add(100, 10, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b3, proportion=1, flag=wx.CENTER | wx.EXPAND)

        panel.SetSizer(vbox)

    def on_click(self, event):
        self.statictext.SetLabelText('Hello, world.')


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
