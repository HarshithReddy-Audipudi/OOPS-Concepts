class A:
    def f1(self):
        print("feature-1")
    def f2(self):
        print("feature-2")
    def f3(self):
        print("feature-3")

class B:
    def f4(self):
        print("feature-4")
    def f5(self):
        print("feature-5")


class C(A,B):
    def f6(self):
        print("feature-6")

obj1=C()
obj1.f1()

    