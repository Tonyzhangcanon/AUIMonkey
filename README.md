## AUIMonkey
> Jenkins 执行 Monkey, 发送报告

### 执行相关:
#### 执行前配置:
##### 配置文件:
- AUICrawler
  - config
    - Setting.py
##### 设置项详解:
```
seed    : monkey 参数
throttle    : monkey 参数
events  : monkey 参数

UnInstallApk : 是否在执行前卸载 测试App/被测App
InstallApk : 是否在执行前安装 测试App／被测App

SMTP_HOST : SMTP服务器地址 
Mail_To_List : 测试报告邮件发送给哪些人
Mail_User : 使用哪个邮箱账号发送测试报告
Mail_Pass : 使用的邮箱账号的登录密码
```
#### 执行脚本:
- AUIMonkey
  - monkey.py
#### 参数执行:
##### 参数：
```
-a xxxx     : 指定被测Apk路径 ， Jenkins中可以用 ${WORKSPACE}+安装包子目录拼接
-b xxxx     : 用来在报告中显示Jenkins中该版本的超链，传入 ${BUILD_URL},&{BUILD_ID}
-d xx,xx    : 指定设备执行，传入设备id，多设备 a,b,c  , 不传则使用服务器连接的所有设备
-e 100      : monkey 参数 event , 执行多少个事件， 默认10000
-i          : 是否安装，使用则安装，需结合 -a 一起使用
-n xxx      : 如果不安装直接执行，并不知道应用名称，可以指定应用名称，在报告中显示
-p xxx      : 如果不安装直接执行，需要传入被测应用的包名，com.xxx.xxx
-s xxx      : monkey 参数 seed ，两次传入相同的seed值，事件顺序相同 ,默认100
-t xxx      : monkey 参数 throttle ，事件中的间隔时间，毫秒，用来控制压力，默认100
-u          : 是否卸载，与 -a 结合使用，传入-u 可以不传入-i，也会安装
-w xxx      : 传入${JENKINS_URL}，用来拼接设备的monkey Log 超链，在报告中显示
```
##### 示例场景：
1. 指定apk快速monkey
```
cd Jenkins中AUIMonkey目录
python monkey.py -a ${WORKSPACE}/build/ui/outputs/apk/xxx-xxx.apk -b ${BUILD_URL},&{BUILD_ID} -iw ${JOB_URL}
```
* 自由组合参数执行，默认执行模式：所有设备、不重新安装、不初始化、按序执行所有控件、不截图、Crash／ANR就停止、过程中不登录
* 可以修改Setting调整默认的执行模式
### 脚本结构:
#### 封装的模块:
##### 所在目录:
- AUIMonkey
  - module
##### 模块介绍:
```
monkey_plan :  本次执行的相关配置 & 运行状态等信息 
monkey_app :  当次执行时使用的App本身信息
monkey_device :  每个执行的Device的本身信息 
```
#### 执行记录:
##### 目录结构:
- AUIMonkey
  - result
    - 2017xxxxxxxxxx : 目录名称时间执行的测试计划
      - Result.html : 测试报告
      - 设备ID
        - monkey.txt : 此设备执行时monkey记录
        - logcat.txt : 此设备执行时详细Log
##### 本地目录
- AUImonkey
  - result
    - 2017xxxxxxxxxx
      - Result.html 
      
##### 发送邮件报告
```
在Setting.py中配置邮件信息
遍历结束后将报告发送给对应的接收人
不设置不会发送，不会报异常
```
##### 邮件报告显示
> 不同的邮件客户端 ／ 浏览器，邮件显示会不同
> html临时接触，所以在显示时可能会有些小问题， 如果有前辈可以帮助调整可以联系我，教教我，谢谢
### 开发进度:
- [x] 1.  架构设计
- [x] 2.  执行逻辑
- [x] 3.  配置信息
- [x] 4.  参数设计
- [x] 5.  报告设计
- [x] 6.  报告发送

> QQ：553410327 ，欢迎前辈指导，同学交流 
