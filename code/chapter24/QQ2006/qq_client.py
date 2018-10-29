# coding=utf-8
# 代码文件：chapter24/QQ2006/qq_client.py

import logging

import wx

from com.zhijieketang.qq.client.login_frame import LoginFrame

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = LoginFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
