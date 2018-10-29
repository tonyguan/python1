# coding=utf-8
# 代码文件：chapter19/ch19.3.2-1.py

import wx

# 创建应用程序对象
app = wx.App()
# 创建窗口对象
frm = wx.Frame(None, title="第一个GUI程序!", size=(400, 300), pos=(100, 100))

frm.Show()  # 显示窗口

app.MainLoop()  # 进入主事件循环
