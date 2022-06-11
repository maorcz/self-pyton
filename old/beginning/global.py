a = 10


def f1():
    a = 5

    def f2():
        global a

        def inner():
            # nonlocal a
            print(a)
        inner()
    f2()


f1()
