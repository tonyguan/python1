# coding=utf-8
# 代码文件：chapter22/PetStore/app_main.py

import wx

from com.zhijieketang.petstore.ui.login_frame import LoginFrame


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = LoginFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
