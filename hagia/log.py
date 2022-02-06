from local_vars import (
    debug, version
)

class log(object):
    def __init__(self):
        super(log,self).__init__()
        self.data:str = '-=- Pico-8 Debug Log File -=-\n\nVersion: {}\n'.format(str(version[0])+'.'+str(version[1])+'.'+str(version[2]))

    def add(self,string):
        self.data+=str(string)

    def export(self):
        if debug:
            with open('pyco8_log.txt','w') as log_file:
                log_file.write(self.data)