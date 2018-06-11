import threading
import time
from werkzeug.local import LocalStack
s=LocalStack()
s.push(1)
print('mainThread before pop :'+str(s.top))
def worker():
    print('other Thread before pop :'+str(s.top))
    s.push(2)
    print('other Thread after pop :' + str(s.top))
newt=threading.Thread(target=worker,name='guaosi-thread')
newt.start()
time.sleep(1)
print('mainThread after pop :'+str(s.top))
