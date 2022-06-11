class Foo:
    def foo1(self, num):
        self.num = num

    def foo2(self, num):
        self.num = num * 2


obj = Foo()

method_to_activate = obj.foo1
method_to_activate(5)
print(obj.num)

method_to_activate = obj.foo2
method_to_activate(5)
print(obj.num)
