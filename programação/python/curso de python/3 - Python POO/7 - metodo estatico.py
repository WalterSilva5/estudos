class MetodosEstaticos:
    def func1():
        print('func1')
    def func2(x, y):
        print("func2 , params {}, {}".format(x, y))

    func1 = staticmethod(func1)
    func2 = staticmethod(func2)
