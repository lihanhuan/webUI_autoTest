import unittest

# 测试用例目录
test_dir = './'
# 加载测试用例
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    #执行用例
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)