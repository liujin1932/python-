import unittest
from api.api_login import Login
from common.mylogger import Log




class test1(unittest.TestCase):
    log = Log()

    def setUp(self):
        login = Login()
    def test_api_login(self):
        r = self.login.add_cookies()
        self.log.info("调用登录接口结果%s"%r)
        self.log.info('获取cookie接口运行完毕----------')
    def tearDown(self):
        print("测试结束-----------")

if __name__ == '__main__':
    unittest.main()
