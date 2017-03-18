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

count=0
for line in data2:
    line0=line.split()[0]
    line1=line.split()[1]
    if line0 in data1:
        print line0,line1
        count+=1
print count