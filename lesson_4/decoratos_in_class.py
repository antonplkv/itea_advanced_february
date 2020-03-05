class A:

    @staticmethod
    def dec(func):
        def wrapper(*args):
            func(*args)

        return wrapper

    @dec
    def do_smth(self, arg1, arg2):
        pass




a = A()
a.do_smth(1, 2)