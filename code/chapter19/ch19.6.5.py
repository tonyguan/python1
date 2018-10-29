# coding=utf-8
# 代码文件：chapter19/ch19.6.5.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='下拉列表', size=(350, 180))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(self)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择你喜欢的编程语言：')

        list1 = ['Python', 'C++', 'Java']
        lb1 = wx.ListBox(panel, -1, choices=list1, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox1, lb1)

        hbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox1.Add(lb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择你喜欢吃的水果：')
        list2 = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(panel, -1, choices=list2, style=wx.LB_EXTENDED)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox2, lb2)

        hbox2.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox2.Add(lb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(vbox)

    def on_listbox1(self, event):
        listbox = event.GetEventObject()
        print('选择 {0}'.format(listbox.GetSelection()))

    def on_listbox2(self, event):
        listbox = event.GetEventObject()
        print('选择 {0}'.format(listbox.GetSelections()))


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
