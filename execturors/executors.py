#!/usr/bin/env python3

import time
from concurrent.futures import ThreadPoolExecutor

def task_a():
    for i in range(4):
        time.sleep(1)
        print("A" + str(i))
    return 4

def task_b():
    for i in range(6):
        time.sleep(1)
        print("B" + str(i))
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(task_a)
b = executor.submit(task_b)

executor.shutdown(wait=True)

print("A: " + str(a.result(timeout=None)))
print("B: " + str(b.result(timeout=None)))
print("DONE")
