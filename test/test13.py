from contextlib import contextmanager
class MyResource:
    def query(self):
        print('this is query')
@contextmanager
def make_myresource():
    print('connect to MyResource')
    yield MyResource()
    print('close to MyResource')
with make_myresource() as r:
    r.query()
    print('yes')