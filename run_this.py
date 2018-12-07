import unittest
import os
from test_login import LoginTest
from test_search_accepted_clue import SearchTest
import HTMLTestRunner

# 设置报告文件保存路径
cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path, "report")
if not os.path.exists(report_path): os.mkdir(report_path)


# 构造测试套件
suite = unittest.TestSuite()
test_cases = [LoginTest("test_login"), SearchTest("test_search_accept_clue")]
suite.addTests(test_cases)


if __name__ == "__main__":

    # 打开一个文件，将result写入此file中
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="WEB UI 自动化测试报告",
                                               description="用例执行情况")
    runner.run(suite)