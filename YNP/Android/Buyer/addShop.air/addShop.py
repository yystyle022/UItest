# -*- encoding=utf8 -*-
__author__ = "ext.yangyang16"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


poco("com.jdd.smart.agricultural:id/textSwitcher").click()
sleep(1)
text("自动化测试商品")
poco(text="自动化测试商品").click()
poco(text="加入购物车").click()
poco(text="确定").click()
poco("com.jd.lib.productdetail.feature:id/pd_text_shopcar_view").click()
sleep(1)
assert_equal(poco("com.jd.lib.cart.feature:id/cart_single_product_name").get_text(), "自动化测试商品", "测试商品加入购物车成功")
sleep(2)
stop_app("com.jdd.smart.agricultural")








