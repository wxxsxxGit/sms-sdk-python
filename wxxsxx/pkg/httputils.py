# -*- coding: utf-8 -*-
# from wxxsxx.pkg.strutils import RandString

def CurlStyleOutput(headers,requestBody,resp,method="POST",proto="HTTP/1.1"):
	#http://112.25.74.234:38080/sms/send/httpSendUser06
	#POST /sms/send/httpSendUser06 HTTP/1.1
	#Host: 112.25.74.234:38080
	#Content-Type: [application/json;charset=utf-8]
	#Authorization: [HMAC-SHA256 1665292677693,aFd23dI9fn0xzVsxBzo/D06zjbSGZ4gO6kOd8D+VLNo=]
	fullString = ""
	urlRight = resp.url.split("//")[1]
	urlSection = urlRight.split("/")
	host = urlSection[0]
	path = '/'+'/'.join(urlSection[1:])
	fullString = fullString + "=" * 20 + "\n"
	fullString = fullString + "http请求\n"
	fullString = fullString + "{method} {path} {proto}\n".format(method=method,path=path,proto=proto)
	fullString = fullString + "Host: {host}\n".format(host=host)
	for k, v in headers.items():
		fullString = fullString + "{key}: {value}\n".format(key=k,value=v)
	fullString = fullString + "\n"
	fullString = fullString + requestBody
	fullString = fullString + "\n"

	
	respStatus = str(resp.status_code)
	fullString = fullString + "http响应\n"
	fullString = fullString + "{proto} {status_code}\n".format(proto=proto,status_code=respStatus)
	for k, v in  resp.headers.items():
		fullString = fullString + "{key}: {value}\n".format(key=k,value=v)
	fullString = fullString + "\n"
	fullString = fullString + resp._content.decode("utf-8")
	fullString = fullString + "\n"
	fullString = fullString + "=" * 20 + "\n"
	return fullString