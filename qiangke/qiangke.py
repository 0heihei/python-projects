# overwrited from https://www.sfantree.com/python-crack-lesson/
import requests
import urllib.request
import urllib.parse
import os,sys
import http.cookiejar
import zlib

vfcode_url="https://jaccount.sjtu.edu.cn/jaccount/captcha?14957079766180.7224017846671493"
post_url="https://jaccount.sjtu.edu.cn/jaccount/ulogin"

usr="duanyunzhi"
pwd="sjtu184052"

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)

vfcode=opener.open(vfcode_url).read()
with open('验证码.png','wb') as f:
	f.write(vfcode)
os.startfile("验证码.png")
captcha=input("输入验证码：")

formData={
    'sid':'jaxuanke091229',
    'returl':'CI/zQ3qiD2etDbXNm7ITwBEEhUvg5WmdDYwxCh34AvXYZVO1AcfDwa/IPMYzphVwbpntxFJMVRy2',
    'se':'CDu+MoSxU/HIRGu55yiEf7LiAYt275JAWZWayVHbRqiHPrYEUSvIA4A=',
    'v':'',
    'user':'duanyunzhi',
    'pass':'sjtu184052',
	'captcha':captcha
}
formData=urllib.parse.urlencode(formData).encode("utf8")

headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2,zh-TW;q=0.2',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'JSESSIONID=B8C8DCC935D3CC5E02140CCA436298C3.jaccount105; JAVisitedSites="CEDRWQ2LiPn6iCcHyZHGoTyCxH/ho7wuGGkhwDZyFuMZmGXmrAVMuDk="; JACCOUNT=jaccount.jaccount105',
'DNT':'1',
'Host':'jaccount.sjtu.edu.cn',
'Origin':'https://jaccount.sjtu.edu.cn',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
req=urllib.request.Request(post_url,formData,headers)
res=opener.open(req)
print(zlib.decompress(res.read(),16+zlib.MAX_WBITS).decode('utf8'))
