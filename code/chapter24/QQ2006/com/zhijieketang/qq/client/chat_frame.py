# coding=utf-8
# 代码文件：chapter24/QQ2006/com/zhijieketang/qq/client/chat_frame.py

"""好友聊天窗口"""

import datetime
import json
import threading

from com.zhijieketang.qq.client.my_frame import *


class ChatFrame(MyFrame):
    def __init__(self, friendsframe, user, friend):
        super().__init__(title='', size=(450, 400))

        self.friendsframe = friendsframe

        self.user = user
        self.friend = friend

        title = '{0}与{1}聊天中...'.format(user['user_name'], friend['user_name'])
        self.SetTitle(title)

        # 创建查看消息文本输入控件
        self.seemsg_tc = wx.TextCtrl(self.contentpanel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.seemsg_tc.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT,
                                       wx.FONTSTYLE_NORMAL,
                                       wx.FONTWEIGHT_NORMAL, faceName='微软雅黑'))

        # 底部发送消息面板
        bottompanel = wx.Panel(self.contentpanel, style=wx.DOUBLE_BORDER)

        bottomhbox = wx.BoxSizer()
        # 创建发送消息文本输入控件
        self.sendmsg_tc = wx.TextCtrl(bottompanel)
        # 设置焦点到发送消息文本输入控件
        self.sendmsg_tc.SetFocus()
        self.sendmsg_tc.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT,
                                        wx.FONTSTYLE_NORMAL,
                                        wx.FONTWEIGHT_NORMAL, faceName='微软雅黑'))

        sendmsg_btn = wx.Button(bottompanel, label='发送')
        self.Bind(wx.EVT_BUTTON, self.on_click, sendmsg_btn)

        bottomhbox.Add(self.sendmsg_tc, 5, wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        bottomhbox.Add(sendmsg_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        bottompanel.SetSizer(bottomhbox)

        # 创建整体Box布局管理对象
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.seemsg_tc, 5, wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        box.Add(bottompanel, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        self.contentpanel.SetSizer(box)

        # 消息日志
        self.msglog = ''

        # 子线程运行状态
        self.isrunning = True
        # 创建一个子线程
        self.t1 = threading.Thread(target=self.thread_body)
        # 启动线程t1
        self.t1.start()

    def on_click(self, event):
        # 发送消息
        if self.sendmsg_tc.GetValue() != '':
            now = datetime.datetime.today()
            strnow = now.strftime('%Y-%m-%d %H:%M:%S')
            # 在消息查看框中显示消息
            msg = '#{0}#\n您对{1}说：{2}\n'.format(strnow, self.friend['user_name'], self.sendmsg_tc.GetValue())
            self.msglog += msg
            self.seemsg_tc.SetValue(self.msglog)
            # 光标显示在最后一行
            self.seemsg_tc.SetInsertionPointEnd()

            # 向服务器发送消息
            json_obj = {}
            json_obj['command'] = COMMAND_SENDMSG
            json_obj['user_id'] = self.user['user_id']
            json_obj['message'] = self.sendmsg_tc.GetValue()
            json_obj['receive_user_id'] = self.friend['user_id']

            # JSON编码
            json_str = json.dumps(json_obj)
            # 给服务器端发送数据
            client_socket.sendto(json_str.encode(), server_address)
            # 清空发送消息文件框
            self.sendmsg_tc.SetValue('')

    # 线程体函数
    def thread_body(self):
        # 当前线程对象
        while self.isrunning:
            try:
                # 从服务器端接收数据
                json_data, _ = client_socket.recvfrom(1024)
                # JSON解码
                json_obj = json.loads(json_data.decode())
                logger.info('CharFrame从服务器端接收数据：{0}'.format(json_obj))
                command = json_obj['command']
                # command不等于空值时候执行
                if command is not None and command == COMMAND_REFRESH: # 刷新好友列表
                    # 获得好友列表
                    userids = json_obj['OnlineUserList']
                    # 刷新好友列表
                    self.friendsframe.refreshfriendlist(userids)
                else:  # 接收聊天信息
                    # 获得当前时间，并格式化
                    now = datetime.datetime.today()
                    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
                    # 在消息查看框中显示消息
                    message = json_obj['message']
                    log = "#{0}#\n{1}对您说：{2}\n".format(strnow, self.friend['user_name'], message)
                    self.msglog += log
                    self.seemsg_tc.SetValue(self.msglog)
                    # 光标显示在最后一行
                    self.seemsg_tc.SetInsertionPointEnd()

            except Exception:
                continue

    # 重写OnClose方法
    def OnClose(self, event):
        # 停止当前子线程
        self.isrunning = False
        self.t1.join()
        self.Hide()
        # 重启好友列表窗口子线程
        self.friendsframe.resettread()
