import AAA
from ABC.BASE import Base
import sys,os
sys.path.append(os.getcwd())
import random
from selenium import webdriver
from  time import sleep
# 随机生成vi
seed = "1234567890ABCDEFGHLJKMNPRSTUVWXYZ"
sa = []
for i in range(17):
    sa.append(random.choice(seed))
salt = ''.join(sa)