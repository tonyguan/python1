# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter24/PetStore/com/zhijieketang/petstore/ui/product_list_gridtable.py

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
