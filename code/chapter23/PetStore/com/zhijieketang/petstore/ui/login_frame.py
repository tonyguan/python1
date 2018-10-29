# coding=utf-8
# 代码文件：chapter22/PetStore/com/zhijieketang/petstore/ui/login_frame.py

"""用户登录窗口"""
import sys
import wx

from com.zhijieketang.petstore.dao.account_dao import AccountDao
from com.zhijieketang.petstore.ui.my_frame import MyFrame
from com.zhijieketang.petstore.ui.product_list_frame import ProductListFrame


class LoginFrame(MyFrame):
    def __init__(self):
        super().__init__(title='用户登录', size=(340, 230))

        # 创建界面控件
        accountid_st = wx.StaticText(self.contentpanel, label='账号：')
        password_st = wx.StaticText(self.contentpanel, label='密码：')
        self.accountid_txt = wx.TextCtrl(self.contentpanel)
        self.password_txt = wx.TextCtrl(self.contentpanel, style=wx.TE_PASSWORD)

        # 创建FlexGrid布局fgs对象
        fgs = wx.FlexGridSizer(2, 2, 20, 20)
        fgs.AddMany([(accountid_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     (self.accountid_txt, 1, wx.CENTER | wx.EXPAND),
                     (password_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     (self.password_txt, 1, wx.CENTER | wx.EXPAND)])
        # 设置FlexGrid布局对象
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 4)

        # 创建按钮对象
        okb_btn = wx.Button(parent=self.contentpanel, label='确定')
        self.Bind(wx.EVT_BUTTON, self.okb_btn_onclick, okb_btn)
        cancel_btn = wx.Button(parent=self.contentpanel, label='取消')
        self.Bind(wx.EVT_BUTTON, self.cancel_btn_onclick, cancel_btn)

        # 创建水平Box布局hbox对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(okb_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        hbox.Add(cancel_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)

        # 创建垂直Box布局，把fgs和hbox添加到垂直Box布局对象上
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(fgs, -1, wx.CENTER | wx.ALL | wx.EXPAND, border=25)
        vbox.Add(hbox, -1, wx.CENTER | wx.BOTTOM, border=20)

        self.contentpanel.SetSizer(vbox)

    def okb_btn_onclick(self, event):
        """确定按钮事件处理"""

        dao = AccountDao()
        account = dao.findbyid(self.accountid_txt.GetValue())
        password = self.password_txt.GetValue()

        if account is not None and account['password'] == password:
            print('登录成功。')
            next_frame = ProductListFrame()
            next_frame.Show()
            self.Hide()

            # 登录成功保存用户Session
            MyFrame.Session = account

        else:
            print('登录失败。')
            dlg = wx.MessageDialog(self, '您输入的账号或密码有误，请重新输入。',
                                   '登录失败',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

    def cancel_btn_onclick(self, event):
        """取消按钮事件处理"""

        # 退出系统
        self.Destroy()
        sys.exit(0)
