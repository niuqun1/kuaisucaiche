
import AAA
from ABC.BASE import Base
import sys,os
sys.path.append(os.getcwd())
import  random
from time import sleep
seed = "1234567890ABCDEFGHLJKMNPRSTUVWXYZ"
sa = []
for i in range(17):
    sa.append(random.choice(seed))
salt = ''.join(sa)
class search(Base):
    # 生成随机vin码
    # 获取base
    def  __init__(self,deiver):
        Base.__init__(self,deiver)
    def click_xj(self):
        self.click_element(AAA.XJ)
    def click_tar1(self):
        self.click_tar(AAA.XJ,1850)
    # 登陆账号
    def import_login(self,A="10000000156",B="uat.portal"):
        self.input_element(AAA.username,A)
        self.input_element(AAA.password,B)
        self.click_element(AAA.lohin)
    def click_cjru(self):
        self.click_element(AAA.cjrk)
        self.click_element(AAA.jia)
        self.click_element(AAA.ss)
    def click_md(self):#选择门店
        md = self.search_elements(AAA.xzmd)
        md[0].click()
        self.click_element(AAA.okan)
    def click_xj2(self):
        a = self.search_elements(AAA.mtxj)
        a[0].click()
    # 点击拍照按钮
    def click_ok(self):
        self.click_element(AAA.vinkm)
    # 不识别vin
    def click_fou(self):
        self.click_element(AAA.fou)
    # 选择车型
    def click_cx(self):
        self.click_element(AAA.cx1)
        self.click_element(AAA.cx2)
        self.click_element(AAA.cx3)
        self.click_element(AAA.cx4)
# 表现历程
    def input_bxl(self, a="14"):
        self.input_element(AAA.bxls, a)
        # 验证输入vin

    def input_vin(self, a=salt):
        self.input_element(AAA.vinsr, a)
        # 点击表显里程相机

    def ckick_bxxj(self):
        sleep(1)
        bcxj = self.search_elements(AAA.mtxj)
        bcxj[1].click()
        self.click_element(AAA.XJ)
        self.click_element(AAA.gouzp)
        # 点击车源照片相机

    def ckick_cyxj(self):
        bcxj = self.search_elements(AAA.mtxj)
        bcxj[2].click()
        # 封面：左前45度

    def click_clzp1(self):
        self.click_element(AAA.clzp1)
        # 点击快门

    def click_clzpkm(self):
        self.click_element(AAA.clzp1KM)

        # 点击添加照片
    def click_TJZP(self):

        self.click_element(AAA.zitj)

    def click_fanhu(self):
        sleep(2)
        a=self.search_elements(AAA.xhtjzp)
        for i in range(0, 16):
            a[i].click()
            sleep(0.5)
        # 选择车身颜色（红色）
    def ckick_zjxz(self):
        self.click_element(AAA.wc)
        self.click_element(AAA.fanhui)

    def click_cys(self):
        self.click_element(AAA.cys)
        self.click_element(AAA.hongs)

    def click_neis(self):
        self.click_element(AAA.nsys)
        self.click_element(AAA.qianse)
        # 选择车辆性质(非营运车辆）以及车辆类别

    def click_cxz(self):
        self.click_element(AAA.clxz)
        self.click_element(AAA.fyy)
        self.click_element(AAA.cllb)
        self.click_element(AAA.cllbxz)
        # 选择初等日期

    def click_cdrq(self):
        self.click_element(AAA.cdrq)
        self.click_element(AAA.okrq)
        # 售价

    def input_sj(self, jiage="119"):
        self.input_element(AAA.sj, jiage)

        # 审核备注

    def input_clbz(self, beizhu="自动化采车"):
        self.input_element(AAA.shbz, beizhu)
        # 车辆描述

    def input_clms(self, abc="车辆vin是%s" % salt):
        self.input_element(AAA.cyms, abc)
    def click_selclick_start_activity(self):
        self.click_start_activity()
    def driver_quit(self):
        self.driver.close_app()
    def click_baocun(self):
        self.click_element(AAA.baocun)
        self.click_element(AAA.shang)

    def click_wode(self):
        self.click_element(AAA.fanhui)
        self.click_element(AAA.my)
    def clcik_esc(self):
        self.click_element(AAA.esc)

