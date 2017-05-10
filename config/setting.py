# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#  - * Plan Setting * -

#  - * Monkey setting * -
seed = 100  # -s
throttle = 100  # -t
events = 10000 # -e


#  - * Apk Install Setting * -
UnInstallApk = False  # True (uninstall app & testApp) , False
InstallApk = False  # True (install app & testApp) ,False

#  - * send crawl result email * -
SMTP_HOST = "smtp.xxx.xxx"  # Set mail smtp host
Mail_To_List = ["xxx@xxx.xxx"]  # who will receive the result mail "quality@dewmobile.net"
Mail_User = "xxx@xxx.xxx"  # which account will be Use to send mail
Mail_Pass = "xxx"  # the password for login
