import requests
import os


def main():
    for i in range(0, 100):
        print("正在下载第%s张验证码" % str(i))
        file_path = path + str(i) + '.jpg'
        r = requests.get('https://jaccount.sjtu.edu.cn/jaccount/captcha?')
        with open(file_path, 'bw') as f:
            f.write(r.content)


path = './images/'
if os.path.exists(path):
    pass
else:
    os.makedirs(path)

if __name__ == '__main__':
    main()
