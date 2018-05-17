# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter19/ch19.4.1.py

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='一对一事件处理', size=(300, 180))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, pos=(110, 20))
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

    def on_click(self, event):
        print(type(event))  # <class 'wx._core.CommandEvent'>
        self.statictext.SetLabelText('Hello, world.')


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
