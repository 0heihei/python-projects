# encoding=cp936
#Ŀ�ģ������鵥��
import urllib2
#��Ŀ̫��Ļ����Ƿ��ʲ�����,Ӧ�ü���  ��ʱʱ������

def haici(word):
    url = 'http://dict.cn/'
    url += word
    req = urllib2.Request(url, headers=headers)
    try:
        page=urllib2.urlopen(req)
    except:
        return
    else:
        data = page.read()
        index_begin = data.find('class=\"dict-basic-ul\"')
        start = data.find('</span><strong>', index_begin)
        end = data.find('</strong></li>', index_begin)
        if start > 0:            # ���Ҳ�����Щ����ʱ�ͻ᷵�� -1����˿����ô���0ɸѡ
            return data[start + 15: end]
        else:
            return '���ʲ�����'

f = open('eg_text.txt', 'r')
data = f.read()
data = data.lower()
for ch in ",.;~!@#$%^&*()_+=-:":
    data = data.replace(ch, ' ')
data = data.split()
f.close()

wordlist=[]
for word in data:
    if word in wordlist:
        pass
    else:
        print word,'  ',haici(word)
        wordlist.append(word)



