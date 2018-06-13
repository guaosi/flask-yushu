class A():
    def __call__(self, *args, **kwargs):
        print(1)
def B():
    print(2)
def main(callable):
    callable();
main(A())
main(B)