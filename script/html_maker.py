#-*- coding= utf-8 -*-


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
                '        body {\n' + \
                '          margin: 0;\n' + \
                '          font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;\n' + \
                '          font-size: 14px;\n' + \
                '          line-height: 20px;\n' + \
                '          color:  #333333;\n' + \
                '          background-color:  #ffffff;\n' + \
                '        }\n' + \
                '        a {\n' + \
                '           color:  #0088cc;\n' + \
                '           text-decoration: none;\n' + \
                '        }\n' + \
                '        .row {\n' + \
                '           margin-left: -20px;\n' + \
                '           *zoom: 1;\n' + \
                '        }\n' + \
                '        .row:before,\n' + \
                '        .row:after {\n' + \
                '           display: table;\n' + \
                '           line-height: 0;\n' + \
                '           content: "";\n' + \
                '        }\n' + \
                '        .row:after {\n' + \
                '           clear: both;\n' + \
                '        }\n' + \
                '        .container {\n' + \
                '           width: 940px;\n' + \
                '           margin-right: auto;\n' + \
                '           margin-left: auto;\n' + \
                '           *zoom: 1;\n' + \
                '        }\n' + \
                '        strong {\n' + \
                '           font-weight: bold;\n' + \
                '        }\n' + \
                '        h1 {\n' + \
                '           margin: 10px 0;\n' + \
                '           font-family: inherit;\n' + \
                '           font-weight: bold;\n' + \
                '           color: inherit;\n' + \
                '           text-rendering: optimizelegibility;\n' + \
                '           line-height: 40px;\n' + \
                '           font-size: 38px;\n' + \
                '        }\n' + \
                '        table {\n' + \
                '           max-width: 100%;\n' + \
                '           background-color: transparent;\n' + \
                '           border-collapse: collapse;\n' + \
                '           border-spacing: 0;\n' + \
                '        }\n' + \
                '        .table {\n' + \
                '           width: 100%;\n' + \
                '           margin-bottom: 20px;\n' + \
                '        }\n' + \
                '        .table th,\n' + \
                '        .table td {\n' + \
                '           padding: 8px;\n' + \
                '           line-height: 20px;\n' + \
                '           text-align: left;\n' + \
                '           vertical-align: top;\n' + \
                '           border-top: 1px\n' + \
                '           solid  #dddddd;\n' + \
                '        }\n' + \
                '        .table-bordered {\n' + \
                '           border: 1px solid  #dddddd;\n' + \
                '           border-collapse: separate;\n' + \
                '           *border-collapse: collapse;\n' + \
                '           border-left: 0;\n' + \
                '           -webkit-border-radius: 4px;\n' + \
                '           -moz-border-radius: 4px;\n' + \
                '           border-radius: 4px;\n' + \
                '        }\n' + \
                '        .table-bordered th,\n' + \
                '        .table-bordered td {\n' + \
                '           border-left: 1px solid  #dddddd;\n' + \
                '        }\n' + \
                '        .table tbody tr.success > td {\n' + \
                '           background-color:  #dff0d8;\n' + \
                '        }\n' + \
                '        .table tbody tr.error > td {\n' + \
                '           background-color:  #f2dede;\n' + \
                '        }\n' + \
                '        .table tbody tr.warning > td {\n' + \
                '           background-color:  #fcf8e3;\n' + \
                '        }\n' + \
                '        .table tbody tr.info > td {\n' + \
                '           background-color:  #d9edf7;\n' + \
                '        }\n' + \
                '        .table-hover tbody tr.success:hover > td {\n' + \
                '           background-color:  #d0e9c6;\n' + \
                '        }\n' + \
                '        .table-hover tbody tr.error:hover > td {\n' + \
                '           background-color:  #ebcccc;\n' + \
                '        }\n' + \
                '        .table-hover tbody tr.warning:hover > td {\n' + \
                '           background-color:  #faf2cc;\n' + \
                '        }\n' + \
                '        .table-hover tbody tr.info:hover > td {\n' + \
                '           background-color:  #c4e3f3;\n' + \
                '        }\n' + \
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
                    '                <td width="auto" class="txt_gray"><strong>Product Name：</strong></td>\n' + \
                    '                <td width="auto" align="left" >' + app.appName + '</td>\n' + \
                    '                <td width="auto"class="txt_gray"><strong>Package Name：</strong></td>\n' + \
                    '                <td width="auto" align="left">' + app.packageName + '</td>\n' + \
                    '                <td width="auto"class="txt_gray"><strong>Version Name：</strong></td>\n' + \
                    '                <td width="auto" align="left">' + app.versionName + '</td>\n' + \
                    '                <td width="auto"class="txt_gray"><strong>Version Code：</strong></td>\n' + \
                    '                <td width="auto" align="left">' + app.versionCode + '</td>\n' + \
                    '                <td width="auto"class="txt_gray"><strong>Version：</strong></td>\n' + \
                    '                <td width="auto" align="left">\n' + \
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
    for device in plan.deviceList:
        if device.result == "Passed":
            result_class = "success"
        elif device.result == "Crashed":
            result_class = "error"
        elif device.result == "ANR":
            result_class = "warning"
        else:
            result_class = "info"
        duration = (device.endTime-device.beginTime).seconds
        monkey_log_url = plan.workspace + '/result/' + plan.runBeginTime.strftime('%Y%m%d%H%M%S') + '/' + device.id + '/monkey.txt'
        logcat_url = plan.workspace + '/result/' + plan.runBeginTime.strftime('%Y%m%d%H%M%S') + '/' + device.id + '/logcat.txt'
        device_result_html = '              <tr class=' + result_class + '>\n' + \
                             '                <td>' + device.name + '</td>\n' + \
                             '                <td>' + device.id + '</td>\n' + \
                             '                <td>' + device.version + '</td>\n' + \
                             '                <td>\n' + \
                             '                  <a href=' + logcat_url + '>\n' + \
                             '                    <span>' + device.result + '</span>\n' + \
                             '                  </a>\n' + \
                             '                </td>\n' + \
                             '                <td>\n' + \
                             '                  <a href=' + monkey_log_url + '>\n' + \
                             '                    <span>' + str(duration) + ' Sec</span>\n' + \
                             '                  </a>\n' + \
                             '                </td>\n' + \
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
