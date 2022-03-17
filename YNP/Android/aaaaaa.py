import unittest
from airtest.core.api import *
from common_util import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
while True:
    if not poco(text="安卓按两测试带属性").exists():
        swipe_to_up()
    else:
        poco(text="安卓按两测试带属性").click()
        break
# 点击去结算
poco(text="去结算").click()
print("------------------2-------------------------")