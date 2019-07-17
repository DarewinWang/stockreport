#!/usr/bin/python  
# -*- coding: utf-8 -*- 
import urllib2
import cookielib
import re
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

def sendMail():
    global information

    print "%"*25
    mail_host="smtp.sina.com"
    mail_user="tpwd@sina.com"
    mail_pass="##passwd##"

    sender = 'tpwd@sina.com'
    receivers = ['540677251@qq.com']
    #,'952198007@qq.com','563496091@qq.com'
    message = MIMEText(information, 'html', 'utf-8')
    message['From'] = Header("tpwd@sina.com")
    message['To'] =  Header("540677251@qq.com")

    subject = '券商今日最新研报'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "successful"


def getPage(url):
    global information
    headers = {'Connection':'keep-alive','User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 Chrome/45.0.2454.101 Safari/537.36'}
    req = urllib2.Request(url,headers = headers)
    result = urllib2.urlopen(req)
    result.encoding ='GBK'
    text = result.read()           # get web page html file

    p=re.compile("var data =.*;")
    mat=p.search(text)
    info=mat.group()[10:-1].decode("GBK")
    datas=json.loads(info)

    print mat.group()[10:-1]
    count=0
    for data in datas["data"]:
        url="http://data.eastmoney.com/report/"+data["datetime"][:4]+data["datetime"][5:7]+data["datetime"][8:10]+"/"+data["infoCode"]+".html"
        code="http://xueqiu.com/S/"+data["secuFullCode"][-2:]+data["secuFullCode"][:6]
        #code="\"xueqiu://S/"+data["secuFullCode"][-2:]+data["secuFullCode"][:6]+"\""

        count+=1
        if(data["rate"] is None or len(data["rate"]) == 0):
            continue

        information+="<b>"+data["secuName"].encode("UTF-8")+"</b>"+"&nbsp;&nbsp;&nbsp;"+data["sratingName"].encode("UTF-8")+"&nbsp;&nbsp;&nbsp;"+data["change"].encode("UTF-8")+"&nbsp;&nbsp;&nbsp;<a href="+code.encode("UTF-8")+">"+code[20:].encode("UTF-8")+"</a>"+"<p />研报：<a href="+url.encode("UTF-8")+">"+data["title"].encode("UTF-8")+"</a><br /><hr />"

        #print data[u"change"],data[u"insName"],data[u"rate"],data[u"secuName"],data[u"sratingName"],data[u"title"],data[u"newPrice"]

information="<h3>今日研报</h3><hr />"
url="http://data.eastmoney.com/report/"
getPage(url)
sendMail()
print 'this is end'

