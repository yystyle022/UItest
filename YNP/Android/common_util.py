import logging
from airtest.core.api import *
from airtest.core.device import Device
from airtest.core.android.adb import *
from airtest.core.android.android import *
from airtest.utils.logger import get_logger
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from threading import Thread

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)  # 获取安装手机权限，
dev = device()  # 获取设备权限
auto_setup(__file__)


# 安装app
def install_app():
    sleep(5)
    for i in range(3):
        if poco("com.oplus.appdetail:id/continue_install").exists():
            poco("com.oplus.appdetail:id/continue_install").click()
        sleep(5)
        if poco(text="继续安装").exists():
            poco(text="继续安装").click()
        sleep(5)
        if poco(text="完成").exists():
            poco(text="完成").click()


# 初始化app,包括启动app，授权，
def init_app():
    keyevent("BACK")
    stop_app("com.jdd.smart.agricultural")
    start_app("com.jdd.smart.agricultural")
    # 授予相机权限
    shell("pm grant com.jdd.smart.agricultural android.permission.CAMERA")
    # 授予悬浮窗权限
    shell("pm grant com.jdd.smart.agricultural android.permission.SYSTEM_ALERT_WINDOW")
    # 授予获取地理位置权限
    shell("pm grant com.jdd.smart.agricultural android.permission.ACCESS_COARSE_LOCATION")
    # 授予获取地理位置权限
    shell("pm grant com.jdd.smart.agricultural android.permission.ACCESS_FINE_LOCATION")
    # 授予录音权限
    shell("pm grant com.jdd.smart.agricultural android.permission.RECORD_AUDIO")
    # 授予写权限
    shell("pm grant com.jdd.smart.agricultural android.permission.WRITE_EXTERNAL_STORAGE")
    # 授予读权限
    shell("pm grant com.jdd.smart.agricultural android.permission.READ_EXTERNAL_STORAGE")
    # 页面弹窗消除
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)
    sleep(3)
    for i in range(3):
        if poco(textMatches='.*允许').exists():
            poco(textMatches='.*允许').click()
        if poco(text='跳过').exists():
            poco(text='跳过').click()
        if poco(text='同意').exists():
            poco(text='同意').click()
        if poco(text='同意').exists():
            poco(text='同意').click()
        if poco(text='我知道了').exists():
            poco(text='我知道了').click()
        if poco(textMatches='.*允许').exists():
            poco(textMatches='.*允许').click()
        if poco(text='好的').exists():
            poco(text='好的').click()
        if poco(name='android:id/button1', text='确定').exists():
            poco(name='android:id/button1', text='确定').click()
        if poco(text='跳过').exists():
            poco(text='跳过').click()
        if poco(text='不提醒').exists():
            poco(text='不提醒').click()
    # 关闭弹窗
    # keyevent("BACK")
    return poco

#通知弹窗去除



# 点击更新app
def Update():
    if exists(Template(r"tpl1645522602523.png", record_pos=(-0.006, 0.146), resolution=(1080, 2400))):
        touch(Template(r"tpl1645522602523.png", record_pos=(-0.021, 0.144), resolution=(1080, 2400)))
        poco(text="允许本次安装").wait_for_appearance()
        poco(text="允许本次安装").click()
        wait(Template(r"tpl1645524218200.png", record_pos=(-0.009, 1.002), resolution=(1080, 2400)))
        touch(Template(r"tpl1645524218200.png", record_pos=(0.014, 1.0), resolution=(1080, 2400)))
        poco(text="安装完成").wait_for_appearance()
        poco(text="打开应用").click()
        print("更新完成")
    elif exists(Template(r"tpl1645522793863.png", record_pos=(-0.009, 0.142), resolution=(1080, 2400))):
        touch(Template(r"tpl1645522793863.png", record_pos=(-0.021, 0.144), resolution=(1080, 2400)))
        poco(text="允许本次安装").wait_for_appearance()
        poco(text="允许本次安装").click()
        wait(Template(r"tpl1645524218200.png", record_pos=(-0.009, 1.002), resolution=(1080, 2400)))
        touch(Template(r"tpl1645524218200.png", record_pos=(0.014, 1.0), resolution=(1080, 2400)))
        poco(text="安装完成").wait_for_appearance()
        poco(text="打开应用").click()
        print("更新完成")
    else:
        return True


# 页面上滑
def swipe_to_up():
    width, height = device().get_current_resolution()
    start_pt = (width / 2, height * 0.8)
    end_pt = (width / 2, height * 0.169)
    swipe(start_pt, end_pt, duration=1)
    sleep(1)


# 页面下滑
def swipe_to_down():
    width, height = device().get_current_resolution()
    start_pt = (width / 2, height * 0.35)
    end_pt = (width / 2, height * 0.95)
    swipe(start_pt, end_pt, duration=1)
    sleep(1)


# install(r"D:\software_ynp\smart-agricultural-jdd.apk")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>安装成功>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
if __name__ == '__main__':
    Update()
