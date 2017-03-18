#encoding=cp936
#目的：统计文章中每个单词出现的频数来查找重要单词

f = open('eg_text.txt', 'r')
data = f.read()
data = data.lower()
for ch in ",.;~!@#$%^&*()_+=-:":
    data = data.replace(ch, ' ')
data = data.split()

data_dict={}
for word in data:
    data_dict[word]=0

for word in data:
    if word in data_dict:
        data_dict[word] +=1

#下面将字典按照value的大小来排序
data_dict= sorted(data_dict.iteritems(), key=lambda d:d[1], reverse = True)
print data_dict

f.close()

