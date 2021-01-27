import time
import platform

class Logging:
    def __init__(self):
        self.file = open('.log', 'a')


    def __del__(self):
        self.file.close()


    def sys(self):
        self.file.write('[{}] Running on {} {}\n'.format(
                            time.ctime(),
                            platform.system(),
                            platform.release()))


    def tell(self, info):
        self.file.write(f'[{time.ctime()}] {info}\n')