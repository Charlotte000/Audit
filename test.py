import os
import time
import datetime

print('Start simle Python program')

time.sleep(3)

pid = os.getpid()
print(f'Current pid: {pid}')

os.execvp('echo', ['echo', 'Bye'])

# while True:
#     print('1', end='', flush=True)
#     time.sleep(1)
#     a = os.getpid()