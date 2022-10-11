# -*- coding: utf-8 -*-

import time
from wxxsxx.pkg.encrypt import HmacSha256AndBase64
class SmsSigner(object):
    def __init__(self,spId, spKey, smsSendUrl, reportUrl, templateUrl):
        #创建实例” 的方法 __init__(self,x,y)第一个参数永远是self，即实例本身
        self.SpId   = spId
        self.SpKey = spKey
        self.SmsSendUrl   = smsSendUrl
        self.ReportUrl  = reportUrl
        self.TemplateUrl = templateUrl

    def Sign(self, bodyString):
        currentTimestring = str(int(round(time.time() * 1000)))
        signature = HmacSha256AndBase64(bodyString,currentTimestring,self.SpKey)
        signatureHeader = "HMAC-SHA256" + " " + currentTimestring + "," + signature
        headers = {"Authorization":signatureHeader,"Content-Type":"application/json;charset=utf-8"}
        return headers

    #短信发送接口（单内容多号码）url
    def SingleSendUrl(self):
        return self.SmsSendUrl.rstrip("/") + "/sms/send/" + self.SpId


    #短信加密发送接口（影响性能，非必要不推荐）url
    def SingleSecureSendUrl(self):
        return self.SmsSendUrl.rstrip("/")+ "/sms/secureSend/" + self.SpId


    #多内容发送url
    def MultiSendUrl(self):
        return self.SmsSendUrl.rstrip("/") + "/sms/sendBatch/" + self.SpId

    #状态报告主动获取url
    def StatusFetchUrl(self):
        return self.ReportUrl.rstrip("/") + "/sms/getReport/" + self.SpId

    #上行主动获取url
    def UpstreamFetchUrl(self):
        return self.ReportUrl.rstrip("/") + "/sms/getUpstream/" + self.SpId

    #预付费账号余额查询url
    def  BalanceFetchUrl(self):
        return self.ReportUrl.rstrip("/") + "/sms/getBalance/" + self.SpId

    #获取发送账号日统计url
    def DailyStatsUrl(self):
        return self.ReportUrl.rstrip("/") +  "/sms/getDailyStats/" + self.SpId

    #报备模板url
    def TemplateAddUrl(self):
        return self.TemplateUrl.rstrip("/") +  "/sms/template/add/" + self.SpId


    #修改模板url
    def TemplateModifyUrl(self):
        return self.TemplateUrl.rstrip("/") +  "/sms/template/modify/" + self.SpId

    #删除模板url
    def TemplateDeleteUrl(self):
        return self.TemplateUrl.rstrip("/") + "/sms/template/delete/" + self.SpId

    #  查询模板状态url
    def TemplateStatusUrl(self):
        return self.TemplateUrl.rstrip("/") + "/sms/template/status/" + self.SpId

    #模板短信发送 单条发送url
    def  TemplateSendSmsUrl(self):
        return self.TemplateUrl.rstrip("/") +  "/sms/template/sendSms/" + self.SpId

    #模板短信发送  批量短信发送url
    def  TemplateSendBatchSmsUrl(self):
        return self.TemplateUrl.rstrip("/") + "/sms/template/sendBatchSms/" + self.SpId