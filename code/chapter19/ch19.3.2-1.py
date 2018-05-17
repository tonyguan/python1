# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter19/ch19.3.2-1.py

import wx

# 创建应用程序对象
app = wx.App()
# 创建窗口对象
frm = wx.Frame(None, title="第一个GUI程序!", size=(400, 300), pos=(100, 100))

frm.Show()  # 显示窗口

app.MainLoop()  # 进入主事件循环
