#encoding=cp936
#Ŀ�ģ�ͳ��������ÿ�����ʳ��ֵ�Ƶ����������Ҫ����

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

#���潫�ֵ䰴��value�Ĵ�С������
data_dict= sorted(data_dict.iteritems(), key=lambda d:d[1], reverse = True)
print data_dict

f.close()

