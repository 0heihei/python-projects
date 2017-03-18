# encoding=utf-8
# Author: Cloud Sophier
# Date:2017/3/18
# version: 1.0
"""
	程序类型：OOP
	库：poplib、smtplib、email 前两个分别负责收发邮件，最后一个负责解析和构造邮件
	实现的功能：登录邮箱，查看邮件总数，查看指定邮件，邮件发送\转发\删除等
	参考资料：廖大《leanring python3》教程；poplib、smtplib、email官方文档；MIME邮件格式分析的博文（blog.csdn.net/xjbclz/article/details/51912725）
"""
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class Email:
	def __init__(self):
		self.email_info = ''
		self.server = input('输入pop服务器地址：')
		self.usr = input('请输入邮箱地址：')
		self.psw = input('请输入邮箱pop服务密码：')

	def login(self):
		self.server1 = poplib.POP3_SSL(self.server)  # ssl
		self.server1.set_debuglevel(0)
		self.server1.user(self.usr)
		self.server1.pass_(self.psw)
		print('成功登录！')
		return

	def load(self):  # 为了使等待时不至太尴尬
		print('loading...')

	def get_mail_sum(self):
		resp, mails, octets = self.server1.list()
		self.sum = len(mails)
		return self.sum

	def get_msg(self, index):
		self.index = index
		resp, lines, octets = self.server1.retr(index)
		self.msg_content = b'\r\n'.join(lines).decode('utf8')
		self.msg = Parser().parsestr(self.msg_content)
		return self.msg

	def save_file(self, fname, data, pattern='wb'):
		try:
			with open(fname, pattern) as f:
				f.write(data)
			print('文件已另存为：%s' % fname)
		except Exception as err:
			print('保存文件出现问题:', err)

	def parse_email(self, msg, indent=0, disp='all'):
		# 用来解析头文件比如 subject，from等
		def decode_hdr(hdr):
			# 可以查看decode_header的源代码，其返回的是包含元组的list
			value, charset = decode_header(hdr)[0]
			if charset:
				value = value.decode(charset)
				return value

		def check_charset(msg):
			charset = msg.get_charset()
			if charset is None:
				content_type = msg.get('Content-Type', '').lower()
				pos = content_type.find('charset=')
				if pos >= 0:
					charset = content_type[pos + 8:].strip()
			return charset

		if indent == 0:
			print('--------------------邮件编号：%s--------------------' % self.index)
			for header in ['Subject', 'To', 'From', 'Date']:
				value = msg.get(header)
				if value:  # 即如果能get到，相当于试错，好方法
					if header == "Subject":
						# subject只有一个元素
						value = decode_hdr(value)
						self.subject = value
					elif header == "Date":
						value = value
					else:
						# name就是发邮件时  msg['From']='***'的产物
						name, addr = parseaddr(value)
						name = decode_hdr(name)
						value = u'%s <%s>' % (name, addr)
						if header == "From":
							self.From = value
						else:
							self.To = value
					if disp == 'all':
						print('%s%s:%s' % ('  ' * indent, header, value))
			self.email_info += '【这是一封由 %s 向 %s 发的邮件， 主题为：%s】' % (self.From, self.To, self.subject)
		if disp == 'all':
			# 如果是多重的格式，递归输出
			if (msg.is_multipart()):
				# get_payload返回一个list,包含所有的子对象
				parts = msg.get_payload()
				for n, part in enumerate(parts):
					print('%spart %s' % ('  ' * indent, n + 1))
					print('%s-------------' % (' ' * indent))
					self.parse_email(part, indent + 1)  # 递归
			else:
				# 否则用 content_type 判断格式，分两种情况
				content_type = msg.get_content_type()
				if content_type == 'text/plain' or content_type == 'text/html':
					content = msg.get_payload(decode=True)
					charset = check_charset(msg)
					if charset:
						content = content.decode(charset)
					if content_type == 'text/html':
						if input('此邮件为HTML格式，当前客户端无法查看。你可以：\n输入"1"查看源码（之后你可以保存源码用浏览器打开查看），否则直接回车即可:') == '1':
							self.save_file('email%s.html' % self.index, content, pattern='w')
					else:
						print('%sText:%s' % ('  ' * indent, content))
				else:
					# 对附件的处理
					filename = msg.get_filename()
					charset = check_charset(msg)
					if filename:
						h = Header(filename)
						dh = decode_header(h)
						fname = dh[0][0]
						encode_str = dh[0][1]
						if encode_str != None:
							if charset == None:
								fname = fname.decode(encode_str, 'gbk')
							else:
								fname = fname.decode(encode_str, charset)
						data = msg.get_payload(decode=True)
						print('attachment:' + fname)
						self.save_file('附件%s' % self.index + fname, data)

	def send_mail(self, text, receivers, original_msg=0, subject=0):
		try:
			msg = MIMEMultipart()
			if not original_msg == 0:
				msg.attach(original_msg)
				subject = '邮件转发'
			else:  # 没原文本消息，即不是转发，而是发邮件
				subject = subject
			msg.attach(MIMEText(text, 'plain', 'utf8'))

			msg['Subject'] = Header(subject, 'utf-8')
			msg['From'] = str(self.usr)
			msg['To'] = ';'.join(receivers)  # 多个收件人

			self.server2 = smtplib.SMTP('smtp.163.com', 25)
			self.server2.set_debuglevel(0)
			self.server2.login(self.usr, self.psw)
			self.server2.sendmail(self.usr, receivers, msg.as_string())
			self.server2.quit()
			print('发送成功！')
		except Exception as error:
			print(error)
		return

	def dele_mail(self, index):
		try:
			self.server1.dele(index)
			print('成功删除第%s封邮件' % index)
		except:
			print('当前服务器不支持pop删除邮件')


