# -*- coding=utf-8 -*-
import os
from script import saver
from config import setting


def install_app(device_id, app):
    if setting.InstallApk:
        install_command = "adb -s " + device_id + " install -r " + app.apkPath
        result = os.popen(install_command).readlines()
        result = result[-1]
        if 'success' in result:
            return True
        else:
            print result
            return False


def uninstall_app(device_id, app):
    if setting.UnInstallApk:
        uninstall_command = "adb -s " + device_id + " uninstall " + app.packageName
        os.system(uninstall_command)


def app_is_installed(device_id, package_name):
    command = 'adb -s ' + device_id + " shell pm list"
    result = os.popen(command)
    lines = result.readlines()
    for line in lines:
        if ("package:"+package_name) == line[:-2]:
            del command, lines, device_id, line, package_name
            return True
        del line
    del command, lines, device_id, package_name
    return False


def run_monkey(plan, app, device):
    if setting.InstallApk:
        uninstall_app(device.id, app)
        if not install_app(device.id, app):
            device.result = "InstallFail"
    elif not app_is_installed(device.id, app.packageName):
        device.result = "InstallFail"

    if device.result != "InstallFail":
        if device.statue == "unlock":
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
        else:
            device.result = "DeviceExc"


