# -*- coding=utf-8 -*-
import os
from script import saver
from config import setting


def install_app(device_id_list, app):
    if setting.InstallApk:
        for device_id in device_id_list:
            install_command = "adb -s " + device_id + " install " + app.apkPath
            os.system(install_command)


def uninstall_app(device_id_list, app):
    if setting.UnInstallApk:
        for device_id in device_id_list:
            uninstall_command = "adb -s " + device_id + " uninstall " + app.packageName
            os.system(uninstall_command)


def run_monkey(plan, app, device):
    device.logFile = 'monkey_' + device.id + '.txt'
    monkey_command = "adb -s " + device.id + " shell monkey -p " + app.packageName + "  -v -v --throttle 200 10000 > " + device.logPath + "/monkey.txt"
    device.update_begin_time()
    os.system(monkey_command)
    device.update_end_time()
    logfile = open(device.logPath + "/monkey.txt", 'r')
    log = logfile.read()
    if "Monkey finished" in log:
        device.result = "Passed"
    elif "CRASH" in log:
        device.result = "Crashed"
    elif "NOT RESPONDING" in log:
        device.result = "ANR"
    elif "ERROR" in log:
        device.result = "Error"
    else:
        device.result = "Unknown Exception"
    saver.save_logcat(plan, device)

