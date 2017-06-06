# encoding = utf-8

class IdApp:
	def __init__(self, inter):
		self.interface = inter

	def calc(self, ID):
		ID1 = str(ID)
		if len(ID1) != 18:
			check = "wrong ID number"
			where = 'null'
			gender = 'null'
		else:
			ID1_check = ID1[17]
			W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
			ID1_num = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
			ID1_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
			ID1_aXw = 0
			for i in range(len(W)):
				ID1_aXw = ID1_aXw + int(ID1[i]) * W[i]
			ID1_Check = ID1_aXw % 11
			if ID1_check != ID1_CHECK[ID1_Check]:
				check = "wrong ID number"
				where = 'null'
				gender = 'null'
			else:
				check = "right ID number"

				ID1_add = ID1[0:6]
				ID1_birth = ID1[6:14]
				ID1_sex = ID1[14:17]
				code_sites = {}
				for line in open('code_addr.txt', 'r').readlines():
					code_sites[line.split()[0].strip('\xe3\x80\x80')] = line.split()[1].strip('\xe3\x80\x80')

				Sheng = code_sites[ID1_add[0:2] + "0000"]
				Shi = code_sites[ID1_add[0:4] + "00"]
				Xian = code_sites[ID1_add]
				where = Sheng + Shi + Xian

				year = ID1_birth[0:4]
				month = ID1_birth[4:6]
				day = ID1_birth[6:8]

				if int(ID1_sex) % 2 == 0:
					gender = "female"
				else:
					gender = "male"
		return check, where, gender

	def run(self):
		while True:
			ID, flag = self.interface.getInfo()
			if flag:
				break
			if self.interface.ready == 'ok':
				check,where,gender=self.calc(ID)
				self.interface.showInfo(check,where,gender)
