# -*- encoding=utf8 -*-
__author__ = "ext.yangyang16"

from airtest.core.api import *
from Android.common_util import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
auto_setup(__file__)


# from poco.drivers.ios import iosPoco
# poco = iosPoco()

#进入到商品管理列表页面
poco(text="商品管理").click()

#进入到新建商品页面
poco(text="新建商品").wait_for_appearance()
poco(text="新建商品").click()

#新建商品基本信息页面
poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.jdd.smart.agricultural:id/fl_content").offspring("android.widget.ScrollView").offspring("com.jdd.smart.agricultural:id/containerLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout")[0].child("android.view.ViewGroup").click()
sleep(1)
text("紫苏叶",enter=False)
poco(text="新建商品").click()
if poco(text="*系统为您自动匹配了分类，如不准确可以手动调整").exists():
    poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.jdd.smart.agricultural:id/fl_content").offspring("android.widget.ScrollView").offspring("com.jdd.smart.agricultural:id/containerLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout")[1].child("android.view.ViewGroup").click()
else:
    poco(text="请选择商品所属品类名称").click()
    poco(text="蔬菜").click()
    poco(text="叶菜").click()
    poco(text="紫苏叶").click()
text("自动化测试按件单sku",enter=False)
poco(text="请选择产地所在市区县、乡镇等").click()
poco(text="重庆").click()
poco(text="巴南区").click()
poco(text="请选择商品销售单位").click()
poco(text="件").click()
poco(text="下一步").click()

#新建商品价格库存页面
poco("com.jdd.smart.agricultural:id/etPrice").click()
text("0.01")
poco("com.jdd.smart.agricultural:id/etProductWeight").click()
text("1.55")
poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.jdd.smart.agricultural:id/fl_content").offspring("android.widget.ScrollView").offspring("com.jdd.smart.agricultural:id/containerLayout").offspring("com.jdd.smart.agricultural:id/llSpuLayout").child("android.widget.LinearLayout")[2].offspring("android.widget.EditText")
text("1")
poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.jdd.smart.agricultural:id/fl_content").offspring("android.widget.ScrollView").offspring("com.jdd.smart.agricultural:id/containerLayout").offspring("com.jdd.smart.agricultural:id/llSpuLayout").child("android.widget.LinearLayout")[3].offspring("android.widget.EditText").click()
text("800")
poco(text="下一步").click()

#上传图片页面
poco(text="主图照片").click()
poco("android.widget.LinearLayout").offspring("com.jdd.smart.agricultural:id/coordinator").offspring("com.jdd.smart.agricultural:id/rv_photos").child("android.view.ViewGroup")[6].child("com.jdd.smart.agricultural:id/tv_selector").click()
poco("android.widget.LinearLayout").offspring("com.jdd.smart.agricultural:id/coordinator").offspring("com.jdd.smart.agricultural:id/tv_done").click() 
poco("com.jdd.smart.agricultural:id/menu_crop").click()
sleep(5)
poco(text="下一步").click()

#预览界面
poco(text="发布").click()
sleep(1)
if poco(text="发布成功").exists():
    print("发布成功")
sleep(5)
    
#验证商品管理列表发品  
swipe_to_down()




     



