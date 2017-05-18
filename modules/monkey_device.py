# -*- coding=utf-8 -*-
import datetime
import os
import re


class device:
    def __init__(self, plan, device_id):
        self.id = device_id
        self.name = self.get_device_name()
        self.model = self.get_device_model()
        self.version = self.get_device_sys_version()
        self.beginTime = datetime.datetime.now()
        self.endTime = datetime.datetime.now()
        self.logPath = self.create_device_folder(plan)
        self.result = "???"

    def create_device_folder(self, plan):
        path = plan.logPath + '/' + self.id
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_screen_resolution(self):
        command = 'adb -s ' + self.id + ' shell wm size'
        resolution = []
        result = os.popen(command).readlines()
        x = ''
        y = ''
        for line in result:
            if 'Physical size: ' in line:
                r = re.findall(r'\d+', line)
                x = r[0]
                y = r[1]
        resolution.append(x)
        resolution.append(y)
        return resolution

    def get_device_name(self):
        # linux:
        # adb shell cat /system/build.prop | grep "product"
        # windows
        # adb -s 84B5T15A10010101 shell cat /system/build.prop | findstr "product"
        device_name = ''
        try:
            command = 'adb -s ' + self.id + ' shell cat /system/build.prop | grep "product" '
            result = os.popen(command).readlines()
            for line in result:
                key = 'ro.product.model='
                if key in line:
                    device_name = line[line.find(key) + len(key):-2]
                    break
        except Exception, e:
            print (e)
            command = 'adb -s ' + self.id + ' shell cat /system/build.prop | findstr "product" '
            result = os.popen(command).readlines()
            for line in result:
                key = 'ro.product.model='
                if key in line:
                    device_name = line[line.find(key) + len(key):-2]
                    del key
                    break
        del command, result
        return device_name

    def get_device_model(self):
        command = 'adb -s ' + self.id + ' shell getprop ro.product.model'
        model = os.popen(command).read()
        return model

    def get_device_sys_version(self):
        command = 'adb -s ' + self.id + ' shell getprop ro.build.version.release'
        result = os.popen(command).read()
        del command
        return result

    def update_begin_time(self):
        self.beginTime = datetime.datetime.now()

    def update_end_time(self):
        self.endTime = datetime.datetime.now()
