from local_vars import (
    debug, version
)

class log(object):
    def __init__(self):
        super(log,self).__init__()
        self.data:str = '-=- Hagia Debug Log File -=-\n\nVersion: {}\n'.format(str(version[0])+'.'+str(version[1])+'.'+str(version[2]))

    def add(self,string):
        self.data+=str(string)

    def export(self):
        if debug:
            with open('hagia_log.txt','w') as log_file:
                log_file.write(self.data)
