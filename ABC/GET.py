from appium import webdriver
import threading
import sys,os
sys.path.append(os.getcwd())

def get_driver():
    """
    :param pac: 包名
    :param act: 启动名
    :return:

    """
    desired_caps = {}
    # 平台 - 必填
    desired_caps['platformName'] = 'Android'
    # 系统版本 - 非必填，填写就必须正确
    desired_caps['platformVersion'] = '7.1'
    # 获取toast支持
    desired_caps['automationName'] = 'Uiautomator2'
    # 设备名称
    desired_caps['deviceName'] = 'sun'
    # desired_caps['app'] = 'apk绝对路径'
    # app包名
    desired_caps['appPackage'] = "com.android.camera"
    # app启动名
    desired_caps['appActivity'] = ".Camera"
    # 获取启动后需要的权限
    desired_caps['noReset'] = True
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# .format(port)
# if __name__ == '__main__':
#     port_list = ["4723", "4725"]
#     # 存线程list
#     thread_list = []
#     for i in port_list:
#         th = threading.Thread(target=get_driver, args=(i,))
#         th.start()
#         thread_list.append(th)
#
#     for o in thread_list:
#         o.join()