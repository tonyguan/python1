# coding=utf-8
# 代码文件：chapter22/PetStore/com/zhijieketang/petstore/ui/product_list_frame.py

"""商品列表窗口"""
import wx
import wx.grid

from com.zhijieketang.petstore.dao.product_dao import ProductDao
from com.zhijieketang.petstore.ui.my_frame import MyFrame
from com.zhijieketang.petstore.ui.cart_frame import CartFrame
from com.zhijieketang.petstore.ui.product_list_gridtable import ProductListGridTable

# 商品类别
CATEGORYS = ['鱼类', '狗类', '爬行类', '猫类', '鸟类']


class ProductListFrame(MyFrame):
    def __init__(self):
        super().__init__(title='商品列表窗口', size=(1000, 700))

        #  购物车，键是选择的商品Id，值是商品的数量
        self.cart = {}
        # 选中商品
        self.selecteddata = {}

        # 创建DAO对象
        dao = ProductDao()
        # 查询所有数据
        self.data = dao.findall()

        # 创建分隔窗口
        splitter = wx.SplitterWindow(self.contentpanel, style=wx.SP_3DBORDER)
        # 创建分隔窗口中的左侧面板
        self.leftpanel = self.createleftpanel(splitter)
        # 创建分隔窗口中的右侧面板
        self.rightpanel = self.createrightpanel(splitter)

        # 设置分隔窗口左右布局
        splitter.SplitVertically(self.leftpanel,
                                 self.rightpanel,
                                 630)
        # 设置最小窗口尺寸
        splitter.SetMinimumPaneSize(630)

        # 设置整个窗口布局是垂直Box布局
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.contentpanel.SetSizer(vbox)

        # 添加顶部对象（topbox）到vbox
        vbox.Add(self.createtopbox(), 1, flag=wx.EXPAND | wx.ALL, border=20)
        # 添加底部对象(splitter)到vbox
        vbox.Add(splitter, 1, flag=wx.EXPAND | wx.ALL, border=10)

        # 在当前创建（Frame对象）创建并添加默认状态栏
        self.CreateStatusBar()
        self.SetStatusText('准备就绪')

    def createtopbox(self):
        """创建顶部布局管理器topbox"""

        # 创建静态文本
        pc_st = wx.StaticText(parent=self.contentpanel, label='选择商品类别：', style=wx.ALIGN_RIGHT)
        # 创建按钮对象
        search_btn = wx.Button(parent=self.contentpanel, label='查询')
        reset_btn = wx.Button(parent=self.contentpanel, label='重置')
        choice = wx.Choice(self.contentpanel, choices=CATEGORYS, name='choice')
        # 绑定事件处理
        self.Bind(wx.EVT_BUTTON, self.search_btn_onclick, search_btn)
        self.Bind(wx.EVT_BUTTON, self.reset_btn_onclick, reset_btn)

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.AddSpacer(200)
        box.Add(pc_st, 1, flag=wx.FIXED_MINSIZE | wx.ALL, border=10)
        box.Add(choice, 1, flag=wx.EXPAND | wx.ALL, border=5)
        box.Add(search_btn, 1, flag=wx.EXPAND | wx.ALL, border=5)
        box.Add(reset_btn, 1, flag=wx.EXPAND | wx.ALL, border=5)
        box.AddSpacer(260)

        return box

    def createleftpanel(self, parent):
        """创建分隔窗口中的左侧面板"""

        panel = wx.Panel(parent)

        # 创建网格对象
        grid = wx.grid.Grid(panel, name='grid')
        # 绑定网格事件处理
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.selectrow_handler)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.selectrow_handler)

        # 初始化网格
        self.initgrid()

        # 创建水平Box管理管理
        box = wx.BoxSizer()
        # 设置水平Box管理管理网格grid
        box.Add(grid, 1, flag=wx.ALL, border=5)
        panel.SetSizer(box)

        return panel

    def initgrid(self):
        """初始化网格对象"""

        # 通过网格名字获得网格对象
        grid = self.FindWindowByName('grid')

        # 创建网格中所需的表格
        table = ProductListGridTable(self.data)
        # 设置网格的表格属性
        grid.SetTable(table, True)

        rowsizeinfo = wx.grid.GridSizesInfo(40, [])
        # 设置网格所有行高
        grid.SetRowSizes(rowsizeinfo)
        colsizeinfo = wx.grid.GridSizesInfo(0, [100, 80, 130, 200])
        # 设置网格所有列宽
        grid.SetColSizes(colsizeinfo)
        # 设置单元格默认字体
        grid.SetDefaultCellFont(wx.Font(11, wx.FONTFAMILY_DEFAULT,
                                        wx.FONTSTYLE_NORMAL,
                                        wx.FONTWEIGHT_NORMAL, faceName='微软雅黑'))
        # 设置行和列标题的默认字体
        grid.SetLabelFont(wx.Font(9, wx.FONTFAMILY_DEFAULT,
                                  wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_NORMAL, faceName='微软雅黑'))
        # 设置网格选择模式为行选择
        grid.SetSelectionMode(grid.wxGridSelectRows)
        # 设置行不能通过拖动改变高度
        grid.DisableDragRowSize()
        # 设置列不能通过拖动改变宽度
        grid.DisableDragColSize()

    def createrightpanel(self, parent):
        """创建分隔窗口中的右侧面板"""

        panel = wx.Panel(parent, style=wx.TAB_TRAVERSAL | wx.BORDER_DOUBLE)
        panel.SetBackgroundColour(wx.WHITE)

        # 显示第一张图片
        imagepath = 'resources/images/' + self.data[0]['image']
        image = wx.Bitmap(imagepath, wx.BITMAP_TYPE_ANY)
        image_sbitmap = wx.StaticBitmap(panel, bitmap=image, name='image_sbitmap')

        # 商品市场价格
        slistprice = "商品市场价：￥{0:.2f}".format(self.data[0]['listprice'])
        listprice_st = wx.StaticText(panel, label=slistprice, name='listprice')
        # 市场价格
        sunitcost = "商品单价：￥{0:.2f}".format(self.data[0]['unitcost'])
        unitcost_st = wx.StaticText(panel, label=sunitcost, name='unitcost')
        # 商品描述
        descn = "商品描述：{0}".format(self.data[0]['descn'])
        descn_st = wx.StaticText(panel, label=descn, name='descn')

        # 创建按钮对象
        addcart_btn = wx.Button(panel, label='添加到购物车')
        seecart_btn = wx.Button(panel, label='查看购物车')
        # 绑定事件处理
        self.Bind(wx.EVT_BUTTON, self.addcart_btn_onclick, addcart_btn)
        self.Bind(wx.EVT_BUTTON, self.seecart_btn_onclick, seecart_btn)

        # 创建垂直Box布局管理器
        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(50)
        box.Add(image_sbitmap, 1, flag=wx.CENTER | wx.ALL, border=30)
        box.AddSpacer(50)
        box.Add(listprice_st, 1, flag=wx.EXPAND | wx.ALL, border=10)
        box.Add(unitcost_st, 1, flag=wx.EXPAND | wx.ALL, border=10)
        box.Add(descn_st, 1, flag=wx.EXPAND | wx.ALL, border=10)
        box.AddSpacer(20)
        box.Add(addcart_btn, 1, flag=wx.EXPAND | wx.ALL, border=10)
        box.Add(seecart_btn, 1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(box)

        return panel

    def search_btn_onclick(self, event):
        """查询按钮事件处理"""

        # 通过名字查询choice控件
        choice = self.FindWindowByName('choice')
        # 获得选中类别索引
        selectcatidx = choice.GetSelection()
        if selectcatidx >= 0:
            # 获得选中的商品类别
            catname = CATEGORYS[selectcatidx]

            # 根据类别查询商品
            dao = ProductDao()
            self.data = dao.findbycat(catname)
            # 初始化网格
            self.initgrid()

    def reset_btn_onclick(self, event):
        """重置按钮事件处理"""

        # 查询所有商品
        dao = ProductDao()
        self.data = dao.findall()
        # 初始化网格
        self.initgrid()

    def addcart_btn_onclick(self, event):
        """添加到购物车事件处理"""

        if len(self.selecteddata) == 0:
            self.SetStatusText('请先选择商品')
            return

        # 获得选择的商品id
        productid = self.selecteddata['productid']
        if productid in self.cart.keys():  # 判断购物车中已经有该商品
            # 获得商品数量
            quantity = self.cart[productid]
            self.cart[productid] = (quantity + 1)
        else:  # 购物车中还没有该商品
            self.cart[productid] = 1

        # 显示在状态栏
        self.SetStatusText('商品{0}添加到购物车'.format(productid))
        print(self.cart)

    def seecart_btn_onclick(self, event):
        """查看添加到购物车事件处理"""

        next_frame = CartFrame(self.cart, self)
        next_frame.Show()
        self.Hide()

    def selectrow_handler(self, event):
        """选择网格行事件处理"""

        srowidx = event.GetRow()
        if srowidx >= 0:
            print(self.data[srowidx])
            self.selecteddata = self.data[srowidx]
            self.SetStatusText('选择第{0}行数据'.format(srowidx + 1))

            # 显示选择的图片
            imagepath = 'resources/images/' + self.selecteddata['image']
            image = wx.Bitmap(imagepath, wx.BITMAP_TYPE_ANY)
            # 通过名字查询子窗口
            image_sbitmap = self.FindWindowByName('image_sbitmap')
            image_sbitmap.SetBitmap(image)

            # 商品市场价格
            slistprice = "商品市场价：￥{0:.2f}".format(self.selecteddata['listprice'])
            listprice_st = self.FindWindowByName('listprice')
            listprice_st.SetLabelText(slistprice)

            # 市场价格
            sunitcost = "商品单价：￥{0:.2f}".format(self.selecteddata['unitcost'])
            unitcost_st = self.FindWindowByName('unitcost')
            unitcost_st.SetLabelText(sunitcost)

            # 商品描述
            descn = "商品描述：{0}".format(self.selecteddata['descn'])
            descn_st = self.FindWindowByName('descn')
            descn_st.SetLabelText(descn)

            self.rightpanel.Layout()

        event.Skip()
