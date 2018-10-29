# coding=utf-8
# 代码文件：chapter22/PetStore/com/zhijieketang/petstore/ui/cart_gridtable.py

"""自定义GridTableBase类, 用于购物车网格"""
import wx.grid

# 购物车网格列名
COLUMN_NAMES = ['商品编号', '商品名', '商品单价', '数量', '商品应付金额']


class CartGridTable(wx.grid.GridTableBase):
    def __init__(self, data):
        super().__init__()
        self.colLabels = COLUMN_NAMES
        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(COLUMN_NAMES)

    def GetValue(self, rowidx, colidx):
        product = self.data[rowidx]
        if colidx == 0:
            return product['productid']
        elif colidx == 1:
            return product['cname']
        elif colidx == 2:
            return product['unitcost']
        elif colidx == 3:
            return product['quantity']
        else:
            return product['amount']

    def GetColLabelValue(self, colidx):
        return self.colLabels[colidx]

    def SetValue(self, rowidx, colidx, value):
        # 只允许修改数量列
        if colidx != 3:
            return

        # 获得商品数量
        try:
            quantity = int(value)
        except:
            #输入非数字数据则不能修改
            return

        # 商品数量不能小于0
        if quantity < 0:
            return
        # 更新数量列
        self.data[rowidx]['quantity'] = quantity
        # 计算商品应付金额
        amount = self.data[rowidx]['unitcost'] * quantity
        # 更新商品应付金额列
        self.data[rowidx]['amount'] = amount
