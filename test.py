#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 2017

@author: Heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""

import unittest
import codecs as cs
from get_path import prime


base_dir = r'./cases/'


def readAnswer(answer):
    with cs.open(answer, 'r', 'utf8') as src:
        return [line.strip() for line in src.readlines()]


class TestPrime(unittest.TestCase):

    def setUp(self):
        print "Prime path test start."

    def test_primt(self):
        for i in range(16):
            test_file = base_dir + 'testcase' + str(i)
            case = prime(test_file)
            case.findPrimePath()
            ans = readAnswer(base_dir + 'answer/anwser' + str(i))
            pred = readAnswer("cache")
            self.assertEqual(
                ans[0], pred[0],
                msg='The answer\'s length not equal to testcase\'s.')
            for j in range(int(ans[0])):
                self.assertEqual(
                    ans[j + 1],
                    pred[j + 1],
                    msg='testcase%d\'s %d path not correct!' % (i, j + 1))
            print "testcase%d all path correct!" % i

    def tearDown(self):
        print "Prime path test end."


if __name__ == "__main__":
    unittest.main()
