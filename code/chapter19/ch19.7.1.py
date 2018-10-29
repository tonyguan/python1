# coding=utf-8
# 代码文件：chapter19/ch19.7.1.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='分隔窗口', size=(350, 180))
        self.Centre()  # 设置窗口居中

        splitter = wx.SplitterWindow(self, -1)
        leftpanel = wx.Panel(splitter)
        rightpanel = wx.Panel(splitter)
        splitter.SplitVertically(leftpanel, rightpanel, 100)
        splitter.SetMinimumPaneSize(80)

        list2 = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(leftpanel, -1, choices=list2, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox, lb2)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(lb2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        leftpanel.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(rightpanel, label='右侧面板')
        vbox2.Add(self.content, 1, flag=wx.ALL | wx.EXPAND, border=5)
        rightpanel.SetSizer(vbox2)

    def on_listbox(self, event):
        s = '选择 {0}'.format(event.GetString())
        self.content.SetLabel(s)


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
