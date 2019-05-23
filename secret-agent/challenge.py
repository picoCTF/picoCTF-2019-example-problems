from hacksport.problem import FlaskApp, File
from hacksport.operations import execute

class Problem(FlaskApp):
    files = [File("templates/index.html"), File("templates/flag.html")]
    
    def generate_flag(self, random):
        hexdigits = "{:08x}".format(random.randrange(16**8))
        return  "picoCTF{s3cr3t_ag3nt_m4n_%s}" % hexdigits
