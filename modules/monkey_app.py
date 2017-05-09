# -*- coding:utf-8 -*-
import os


class App:
    def __init__(self):
        self.apkPath = ""
        self.appName = ""
        self.packageName = ""
        self.versionCode = ""
        self.versionName = ""
        self.buildVersion = ""
        self.buildUrl = ""

    def get_app_name(self):
        try:
            command = 'aapt dump badging ' + self.apkPath
            result = os.popen(command).readlines()
            for line in result:
                name_head = "application-label-zh-CN:'"
                if name_head in line:
                    name = line[line.index(name_head) + len(name_head):len(line) - 2]
                    del name_head
                    self.appName = name
                del line
            del command, result
            self.appName = ''
        except:
            self.appName = ""

    def get_package_name(self):
        try:
            command = 'aapt dump badging ' + self.apk_path
            result = os.popen(command).readlines()
            for line in result:
                package_head = "package: name='"
                end = "' "
                if package_head in line:
                    package_name = line[line.index(package_head) + len(package_head):line.index(end)]
                    del command, result, package_head, end
                    self.packageName = package_name
            del command, result
            self.packageName = ''
        except:
            self.packageName = ""

    def get_version_code_in_device(self, device_id):
        try:
            command = 'adb -s ' + device_id + ' shell dumpsys package ' + self.packageName
            result = os.popen(command).readlines()
            for line in result:
                version_code_head = "versionCode="
                end = " t"
                if version_code_head in line:
                    line = line[line.index(version_code_head) + len(version_code_head):]
                    version_code = line[:line.index(end)]
                    del command, result, version_code_head, line
                    self.versionCode = version_code
            del command, result, device_id
            self.versionCode = ''
        except:
            del device_id
            self.versionCode = ''

    def get_version_code(self):
        try:
            command = 'aapt dump badging ' + self.apkPath
            result = os.popen(command).readlines()
            for line in result:
                version_code_head = "versionCode='"
                end = "' "
                if version_code_head in line:
                    line = line[line.index(version_code_head) + len(version_code_head):]
                    version_code = line[:line.index(end)]
                    del command, result, version_code_head, line
                    self.versionCode = version_code
            del command, result
            self.versionCode = ''
        except:
            self.versionCode = ''

    def get_version_name_in_device(self, device_id):
        try:
            command = 'adb -s ' + device_id + ' shell dumpsys package ' + self.packageName
            result = os.popen(command).readlines()
            for line in result:
                version_name_head = "versionName="
                if version_name_head in line:
                    version_name = line[line.index(version_name_head) + len(version_name_head):]
                    del command, result, version_name_head, line
                    self.versionName = version_name
            del command, result, device_id
            self.versionName = ''
        except:
            del device_id
            self.versionName = ''

    def get_version_name(self):
        try:
            command = 'aapt dump badging ' + self.apkPath
            result = os.popen(command).readlines()
            for line in result:
                version_name_head = "versionName='"
                end = "' "
                if version_name_head in line:
                    line = line[line.index(version_name_head) + len(version_name_head):]
                    version_name = line[:line.index(end)]
                    del command, result, line, version_name_head, end
                    self.versionName = version_name
            del command, result
            self.versionName = ''
        except:
            self.versionName = ''
