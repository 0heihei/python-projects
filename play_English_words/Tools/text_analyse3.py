#encoding=cp936
#目的：从一篇文章中找出所包含的六级单词

f1=open('eg_text.txt','r')
f2=open('六级单词库.txt','r')

data1=f1.read()
data1=data1.lower()
for ch in ",.;~!@#$%^&*()_+=-:":
    data1=data1.replace(ch,' ')
data1=data1.split()

data2 = f2.readlines()
wordslist=[]
for line in data2:
    line0=line.split()[0]
    wordslist.append(line0)

count=0
for i in wordslist:
    if i in data1:
        print i
        count+=1
print count