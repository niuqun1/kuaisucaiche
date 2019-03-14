import sys,os
from time import sleep
sys.path.append(os.getcwd())
import allure
from AAA.AAA import search
from ABC.GET import get_driver
class Test_1:
    def setup_class(self):
        self.obj=search(get_driver())
    def test_001(self):
        self.obj.click_tar1()
        self.obj.driver_quit()
    def test_fsdf(self):
        self.obj.click_selclick_start_activity()
    def test_0011(self):
        self.obj.import_login()
    def test_cjrk(self):
        self.obj.click_cjru()
        self.obj.click_md()
        self.obj.click_xj()
        self.obj.click_ok()
        self.obj.click_fou()
    def test_click_03(self):
        self.obj.click_cx()
        self.obj.input_bxl()
        self.obj.input_vin()
    def test_4(self):
        self.obj.ckick_bxxj()
    def test_5(self):
        self.obj.ckick_cyxj()
        self.obj.click_clzp1()
    def test_6(self):
        self.obj.click_clzpkm()
        self.obj.click_TJZP()
    def test_7(self):
        self.obj.click_fanhu()
    def test_8(self):
        self.obj.ckick_zjxz()
        self.obj.click_cys()

    def test_9(self):
        self.obj.click_neis()
        self.obj.click_cxz()
        self.obj.click_cdrq()
        self.obj.input_sj()
    def test_hd(self):
        self.obj.slide(458, 1900, 458, 800, 2000)
        self.obj.input_clbz()
        self.obj.input_clms()
    # 保存
    def test_baocun(self):
        self.obj.click_baocun()
        sleep(7)
        self.obj.click_wode()
