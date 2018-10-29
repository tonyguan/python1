# coding=utf-8
# 代码文件：chapter19/ch19.5.2.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='StaticBox布局', size=(300, 120))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(parent=self)
        # 创建垂直方向的Box布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='Button1单击')
        # 添加静态文本到Box布局管理器
        vbox.Add(self.statictext, proportion=2, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=10)

        b1 = wx.Button(parent=panel, id=10, label='Button1')
        b2 = wx.Button(parent=panel, id=11, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

        # 创建静态框对象
        sb = wx.StaticBox(panel, label="按钮框")
        # 创建水平方向的StaticBox布局管理器
        hsbox = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        # 添加b1到水平StaticBox布局管理
        hsbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 添加b2到水平StaticBox布局管理
        hsbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        # 添加hbox到vbox
        vbox.Add(hsbox, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
