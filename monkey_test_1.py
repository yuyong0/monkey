import os
import subprocess
import threading
import time
import datetime


def uno_don():
    print('----------- 卸载旧包并下载一个新包-----------')
    os.system('adb uninstall cn.com.weilaihui3')

    os.system(
        'adb install C:\\Users\\yong.yu2\\Downloads\\lifestyle_64bit_release_dev_dev-address_337_v5.14.0_20230301-110945_ffe709a1d_vmp.apk')

# uno_don()
# time.sleep(10)

flg = True
# 控制while循环
# now1 = time.strftime('%m-%d %H:%M:%S', time.localtime())
# nowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
class PyPrecondition(object):
    def __int__(self):
        pass

    def jietu(self):
        # 隔几秒截图
        global flg
        count = 0
        while flg:
            time.sleep(3)
            count += 1
            os.system('adb shell screencap -p /sdcard/screen{}.png'.format(count))
            os.system('adb pull /sdcard/screen{}.png D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}'.format(count, name))
            os.renames("D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\screen{}.png".format(name, count),
                       "D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\{}.png" .format(name, time.strftime('%Y%m%d%H%M%S')))
            # time.sleep(5)

    def pre_con(self):
        time.sleep(3)
        self.jietu()

# lock = threading.Lock()


class MonkeyHelper(object):
    def __init__(self):
        pass

    def dev_connect(self):
        print('-----------第一步 判断设备是否连接-----------')
        r = os.popen('adb devices')
        res = r.read()  # res:'List of devices attached\n\n'
        r.close()
        global device
        device = res[res.find('\n') + 1:].split()[0]
        print(f"device:{device}")
        status = res[res.find('\n') + 1:].split()[1]
        print(f"status:{status}")
        if status == 'device':
            print('*设备{}  状态为{}  已连接'.format(device, status))
        else:
            print('*设备{}  状态为{}  未正常连接'.format(device, status))


    def screencap(self, count):
        os.system('adb shell screencap -p /sdcard/screen{}.png'.format(count))
        os.system('adb pull /sdcard/screen{}.png D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}'.format(count, name))
        os.renames("D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\screen{}.png".format(name, count),
                   "D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\{}.png".format(name, time.strftime('%Y%m%d%H%M%S')))

    # def uno_don(self):
    #     print('----- 卸载旧包并下载一个新包-----')
    #     os.system('adb uninstall cn.com.weilaihui3')
    #
    #     os.system(
    #         'adb install C:\\Users\\lijie.jia1\\Desktop\\lifestyle_64bit_release_dev_2283_v5.12.0_20230110-180407_888379651_vmp.apk')

    def run_app(self):
        print('-----------正在调起主activity-----------')
        # 此时的包名及activity已事先获得
        # 通过 查看启动的app的包名 adb shell dumpsys activity top | find "ACTIVITY" 命令
        os.system('adb shell am start cn.com.weilaihui3/.app.ui.activity.HomeActivity')

    def get_version(self):
        print('-----------获取测试机系统信息-----------')
        v = os.popen('adb shell pm dump cn.com.weilaihui3 | findstr "version"')
        res = v.read()
        v.close()
        global version_name
        version = res[res.find('\n') + 1:].split()[0]
        version_name = version.replace("versionName=", "")
        print('APP版本={}'.format(version_name))
        # 获取系统版本
        cmd_s = 'adb -s {} shell getprop ro.build.version.release'.format(device)
        release = os.popen(cmd_s).readline().replace('\n', '')
        print("系统版本={}".format(release))
        # 获取手机型号
        cmd_s = 'adb -s {} shell getprop ro.product.model'.format(device)
        self.model = os.popen(cmd_s).readline().replace('\n', '')
        print("手机型号={}".format(self.model))
        # 手机厂商
        cmd_s = 'adb -s {} shell getprop ro.product.brand'.format(device)
        brand = os.popen(cmd_s).readline().replace('\n', '')
        print("手机厂商={}".format(brand))


    # 准备工作：创建文件夹
    def mkdir(path):
        global version_name
        path = 'D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}_{}'.format(version_name, time.strftime('%Y%m%d%H%M%S'))
        global name
        name = path.split('\\')[-1]
        # 判断路径是否存在
        # 存在 true
        # 不存在 false
        isExits = os.path.exists(path)

        # 判断结果
        if not isExits:
            os.makedirs(path)  # 不存在则创建该目录
            # print('-----' + path + " 创建成功-----")
            return True
        else:
            print('-----' + path + " 目录已经存在-----")
            return False

    def run_monkey(self):
        print('正在进行指定app monkey测试')
        # 通用monkey命令
        # 指定系统事件百分比
        syskeys = 5
        # 调整触摸事件的百分比
        touch = 55
        # 调整动作事件的百分比
        motion = 20
        # 指定Activity启动的百分比
        appswitch = 0
        # 指定其他事件的百分比
        anyevent = 20
        # 在事件之间插入特定的延时时间
        throttle = 100
        # throttle = 0
        filename = "D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\logcatLog.txt".format(name)
        logcat_file = open(filename, 'w')
        logcmd = "adb logcat -v time"
        Poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        c = 'adb logcat -v threadtime > D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\logcatLog.txt'.format(name)
        os.system(c)
        # 开始前截图
        # self.screencap('1')
        # cmd = 'adb shell monkey -p com.huawei.calculator --monitor-native-crashes --ignore-crashes --pct-syskeys {} --pct-touch {} --pct-appswitch {} --pct-anyevent {} --pct-motion {} --throttle {} -s %random% -v-v-v {} >  logcat : *:S >logcatDetail.txt'.format(
        #      syskeys, touch, motion, appswitch, anyevent, throttle, 800)
        global device
        cmd = 'adb -s {} shell monkey -p cn.com.weilaihui3 --throttle {} -s {} --ignore-crashes ' \
              '--ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes --pct-syskeys {} -v-v-v ' \
              '{} >> D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}\\monkeyLog.txt'.format(device, 300, 100, syskeys, 10, name)
        os.system(cmd)
        # 开始后截图

        # Poplog.terminate()
        # 杀死子进程
        global flg
        flg = False

        Poplog.terminate()

        # os.system('adb shell monkey -p com.android.calculator2 100')
        # print('monkey测试完成 请在当前目录查看日志')

    def zip_dir(self):
        print("------------压缩产出文件-------------")
        os.system("d:")
        os.system("cd D:\Jenkins\workspace")
        os.system(
            "D:\winrar\winrar.exe a -r -s -m3 -o- -ep1 D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}.zip D:\\Jenkins\\workspace\\Android稳定性测试（Monkey）\\monkeyreport\\{}".format(
                name, name))


    def show(self):
        print('---' * 8)
        print('正在进行monkey测试......')
        print('正在调起终端......')
        self.dev_connect()
        # self.uno_don()
        self.run_app()
        time.sleep(2)
        self.get_version()
        self.mkdir()
        self.run_monkey()
        # self.screencap()
        time.sleep(2)
        self.zip_dir()
        time.sleep(5)
        print("11111")



if __name__ == "__main__":
    m = MonkeyHelper()
    p = PyPrecondition()
    # p.show()
    new_thread1 = threading.Thread(target=m.show)
    new_thread2 = threading.Thread(target=p.pre_con)
    new_thread1.start()
    new_thread2.start()
    new_thread1.join()
    new_thread2.join()
    print('monkey测试完成 请查看日志')
