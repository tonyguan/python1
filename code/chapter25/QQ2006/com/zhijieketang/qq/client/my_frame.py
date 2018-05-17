# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter25/QQ2006/com/zhijieketang/qq/client/my_frame.py

"""定义Frame窗口基类"""
import logging
import socket
import sys

import wx

logger = logging.getLogger(__name__)

# 服务器端IP
SERVER_IP = '127.0.0.1'
# 服务器端端口号
SERVER_PORT = 8888

# 服务器地址
server_address = (SERVER_IP, SERVER_PORT)

# 操作命令代码
COMMAND_LOGIN = 1  # 登录命令
COMMAND_LOGOUT = 2  # 下线命令
COMMAND_SENDMSG = 3  # 发消息命令
COMMAND_REFRESH = 4  # 刷新好友列表命令

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置超时1秒，不再等待接收数据
client_socket.settimeout(1)


class MyFrame(wx.Frame):
    
    def __init__(self, title, size):
        super().__init__(parent=None, title=title, size=size,
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)
        # 设置窗口居中
        self.Centre()
        # 设置Frame窗口内容面板
        self.contentpanel = wx.Panel(parent=self)

        ico = wx.Icon('resources/icon/qq.ico', wx.BITMAP_TYPE_ICO)
        # 设置窗口图标
        self.SetIcon(ico)
        # 设置窗口的最大和最小尺寸
        self.SetSizeHints(size, size)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        # 退出系统
        self.Destroy()
        client_socket.close()
        sys.exit(0)
