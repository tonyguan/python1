# coding=utf-8
# 代码文件：chapter22/PetStore/com/zhijieketang/petstore/ui/product_list_gridtable.py

"""自定义GridTableBase类, 用于商品网格"""
import wx.grid

# 商品网格列名
COLUMN_NAMES = ['商品编号', '商品类别', '商品中文名', '商品英文名']


class ProductListGridTable(wx.grid.GridTableBase):
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
            return product['category']
        elif colidx == 2:
            return product['cname']
        else:
            return product['ename']

    def GetColLabelValue(self, colidx):
        return self.colLabels[colidx]
