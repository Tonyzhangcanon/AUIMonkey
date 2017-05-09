# -*- coding= utf-8 -*-


def make_result_html(plan, app):
    html_head = '<!doctype html>\n' + \
                '<html lang="en-US">\n' + \
                '  <head>\n' + \
                '    <meta charset="UTF-8" >\n' + \
                '    <title>Android Monkey Test Result</title>\n' + \
                '    <link rel="stylesheet" type="text/css" href="bootstrap.css"/>\n' + \
                '    <style type="text/css">\n' + \
                '      body {\n' + \
                '          margin: 0;\n' + \
                '      }\n' + \
                '      #main{\n' + \
                '          height: 1000px;\n' + \
                '      }\n' + \
                '      #footer {\n' + \
                '        bottom: 0px;\n' + \
                '        color: #666;\n' + \
                '        width: 98%;\n' + \
                '        height: 30px;\n' + \
                '        clear: both;\n' + \
                '        position: fixed;\n' + \
                '      }\n' + \
                '    </style>\n' + \
                '  </head>\n'
    html_body_head = '   <body>\n' + \
                     '    <div id="main" class="container">\n' + \
                     '      <div class="row">\n' + \
                     '        <div>\n' + \
                     "          <h1 Align='center'>\n" + \
                     "            <span style='font-size:30px;font-weight:normal;font-style:normal;text-decoration:none;color:rgb(87, 191, 135);'><strong>Android Monkey 测试报告</strong></span>\n" + \
                     '          </h1>\n' + \
                     '        </div>\n' + \
                     '        <div>\n' + \
                     '          <h1 style="font-size:30px;color: rgb(87, 191, 135)">App Info</h1>\n' + \
                     '        </div>\n' + \
                     '        <br>\n' + \
                     '        <div>\n'
    html_app_info = '          <table width="100%" cellpadding="0" border="0" cellspacing="0" style="border:none;">\n' + \
                    '            <tbody>\n' + \
                    '              <tr>\n' + \
                    '                <td width="110" class="txt_gray"><strong>Product Name：</strong></td>\n' + \
                    '                <td width="100" align="left" >' + app.appName + '</td>\n' + \
                    '                <td width="120"class="txt_gray"><strong>Package Name：</strong></td>\n' + \
                    '                <td width="170" align="left">' + app.packageName + '</td>\n' + \
                    '                <td width="110"class="txt_gray"><strong>Version Name：</strong></td>\n' + \
                    '                <td width="70" align="left">' + app.versionName + '</td>\n' + \
                    '                <td width="110"class="txt_gray"><strong>Version Code：</strong></td>\n' + \
                    '                <td width="30" align="left">' + app.versionCode + '</td>\n' + \
                    '                <td width="50"class="txt_gray"><strong>Version：</strong></td>\n' + \
                    '                <td width="30" align="left">\n' + \
                    '                  <a href=' + app.buildUrl + '>\n' + \
                    '                    <span>\n' + \
                    '                      ' + app.buildVersion + '\n' + \
                    '                    </span>\n' + \
                    '                  </a>\n' + \
                    '                </td>\n' + \
                    '              </tr>\n' + \
                    '            </tbody>\n' + \
                    '          </table>\n'
    html_result_head = '         </div>\n' + \
                       '        <br>\n' + \
                       '        <div>\n' + \
                       '          <h1 style="font-size:30px;color: rgb(87, 191, 135)">Results</h1>\n' + \
                       '          <table class="table table-bordered">\n' + \
                       '            <thead>\n' + \
                       '              <tr>\n' + \
                       '                <th>Device</th>\n' + \
                       '                <th>ID</th>\n' + \
                       '                <th>Version</th>\n' + \
                       '                <th>Result</th>\n' + \
                       '                <th>Duration</th>\n' + \
                       '              </tr>\n' + \
                       '            </thead>\n' + \
                       '            <tbody>\n'
    html_device_list = ''
    for device in plan.device_list:
        if device.result == "Passed":
            result_class = "success"
        else:
            result_class = "error"
        duration = (device.endTime - device.beginTime).seconds
        monkey_log_url = plan.workspace + '/result/' + plan.runBeginTime.strftime('%Y%m%d%H%M%S') + '/' + device.id + '/monkey.txt'
        device_result_html = '              <tr class=' + result_class + '>\n' + \
                             '                <td>' + device.name + '</td>\n' + \
                             '                <td>' + device.id + '</td>\n' + \
                             '                <td>' + device.version + '</td>\n' + \
                             '                <td>\n' + \
                             '                  <a href=' + monkey_log_url + '>\n' + \
                             '                    <span>' + device.result + '</span>\n' + \
                             '                  </a>\n' + \
                             '                </td>\n' + \
                             '                <td>' + str(duration) + ' Sec</td>\n' + \
                             '              </tr>\n'
        html_device_list += device_result_html
    html_end = '             </tbody>\n' + \
               '          </table>\n' + \
               '        </div>\n' + \
               '      </div>\n' + \
               '    </div>\n' + \
               '    <div  id = "footer" Align=\'right\'>\n' + \
               '      <span style="font-size:10px;font-weight:normal;font-style:normal;text-decoration:none;">\n' + \
               '　　    Dev : Zhiyang .\n' + \
               '      </span>\n' + \
               '    </div>\n' + \
               '    <script src="jquery.min.js"></script>\n' + \
               '    <script src="bootstrap.js"></script>\n' + \
               '  </body>\n' + \
               '</html>\n'
    result = html_head + html_body_head + html_app_info + html_result_head + html_device_list + html_end
    plan.resultHtml = result
    return result
