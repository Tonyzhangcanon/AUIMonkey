# -*- coding: utf-8 -*-

from __future__ import print_function
import smtplib
from email.mime.text import MIMEText
from config import setting


def send_mail(plan):
    me = "AUIMonkey" + "<" + setting.Mail_User + ">"
    msg = MIMEText(plan.resultHtml, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"Monkey测试报告 - " + str(plan.runBeginTime)
    msg['From'] = me
    msg['To'] = ";".join(setting.Mail_To_List)
    try:
        s = smtplib.SMTP()
        s.connect(setting.SMTP_HOST)
        s.login(setting.Mail_User, setting.Mail_Pass)
        s.sendmail(me, setting.Mail_To_List, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print(str(e))
        return False
