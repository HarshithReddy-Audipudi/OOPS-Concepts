class Details:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def f1(self):
        print("my name is:",self.name,"age is:",self.age)
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


obj1=Details("harshith",25)
obj2=Details("Rohith",28)
obj1.f1()
if obj1.compare(obj2):
    print("They are same")
else:
    print("They are Different")
