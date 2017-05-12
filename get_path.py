#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 2017

@author: Heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""

import sys
import PrimePath
import codecs as cs
# import PrimePath.readGraphFromFile as readGraphFromFile
# import PrimePath.findPrimePaths as findPrimePaths


class prime:

    def __init__(self, graph):
        self.graph = PrimePath.readGraphFromFile(graph)
        # self.answer = self.readAnswer(answer)

    def findPrimePath(self):
        savedStdout = sys.stdout  # save the stdout
        output = cs.open('cache', 'w', 'utf8')
        sys.stdout = output

        PrimePath.findPrimePaths(self.graph)
        sys.stdout = savedStdout


if __name__ == "__main__":
    case = prime("../Prime-Path/graphs/testcase1")
    case.findPrimePath()
