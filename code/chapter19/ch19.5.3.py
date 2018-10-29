# coding=utf-8
# 代码文件：chapter19/ch19.5.3.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Grid布局', size=(300, 300))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, label='1')
        btn2 = wx.Button(panel, label='2')
        btn3 = wx.Button(panel, label='3')
        btn4 = wx.Button(panel, label='4')
        btn5 = wx.Button(panel, label='5')
        btn6 = wx.Button(panel, label='6')
        btn7 = wx.Button(panel, label='7')
        btn8 = wx.Button(panel, label='8')
        btn9 = wx.Button(panel, label='9')

        grid = wx.GridSizer(cols=3, rows=3, vgap=0, hgap=0)

        # grid.AddMany([
        #     (btn1, 0, wx.EXPAND),
        #     (btn2, 0, wx.EXPAND),
        #     (btn3, 0, wx.EXPAND),
        #     (btn4, 0, wx.EXPAND),
        #     (btn5, 0, wx.EXPAND),
        #     (btn6, 0, wx.EXPAND),
        #     (btn7, 0, wx.EXPAND),
        #     (btn8, 0, wx.EXPAND),
        #     (btn9, 0, wx.EXPAND)
        # ])

        grid.Add(btn1, 0, wx.EXPAND)
        grid.Add(btn2, 0, wx.EXPAND)
        grid.Add(btn3, 0, wx.EXPAND)
        grid.Add(btn4, 0, wx.EXPAND)
        grid.Add(btn5, 0, wx.EXPAND)
        grid.Add(btn6, 0, wx.EXPAND)
        grid.Add(btn7, 0, wx.EXPAND)
        grid.Add(btn8, 0, wx.EXPAND)
        grid.Add(btn9, 0, wx.EXPAND)

        panel.SetSizer(grid)


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
