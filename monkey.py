# -*- coding:utf-8 -*-
import threading
import getopt
import sys
from modules import monkey_app
from modules import monkey_plan
from runner import monkey_runner
from script import saver
from script import email_sender
from config import setting


plan = monkey_plan.Plan()
device_id_list = []
device_list = []
thread_list = []
app = monkey_app.App()
opts, args = getopt.getopt(sys.argv[1:], "iua:b:d:e:n:p:s:t:w:")
for op, value in opts:
    if op == "-a":
        app.apkPath = value
        app.get_package_name()
        app.get_app_name()
        app.get_version_code()
        app.get_version_name()
    elif op == "-b":
        build_info = []
        build_info = value.split(',')
        app.buildUrl = build_info[0]
        app.buildVersion = build_info[1]
    elif op == "-d":
        if ',' in value:
            device_id_list = value.split(',')
        else:
            device_id_list.append(value)
        plan.update_device_list(device_id_list)
    elif op == '-e':
        setting.events = value
    elif op == '-i':
        setting.InstallApk = True
    elif op == '-n':
        app.appName = value
    elif op == '-p':
        app.packageName = value
    elif op == '-s':
        setting.seed = value
    elif op == '-t':
        setting.throttle = value
    elif op == '-u':
        setting.UnInstallApk = True
        setting.InstallApk = True
    elif op == '-w':
        plan.workspace = str(value) + 'job/AUIMonkey/ws'
if len(plan.deviceList) == 0:
    plan.get_device_list()
if len(app.apkPath) == 0:
    app.get_version_code_in_device(plan.deviceList[0])
    app.get_version_name_in_device(plan.deviceList[0])

for device in plan.deviceList:
    thread = threading.Thread(target=monkey_runner.run_monkey, args=(plan, app, device))
    thread_list.append(thread)

for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()

saver.save_monkey_result(plan, app)
email_sender.send_mail(plan)
