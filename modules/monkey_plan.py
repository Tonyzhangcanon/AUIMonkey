# -*- coding:utf-8 -*-
import os
import datetime
import monkey_device
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Plan:
    def __init__(self):
        self.runBeginTime = datetime.datetime.now()
        self.logPath = self.create_this_time_folder()
        self.deviceList = []
        self.deviceNum = str(len(self.deviceList))
        self.passedDevice = 0
        self.failedDevice = 0
        self.endTime = None
        self.workspace = ''
        self.resultHtml = '<a>测试结果</a>'

    # change the node info ,because the same type nodes has difference bounds.
    # the same type nodes need crawl once only

    def create_this_time_folder(self):
        path = os.getcwd() + '/result/' + self.runBeginTime.strftime('%Y%m%d%H%M%S')
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_device_list(self):
        device_list = []
        string = '	'
        outLine = os.popen('adb devices').readlines()
        for line in outLine:
            if string in line:
                device_id = line[0:line.index(string)]
                device = monkey_device.device(self, device_id)
                device_list.append(device)
                del device_id, device
            del line
        self.deviceList = device_list
        self.deviceNum = str(len(device_list))
        del device_list, string, outLine

    def update_device_list(self, id_list):
        device_list = []
        for device_id in id_list:
            device = monkey_device.device(self, device_id)
            device_list.append(device)
            del device_id, device
        self.deviceList = device_list
        self.deviceNum = str(len(device_list))
        del device_list



