def f1():  # old use (java 2)
    print('hi {}. you are {} years old'.format('new maor', '55'))


def f2():  # old use (java 2)
    name = 'maor'
    age = 30.605
    print('hi {}. you are {} years old'.format(name, age))


def f3():  # old use (java 2)
    name = 'maor'
    age = 30.605
    print('hi {1}. you are {0} years old'.format(name, age))


def f4():
    name = "maor"
    age = 30.605
    print('hi %.2r. you are %.1r years old' % (name, age))


def f5():
    name = 'maor'
    age = 30.605
    print('hi {}. you are {} years old'.format(name, age))
    print('hi %s. you are %.1f years old' % (name, age))
    print(f'hi {name}. you are {age} years old')


# f1()
# f2()
# f3()
f4()
# f5()
