from hacksport.problem import PHPApp, ProtectedFile, files_from_directory
from string import digits
from random import Random

class Problem(PHPApp):
	files = files_from_directory("webroot/") 
	php_root = "webroot/"
	flagPartLen = 4

	flag = ''

	def initialize(self):
		random = Random()
		flag = 'picoCTF{clients_are_bad' + ''.join(random.choice(digits + 'abcdef') for _ in range(8)) + '}'
		self.flag1 = self.flag[0:self.flagPartLen]
		self.flag2 = self.flag[self.flagPartLen:self.flagPartLen*2]
		self.flag3 = self.flag[self.flagPartLen*2:self.flagPartLen*3]
		self.flag4 = self.flag[self.flagPartLen*3:self.flagPartLen*4]
		self.flag5 = self.flag[self.flagPartLen*4:self.flagPartLen*5]
		self.flag6 = self.flag[self.flagPartLen*5:self.flagPartLen*6]
		self.flag7 = self.flag[self.flagPartLen*6:self.flagPartLen*7]
		self.flag8 = self.flag[self.flagPartLen*7:]


	def generate_flag(self, random):
		hexdigits = "{:06x}".format(random.randrange(16**6))
		return  "picoCTF{client_is_bad_%s}" % hexdigits
  
