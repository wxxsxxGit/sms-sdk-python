# -*- coding: utf-8 -*-
from wxxsxx.pkg.httputils import CurlStyleOutput
from wxxsxx.pkg.strutils import NormalizeKey,RandString
from wxxsxx.pkg.encrypt import AesECBEncrypt,HmacSha256AndBase64
from wxxsxx.smsutils.signer import SmsSigner
import yaml
import requests
import json
import time
import logging
import datetime
import os




with open("config/sms.yaml", encoding='utf-8') as fr:
    config = yaml.safe_load(fr)
    
smsSigner =  SmsSigner(config["spId"],config["spKey"],config["smsSendUrl"],config["reportUrl"],config["templateUrl"])
fileToWrite = open("http_details.txt",'w',encoding=("utf-8"))  


def demoSingleSend():
    requestBody = {
        "content": "【线上线下】您的验证码为123456，在10分钟内有效。",
        "mobile":  "13800001111,13955556666,13545556666",
        "extCode": "123456",
        "sId":     "123456789abcdefg"}
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.SingleSendUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoSingleSend()状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        
def demoSingleSecureSend():
    requestBody = {
         "content": "【线上线下】您的验证码为123456，在10分钟内有效。我当然没问题",
         "mobile":  "13800001111",
         "extCode": "123456",
         "sId":     "123456789abcdefg"}
    tempReqBody = json.dumps(requestBody,ensure_ascii=False)
    # tempReqBody = json.dumps(requestBody,ensure_ascii=False)
    tempReqBody = '''{"content":"【线上线下】您的验证码为123456，在10分钟内有效。","mobile":"13800001111,13955556666,13545556666","extCode":"123456","sId":"123456789abcdefg"}'''
    contentString = AesECBEncrypt(tempReqBody, NormalizeKey(smsSigner.SpKey))
    secondReqBody = {"content":contentString}
    finalReqBody = json.dumps(secondReqBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.SingleSecureSendUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoSingleSecureSend()状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        
        
def demoMultiSend():
    smsBody1 = {
        "content": "【线上线下】线上线下欢迎你参观1",
        "mobile":  "13800001111,8613955556666,+8613545556666",
        "extCode": "123456",
        "msgId":   "123456787"}

    smsBody2 = {
        "content": "【线上线下】线上线下欢迎你参观2",
        "mobile":  "13800001111,8613955556666,+8613545556666",
        "extCode": "123456",
        "msgId":   "123456787"}

    smsBody3 = {
        "content": "【线上线下】线上线下欢迎你参观3",
        "mobile":  "13800001111,8613955556666,+8613545556666",
        "extCode": "123456",
        "msgId":   "123456787"}

    requestBody = [smsBody1, smsBody2,smsBody3]
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.MultiSendUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoMultiSend()状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        
        
def demoStatusFetch():
    requestBody = {
        "maxSize": 500,
    }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.StatusFetchUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoStatusFetch()状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
    
def  demoUpstreamFetch():
    requestBody = {
        "maxSize": 500,
    }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.UpstreamFetchUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoUpstreamFetch()状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))

