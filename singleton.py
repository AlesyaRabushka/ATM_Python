from datetime import datetime

class Singleton():
    _instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, error: str, status: bool, error_type:str):
        fo = open('log.txt', 'a')
        date = datetime.now()
        fo.write(date.strftime('%d-%m-%Y  %H:%M:%S') + '\n')
        fo.write('Operation type: ' + error + '\n')
        if status == 1:
            fo.write("Status: Success\n\n")
        else:
            fo.write('Status: Fail\n')
            fo.write('Error type: ' + error_type + '\n\n')
        fo.close()