# coding=utf-8
# 代码文件：chapter19/ch19.6.6.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态图片控件', size=(300, 300))
        self.bmps = [wx.Bitmap('images/bird5.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird4.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird3.gif', wx.BITMAP_TYPE_GIF)]

        self.Centre()  # 设置窗口居中
        self.panel = wx.Panel(parent=self)
        # 创建垂直方向的Box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        b1 = wx.Button(parent=self.panel, id=1, label='Button1')
        b2 = wx.Button(self.panel, id=2, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)

        self.image = wx.StaticBitmap(self.panel, -1, self.bmps[0])

        # 添加标控件到Box布局管理器
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.CENTER)

        self.panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])
        self.panel.Layout()


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
