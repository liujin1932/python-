import configparser
import os

class ReadConfig():
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
            print(configpath)
        else:
            # 获取当前文件所在目录
            root_dir = os.path.dirname(os.path.abspath('config'))
            # print(root_dir)
            configpath = os.path.join(root_dir, "config.ini")
            # print(configpath)
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_db(self, param):
        value = self.cf.get("Mysql-Database", param)
        return value

    def get_url(self, param):
        value = self.cf.get("url", param)
        print(value)
        return value
    def get_mail(self,param):
        value = self.cf.get("Email",param)
        print(value)
        return value

if __name__ == '__main__':
    rc = ReadConfig(r"D:\Users\Raymond\PycharmProjects\bokeyuan0229\config\config.ini")
    rc.get_url("base_url")
    rc.get_mail("smtpserver")



