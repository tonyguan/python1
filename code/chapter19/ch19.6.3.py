# coding=utf-8
# 代码文件：chapter19/ch19.6.3.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='复选框和单选按钮', size=(400, 130))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(self)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择你喜欢的编程语言：')
        cb1 = wx.CheckBox(panel, 1, 'Python')
        cb2 = wx.CheckBox(panel, 2, 'Java')
        cb2.SetValue(True)
        cb3 = wx.CheckBox(panel, 3, 'C++')
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1, id2=3)

        hbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox1.Add(cb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(cb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(cb3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择性别：')
        radio1 = wx.RadioButton(panel, 4, '男', style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, 5, '女')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio1_click, id=4, id2=5)

        hbox2.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox2.Add(radio1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox2.Add(radio2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择你最喜欢吃的水果：')
        radio3 = wx.RadioButton(panel, 6, '苹果', style=wx.RB_GROUP)
        radio4 = wx.RadioButton(panel, 7, '橘子')
        radio5 = wx.RadioButton(panel, 8, '香蕉')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio2_click, id=6, id2=8)

        hbox3.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox3.Add(radio3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3.Add(radio4, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3.Add(radio5, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox3, 1, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(vbox)

    def on_checkbox_click(self, event):
        cb = event.GetEventObject()
        print('选择 {0}，状态{1}'.format(cb.GetLabel(), event.IsChecked()))

    def on_radio1_click(self, event):
        rb = event.GetEventObject()
        print('第一组 {0} 被选中'.format(rb.GetLabel()))

    def on_radio2_click(self, event):
        rb = event.GetEventObject()
        print('第二组 {0} 被选中'.format(rb.GetLabel()))

class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
