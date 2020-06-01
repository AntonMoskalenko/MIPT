import datetime
import threading

def foo():
     print(datetime.datetime.now())
     print(threading.active_count())


for x in range(0,300, 10):
     t = threading.Timer(x + 1, foo)
     t.start()