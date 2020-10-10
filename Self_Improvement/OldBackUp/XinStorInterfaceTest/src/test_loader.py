# -*- coding: utf-8 -*-
import unittest
from test_case import XinstorLogin01
from test_case import CreateVolume01
import HtmlTestRunner
'''
测试套测试并生成结果
'''
suite = unittest.TestSuite()

ts = unittest.TestLoader()
suite.addTests(ts.loadTestsFromModule(XinstorLogin01))
suite.addTests(ts.loadTestsFromModule(CreateVolume01))

with open("test_result/test_report.txt", "a+") as f:
    runner = HtmlTestRunner.HTMLTestRunner(stream=f, report_title="ZHL test", descriptions='Test Report', verbosity=2)
    runner.run(suite)