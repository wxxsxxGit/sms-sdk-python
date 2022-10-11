# sms-sdk-python

sms http protocol sdk

# 开发帮助文档

- [【V4】短信服务API接入-帮助文档][]
- [【V4】短信服务 客户自助报备短信模板及其模板发送API接入-帮助文档][]
- [【V4】短信服务接入协议错误码对照表][]
- [【V4】短信运营商失败状态码一览表][]

[【V4】短信服务API接入-帮助文档]:https://api-wiki.wxxsxx.com
[【V4】短信服务 客户自助报备短信模板及其模板发送API接入-帮助文档]:https://www.yuque.com/docs/share/8446f03b-5132-4e87-b8d6-48b9cee0846a
[【V4】短信服务接入协议错误码对照表]:https://thoughts.teambition.com/share/5f22592404ce5e001a397794

[【V4】短信运营商失败状态码一览表]:https://thoughts.teambition.com/share/62f9aa40f3d36d0041586a7f#title=运营商短信失败状态码一览表

# 操作步骤

### python环境
脚本在python3.10.7以及3.6.8 通过测试

### git下载sdk
```
git clone https://github.com/wxxsxxGit/sms-sdk-python
```

### 进入虚拟环境

进入下载的sms-sdk-python目录执行命令
创建虚拟环境
```         
python -m venv env
```

### 进入虚拟环境
进入下载的sms-sdk-python目录执行命令
windows环境下
```
 .\env\Scripts\activate
 ```
linux环境下
```
source env/bin/activate
```

### 安装依赖文件
进入下载的sms-sdk-python目录执行命令
```
pip install -r requirements.txt
```

### 配置文件
进入下载的sms-sdk-python目录执行命令
```
创建config目录
在config目录下添加配置文件
配置文件名字为sms.yaml
```
配置文件内容如下,配置信息联系运营获取
```
spId: xxxxxxxxx
spKey: xxxxxxxxx
smsSendUrl: xxxxxxxxx
reportUrl: xxxxxxxxx
templateUrl: xxxxxxxxx
```

### 运行文件
进入下载的sms-sdk-python目录执行命令
```
python main.py
```
