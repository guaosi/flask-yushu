import threading
import time
from werkzeug.local import Local
obj_a=Local()
obj_a.b=1
def worker():
    # print("in before thread b is :" + str(obj_a.b))
    obj_a.b=2
    print("in new thread b is :"+str(obj_a.b))
newt=threading.Thread(target=worker,name='guaosi-thread')
newt.start()
time.sleep(1)
print("in mainThread b is :"+str(obj_a.b))