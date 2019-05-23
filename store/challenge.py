
from hacksport.problem_templates import Compiled, Remote

class Problem(Compiled, Remote):

    program_name = "store"
    compiler_sources = ["store.c"]

    def generate_flag(self, random):
        hexdigits = "{:08x}".format(random.randrange(16**8))
        return  "picoCTF{numb3r3_4r3nt_s4f3_%s}" % hexdigits
