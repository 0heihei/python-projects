#encoding=cp936
#Ŀ�ģ���һƪ�������ҳ�����������������

f = open('eg_text.txt', 'r')
    data = f.read()
    data = data.lower()
for ch in ",.;~!@#$%^&*()_+=-:":
    data = data.replace(ch, ' ')
data = data.split()

count = 0
for line in open("�������ʿ�.txt"):  # in�Ķ���ֻ����open(file),������������������
    line0 = line.split()[0]  # ���򲻻��������֪��Ϊʲô
    line1 = line.split()[1]
    if line0 in data:
        print line0, line1
        count += 1
print count

f.close()

