# coding: utf-8

from multiprocessing import Process

import test_functions


pList = []
for idx in xrange(0, 8):
    p = Process(target=test_functions.test_add_while, args=(idx, ))
    pList.append(p)

for p in pList:
    p.start()

for p in pList:
    p.join()
