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
                    print line
                    name = line[line.index(name_head) + len(name_head):len(line) - 2]
                    self.appName = name
                    print name
                    del name, name_head, line , command, result
                    break
        except:
            print "get app name error"

    def get_package_name(self):
        try:
            command = 'aapt dump badging ' + self.apkPath
            result = os.popen(command).readlines()
            for line in result:
                package_head = "package: name='"
                end = "' versionCode"
                if package_head in line:
                    print line
                    package_name = line[line.index(package_head) + len(package_head):line.index(end)]
                    print package_name
                    self.packageName = package_name
                    del command, result, package_head, end
                    break
        except:
            print 'get package name error'

    def get_version_code_in_device(self, device_id):
        try:
            command = 'adb -s ' + device_id + ' shell dumpsys package ' + self.packageName
            result = os.popen(command).readlines()
            for line in result:
                version_code_head = "versionCode="
                end = " t"
                if version_code_head in line:
                    print line
                    line = line[line.index(version_code_head) + len(version_code_head):]
                    version_code = line[:line.index(end)]
                    self.versionCode = version_code
                    print version_code
                    del command, result, version_code_head, line, device_id
                    break
        except:
            del device_id
            print 'get version code error'

    def get_version_code(self):
        try:
            command = 'aapt dump badging ' + self.apkPath
            result = os.popen(command).readlines()
            for line in result:
                print line
                version_code_head = "versionCode='"
                end = "' "
                if version_code_head in line:
                    print line
                    line = line[line.index(version_code_head) + len(version_code_head):]
                    version_code = line[:line.index(end)]
                    self.versionCode = version_code
                    print version_code
                    del version_code, command, result, version_code_head, line
                    break
        except:
            print 'get version code error'

    def get_version_name_in_device(self, device_id):
        try:
            command = 'adb -s ' + device_id + ' shell dumpsys package ' + self.packageName
            result = os.popen(command).readlines()
            for line in result:
                print line
                version_name_head = "versionName="
                if version_name_head in line:
                    print line
                    version_name = line[line.index(version_name_head) + len(version_name_head):]
                    self.versionName = version_name
                    del version_name, command, result, version_name_head, line, device_id
                    break
        except:
            del device_id
            print 'get version name error'

    def get_version_name(self):
        try:
            command = 'aapt dump badging ' + self.apkPath
            result = os.popen(command).readlines()
            for line in result:
                version_name_head = "versionName='"
                end = "' "
                if version_name_head in line:
                    print line
                    line = line[line.index(version_name_head) + len(version_name_head):]
                    version_name = line[:line.index(end)]
                    self.versionName = version_name
                    print version_name
                    del version_name, command, result, line, version_name_head, end
        except:
            print 'get version name error'
