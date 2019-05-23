from hacksport.problem import Remote, ProtectedFile
import string, random
import os, sys

class Problem(Remote):

    program_name = "pipe.py"
    
    def generate_flag(self,random):
        hexdigits = "{:08x}".format(random.randrange(16**8))
        return  "picoCTF{almost_like_mario_%s}" % hexdigits

    def initialize(self):
        self.index = self.random.randint(1000,4000)
