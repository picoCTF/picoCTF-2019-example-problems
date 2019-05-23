from hacksport.problem import Challenge, File
import string, random

# TODO: make sure that 'file' apears in the problem directory
class Problem(Challenge):

    def setup(self):
        pass
    
    def generate_flag(self,random):
        hexdigits = "{:08x}".format(random.randrange(16**8))
        return  "picoCTF{grep_and_you_will_find_%s}" % hexdigits

    def initialize(self):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`|~ \t"
	# TODO: fix some of these random characters that are causing framework to break during deploy!
        open("file", "a").write(''.join(random.choice(characters) for _ in range(4000)) + '\n')
        open("file", "a").write(self.flag + '\n')
        open("file", "a").write(''.join(random.choice(characters) for _ in range(4000)) + '\n')
        open("file", "a").write(''.join(random.choice(characters) for _ in range(4000)) + '\n')
        open("file", "a").write(''.join(random.choice(characters) for _ in range(4000)) + '\n')
        open("file", "a").write('\n')
        self.files = [File('file')]