def demoBalanceFetch():
    headers = smsSigner.Sign("")
    resp = requests.post(smsSigner.StatusFetchUrl(),headers=headers,timeout=3)
    output = CurlStyleOutput(headers,"",resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoBalanceFetch()状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
    
def demoDailyStatsFetch():
    requestBody = {
        "date": datetime.datetime.now().strftime("%Y%m%d"),
        }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.DailyStatsUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoDailyStatsFetch状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
     
def demoTemplateAdd():
    requestBody = {
        "templateName":    "线上线下addTemplate SDK DEMO " + RandString(10),
        "templateType":    2,
        "templateContent": "线上线下addTemplate SDK DEMO template content ${code} template " + RandString(20),
        "remark":          "线上线下addTemplate SDK DEMO template " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.TemplateAddUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoTemplateAdd状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
    else:
        return respDict["templateCode"]    

def demoTemplateModify(templateCode):
    requestBody = {
        "templateCode":    templateCode,
        "templateType":    2,
        "templateName":    "线上线下addTemplate SDK DEMO " + RandString(10),
        "templateContent": "线上线下addTemplate SDK DEMO template content ${code} modify template " + RandString(20),
        "remark":          "线上线下addTemplate SDK DEMO template " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
	}
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.TemplateModifyUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoTemplateModify状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        return respDict["status"]
    logging.info("模板修改成功")
    


    

#返回状态0,1,2,3 0是没审核 1审核通过 2审核失败 3禁用    
def demoTemplateStatus(templateCode):
    tList = [str(templateCode)]
    requestBody = {
        "templateCodes": ",".join(tList),
    }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.TemplateStatusUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoTemplateStatus状态码为"+resp.status_code)
        return
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        return 0

    for v in respDict["templateList"]:
        if v["templateCode"] == templateCode and v["status"] == 0:
            return v["auditStatus"]
    return 0

def demoTemplateDelete(templateCode):
    requestBody = {
        "templateCode": templateCode,
    }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.TemplateDeleteUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoTemplateDelete状态码为"+resp.status_code)
        return False
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        return False
    else:
        return True


def demoTemplateSendSms(templateCode):
    params = {
        "code": "本届预选赛"
    }
	
    paramsString = json.dumps(params)
    requestBody = {
        "signName":     "模板测试",
        "templateCode": templateCode,
        "params":       paramsString,
        "mobile":       "18799991367,12899190876,13914117531",
    }
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.TemplateSendSmsUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoTemplateSendSms()状态码为"+resp.status_code)
        return False
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        return False
    else:
        return True

def demoTemplateSendBatchSms(templateCode):
    params = {
        "code": "本届预选赛"
    }
    paramsString = json.dumps(params)
    item1 = {
        "signName":     "模板测试1",
        "templateCode": templateCode,
        "params":       paramsString,
        "mobile":       "18505101387",
    }
    item2 = {
        "signName":     "模板测试2",
        "templateCode": templateCode,
        "params":       paramsString,
        "mobile":       "12899190872",
    }
    item3 = {
        "signName":     "模板测试3",
        "templateCode": templateCode,
        "params":       paramsString,
        "mobile":       "18799991362",
    }
    item4 = {
        "signName":     "模板测试4",
        "templateCode": templateCode,
        "params":       paramsString,
        "mobile":       "13914117532",
    }
    item5 = {
        "signName":     "模板测试5",
        "templateCode": templateCode,
        "params":       paramsString,
        "mobile":       "1895606996",
    }
    requestBody = [item1,item2,item3,item4,item5]
    finalReqBody = json.dumps(requestBody,ensure_ascii=False)
    headers = smsSigner.Sign(finalReqBody)
    resp = requests.post(smsSigner.TemplateSendBatchSmsUrl(),headers=headers,data=finalReqBody.encode("utf-8"),timeout=3)
    output = CurlStyleOutput(headers,finalReqBody,resp)
    fileToWrite.write(output)
    if resp.status_code != 200:
        logging.info("demoTemplateSendSms()状态码为"+resp.status_code)
        return False
    respDict = json.loads(resp._content)
    if respDict["status"] != 0:
        logging.info("status状态为"+str(respDict["status"]))
        return False
    else:
        return True

def sperator(sec):
    print("\n")
    time.sleep(sec)


def configPrompt():
    logging.info("配置文件默认为/etc/sms.yaml\n" +
    "需要5个配置项spId,spKey,smsSendUrl,reportUrl,templateUrl联系管理员获取")

	

if __name__ == "__main__":
    globalTemplateCode = ""
    console_fmt = "%(asctime)s--->%(message)s"
    logging.basicConfig(level="INFO",format=console_fmt)
    
    
    logging.info("短信发送接口（单内容多号码）")
    demoSingleSend()
    sperator(1)
    
    #单条内容加密发送
    logging.info("短信加密发送接口")
    demoSingleSecureSend()
    sperator(1)

	# #多内容批量发送
    logging.info("短信多发接口")
    demoMultiSend()
    sperator(1)

	# #主动获取状态报告
    logging.info("状态报告主动获取")
    demoStatusFetch()
    sperator(1)

	# #主动获取上行
    logging.info("上行主动获取")
    demoUpstreamFetch()
    sperator(1)

    # #查询余额
    logging.info("预付费账号余额查询")
    demoBalanceFetch()
    sperator(1)

    # #查询每日发送统计
    logging.info("获取发送账号spId的每日短信发送情况统计")
    demoDailyStatsFetch()
    sperator(1)

    # #模板报备
    logging.info("模板报备")
    globalTemplateCode = demoTemplateAdd()
    print("模板报备的code为{0}".format(globalTemplateCode))
    sperator(1)
    

    logging.info("等待模板审核...")
    finalAuditCode = 0
    while True:
        auditCode = demoTemplateStatus(globalTemplateCode)
        if auditCode != 0:
            finalAuditCode = auditCode
            break
        logging.info("模板还未审核，请联系管理员审核...")
        time.sleep(10)
    
    if finalAuditCode == 2:
        logging.info("模板审核未通过,尝试重新提交模板")
        demoTemplateModify(globalTemplateCode)
        os._exit(11)
    elif finalAuditCode == 3:
        logging.info("模板被禁用")
        os._exit(12)
    else:
        logging.info("模板审核通过")
        sperator(1)
    
    #模板发送单条短信
    logging.info("模板发送单条短信")
    demoTemplateSendSms(globalTemplateCode)
    sperator(1)

    #模板批量发送短信
    logging.info("模板发送批量短信")
    demoTemplateSendBatchSms(globalTemplateCode)
    sperator(1)    
    
    logging.info("10秒后将删除模板{0:d}".format(globalTemplateCode))
    time.sleep(10)
    deleteResult = demoTemplateDelete(globalTemplateCode)
    if deleteResult:
        logging.info("删除模板{0:d}成功".format(globalTemplateCode))
        
    fileToWrite.close()
    sperator(1)
    
    logging.info("http请求内容保存在http_details.txt文件中")