#encoding=cp936
#目的：从一篇文章中找出所包含的六级单词

f = open('eg_text.txt', 'r')
    data = f.read()
    data = data.lower()
for ch in ",.;~!@#$%^&*()_+=-:":
    data = data.replace(ch, ' ')
data = data.split()

count = 0
for line in open("六级单词库.txt"):  # in的对象只能是open(file),而不能是其它变量名
    line0 = line.split()[0]  # 否则不会输出，不知道为什么
    line1 = line.split()[1]
    if line0 in data:
        print line0, line1
        count += 1
print count

f.close()

