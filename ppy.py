import time
import threading

def read():
    print("读书")
    time.sleep(5)
    print("读书结束")
def write():
    print("写字")
    time.sleep(5)
    print("写字结束")

t1=threading.Thread(target=read)
t2=threading.Thread(target=write)
t1.start()
t2.start()
t1.join(1)
t2.join(3)
print("主线程结束")