# coding=utf-8
# 代码文件：chapter19/ch19.6.4.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='下拉列表', size=(400, 130))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(self)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择你喜欢的编程语言：')

        list1 = ['Python', 'C++', 'Java']
        ch1 = wx.ComboBox(panel, -1, value='C', choices=list1, style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, ch1)

        hbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox1.Add(ch1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择性别：')
        list2 = ['男', '女']
        ch2 = wx.Choice(panel, -1, choices=list2)
        self.Bind(wx.EVT_CHOICE, self.on_choice, ch2)

        hbox2.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox2.Add(ch2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(vbox)

    def on_combobox(self, event):
        print('选择 {0}'.format(event.GetString()))

    def on_choice(self, event):
        print('选择 {0}'.format(event.GetString()))


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
