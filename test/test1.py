import threading
import time
def worker():
    t=threading.current_thread()
    a=1
    a+=1
    print(a)
    print(t.getName())
newthread=threading.Thread(target=worker,name='guaosi-thread') #创建一个线程，指定执行函数与线程名称
newthread1=threading.Thread(target=worker,name='guaosi-thread') #创建一个线程，指定执行函数与线程名称
newthread2=threading.Thread(target=worker,name='guaosi-thread') #创建一个线程，指定执行函数与线程名称
newthread.start() #开始这个线程
newthread1.start() #开始这个线程
newthread2.start() #开始这个线程
t=threading.current_thread() #获取当前线程
print(t.getName()) #获取线程名称