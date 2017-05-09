# -*- coding:utf-8 -*-

import os
import sys
import html_maker


reload(sys)
sys.setdefaultencoding('utf-8')

log_tag = os.path.basename(os.getcwd())


def save_logcat(plan, device):
    command = 'adb -s ' + device.id + ' logcat -d >> ' + device.logPath + '/logcat.txt'
    os.system(command)
    del plan, device, command


def save_monkey_result(plan, app):
    result = html_maker.make_result_html(plan, app)
    result_file = open(plan.logPath + '/Result.html', 'w')
    result_file.write(result)
    result_file.close()
