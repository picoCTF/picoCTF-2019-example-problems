from hacksport.problem_templates import Compiled
import base64

class Problem(Compiled):
    makefile = "Makefile"
    program_name = "radix"

    def generate_flag(self, random):
        bf = "picoCTF{bAsE_64_eNCoDiNg_iS_EAsY_}"
        hexdigits = "{:08}".format(random.randrange(16**8))
        while (((len(bf) + len(hexdigits))*8) % 6 != 0):
            hexdigits = hexdigits[:-1]
        return "picoCTF{bAsE_64_eNCoDiNg_iS_EAsY_%s}" % hexdigits

    def initialize(self):
        self.pwd = base64.b64encode((self.flag).encode()).decode()
