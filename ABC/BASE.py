from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import datetime
import sys,os
sys.path.append(os.getcwd())
import allure,time
class Base:
    def __init__(self, driver):
        # 初始化driver -- 供find_element 和 find_elements使用
        self.driver = driver

    def search_element(self, loc, timeout=15, poll=1.0):

        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=15, poll=1):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, name=None):
        """
        点击元素
        :param loc:
        :return:
        """
        if name:
            a,b = loc
            loc = (a, b.format(name))

        self.search_element(loc).click()
    def input_element(self, loc, text):
        """
        输入内容
        :param loc:
        :param text: 输入的文本
        :return:
        """
        input_text = self.search_element(loc)
        input_text.clear()
        input_text.send_keys(text)

    def slide(self,startx, starty, endx, endy, duration ):
        """

        :param startx:开始x
        :param starty:开始
        :param endx: 结束x
        :param endy:结束y
        :param duration: 滑动的时间
        :return:
        """
        return self.driver.swipe(startx, starty, endx, endy, duration)

    def click_deierd(self):
        self.driver.click()
    def click_tar(self,a,b):
        """

        :param a: 点击的元素
        :param b: 长安的秒数
        :return: a
        """

        return TouchAction(self.driver).long_press(self.search_element(a), duration=b).release().perform()
    def click_start_activity(self):
        self.driver.start_activity("com.kanche.mars","com.kanche.mars.activity.WelcomeActivity")