# coding: utf-8

from threading import Thread

import test_functions


tList = []
for idx in xrange(0, 8):
    t = Thread(target=test_functions.test_add_while, args=(idx, ))
    tList.append(t)

for t in tList:
    t.start()

for t in tList:
    t.join()
