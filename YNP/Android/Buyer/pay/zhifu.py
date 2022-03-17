# -*- encoding=utf8 -*-
__author__ = "ext.yangyang16"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

poco(text="待付款").click()
poco(text="去支付").click()
poco(text="京东支付").click()
poco("android.widget.FrameLayout").offspring("app").child("android.view.View")[6].child("android.view.View")[1].click()
wait(Template(r"tpl1645514974798.png", record_pos=(-0.213, 0.256), resolution=(1080, 2400)))
poco("com.jd.lib.jdpaysdk.feature:id/jdpay_payinfo_txt_pay").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jingdong.app.mall:id/a3k").child("android.widget.LinearLayout")[1].child("android.widget.FrameLayout")[2].child("android.view.View").click()
sleep(0.8)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jingdong.app.mall:id/a3k").child("android.widget.LinearLayout")[0].child("android.widget.FrameLayout")[2].child("android.view.View").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jingdong.app.mall:id/a3k").child("android.widget.LinearLayout")[0].child("android.widget.FrameLayout")[0].child("android.view.View").click()
sleep(0.5)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jingdong.app.mall:id/a3k").child("android.widget.LinearLayout")[1].child("android.widget.FrameLayout")[2].child("android.view.View").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jingdong.app.mall:id/a3k").child("android.widget.LinearLayout")[2].child("android.widget.FrameLayout")[0].child("android.view.View").click()
sleep(0.6)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jingdong.app.mall:id/a3k").child("android.widget.LinearLayout")[1].child("android.widget.FrameLayout")[2].child("android.view.View").click()
sleep(5.0)
if poco("com.jd.lib.ordercenter.feature:id/order_status_text").get_text()=="待出厅核验":
    print("支付成功")