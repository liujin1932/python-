import unittest
import api.api_user_info
from api.api_user_info import UserInfo
import re
from common.mylogger import Log



class test2(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.userinfo = UserInfo()

    def test_user_info(self):
        result = self.userinfo.get_userinfo()
        self.log.info("调用用户信息接口结果%s" %result)
        self.log.info('获取用户信息接口运行完毕----------')



    def tearDown(self):
        print("测试结束-----------")

if __name__ == '__main__':
    unittest.main()