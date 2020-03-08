import time
from config import base_url,Cookie

def sleep(n_secs):
    time.sleep(n_secs)

def get_base_url():
    # print(base_url)
    return base_url
def get_Cookie():
    print(Cookie)
    return Cookie

def hook_up():
    print("前置操作：setup!")

def hook_down():
    print("后置操作：teardown!")

def hook_log(var=''):
    print("用例执行log：%s" % var)




if __name__ == '__main__':
    get_base_url()
    get_Cookie()
