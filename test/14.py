from contextlib import contextmanager
@contextmanager
def book_make_preix():
    print('《',end='')
    yield
    print('》',end='')
with book_make_preix():
    print('且将生活饮而尽',end='')