#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import sys,os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
xjXXXXX=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/btn_shutter']")
XJ=(By.XPATH,"//android.widget.ImageView[@resource-id='com.android.camera:id/v6_shutter_button_internal' and @content-desc='拍摄']")
username = (By.ID,"com.kanche.mars:id/et_username")
# 密码框
password=(By.ID,"com.kanche.mars:id/et_password")
# 登陆按钮
lohin=(By.ID,"com.kanche.mars:id/bt_login")
# 采集入口
cjrk=(By.XPATH,"//android.widget.TextView[@text='车源采集']")
# +
jia=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/menu_item_add' and @content-desc='Add']")
# 搜索
ss=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_dialog_search' and @text='搜索']")
# 选择门店
xzmd=(By.ID,"com.kanche.mars:id/tv_store_name")
# 选择门店 确定按钮
okan=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button1' and @text='确定']")
# vin相机
mtxj=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/button2']")
# 勾选照片
gouzp=(By.XPATH,"//android.widget.ImageView[@resource-id='com.android.camera:id/v6_btn_done']")
vinkm=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/btn_shutter']")
# 不识别vin
fou=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button2' and @text='否']")
# 识别vin
shi=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button2' and @text='是']")
# vin码填写框
vinsr=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入17位VIN码']")
# 车型
cx1=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='VIN码识别自动带入，或手选']")
cx2=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='大众']")
cx3=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='Eos']")
cx4=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='2011款 2.0 TFSI 自动']")
# 表显里数
bxls=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='保留到小数点后两位']")
# 车辆照片
# 封面：左前45度
clzp1=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='封面：左前45度']")
clzp1KM=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/btn_shutter_vehicle']")
# 点击自己天机
zitj=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_action_one' and @text='添加照片']")

# 车源相机页面完成
wanc=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/save_data' and @text='1/1 完成']")

# 车身颜色
cys=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择车身颜色']")
# 内饰颜色
qianse=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='深色']")
nsys=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择内饰颜色']")
# 红色
hongs=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='红色	']")
# 车辆性质
clxz=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择车辆性质']")
# 车辆类别
cllb=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择车辆类别']")
# 车辆类别选择七座以下普通车辆
cllbxz=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='七座（含）以下普通小型汽车']")
# 非营运车辆
fyy=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='非营运']")
# 初等日期
cdrq=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择初登日期']")
# 确定
okrq=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button1' and @text='确定']")
# 售价
sj=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='保留到小数点后两位']")
# 审核备注
shbz=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText' and @text='300字以内']")
# 车源描述
cyms=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText' and @text='200字以内']")
# 保存
baocun=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/save_data' and @text='保存']")
# 完成
wancheng=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_action_four' and @text='完成']")
# 上传
shang=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_action_three' and @text='上传车辆']")
# 循环添加照片
xhtjzp=(By.XPATH,"//android.widget.ImageView[@resource-id='com.kanche.mars:id/cover']")
# 完成
wc=(By.ID,"com.kanche.mars:id/save_data")
# 返回
fanhui=(By.XPATH,"//android.widget.ImageButton[@content-desc='转到上一层级']")
# 我的
my=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_tab' and @text='我的']")
# 退出登录
esc=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_logout' and @text='退出']")
# 登录页面