import unittest
import HTMLTestRunner
import time
import testcases.test_api_login
import testcases.test_api_user_info
from common.sendmail import SendMail

def add_by_class_testsuite():
    '''
    使用makeSuite（）以一个class作为单元添加class里面的所有case进入Suite
    :return:
    '''
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testcases.test_api_login.test1))
    suite.addTest(unittest.makeSuite(testcases.test_api_user_info.test2))
    return suite

if __name__ == '__main__':

    test_suite = add_by_class_testsuite()
    now = time.strftime("%y%m%d_%H%M%S")
    html_file = "./report/" + now + "result.html"
    print(html_file)
    fp = open(html_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="ceshi0229")
    runner.run(test_suite)
    ss = SendMail()
    ss.sendmail()