if __name__ == '__main__':
	while True:
		try:
			hdlMail = Email()
			hdlMail.load()
			hdlMail.login()
			break
		except:
			print('服务器或账号或密码错误')

	while True:
		print("""Options:
	1 查看收件箱总邮件数
	2 查看最近的5封邮件
	3 查看指定的一封邮件
	4 发送邮件
	5 转发邮件
	6 删除邮件
	7 退出程序""")
		cmd = input('>>>')
		try:
			if cmd == '1':
				amount = hdlMail.get_mail_sum()
				print('您当前收件箱中共有%s封邮件' % amount)
			elif cmd == '2':
				hdlMail.load()
				for i in range(5):
					msg = hdlMail.get_msg(amount - i)
					hdlMail.parse_email(msg)
			elif cmd == '3':
				index = input('请输入要查看的email的序号（1~%s）' % amount)
				hdlMail.load()
				msg = hdlMail.get_msg(index)
				hdlMail.parse_email(msg)
			elif cmd == '4':
				subject = input('请输入主题：')
				text = input('请输入文本内容：')
				num = int(input('你想要发给多少人？'))
				receivers = []
				for i in range(0, num):
					receiver = input('请输入一个收件人的email地址：')
					receivers.append(receiver)
				hdlMail.load()
				hdlMail.send_mail(text, receivers, subject=subject)
			elif cmd == '5':
				index = input('请输入要转发的email的序号（1~%s）' % amount)
				hdlMail.load()
				original_msg = hdlMail.get_msg(index)
				hdlMail.parse_email(original_msg, disp='part')  # 只得到原邮件的收发人信息，对正文不做解析（转发的是原文本
				text = hdlMail.email_info
				print(text)
				num = int(input('你想要发给多少人？'))
				receivers = []
				for i in range(0, num):
					receiver = input('请输入一个对方的email地址：')
					receivers.append(receiver)
				hdlMail.load()
				hdlMail.send_mail(text, receivers, original_msg=original_msg)
			elif cmd == '6':
				index = int(input('请输入要删除的邮件的编号：'))
			elif cmd == '7':
				break
			else:
				print('输入有误，请重新输入！')
				continue
		except Exception as err:
			print('出现错误：%s\n已为你自动刷新' % err)
