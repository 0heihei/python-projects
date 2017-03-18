# encoding=cp936
#目的：批量查单词
import urllib2
#数目太多的话还是访问不过来,应该加上  超时时间设置

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
        if start > 0:            # 当找不到那些序列时就会返回 -1，因此可以用大于0筛选
            return data[start + 15: end]
        else:
            return '单词不存在'

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



