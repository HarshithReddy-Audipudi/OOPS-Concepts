class Car:
    wheels=5
    def __init__(self,com,mil):
        self.com=com
        self.mil=mil
    
    def f1(self):
        print("its:",self.com,self.mil,self.wheels)

obj1=Car("BMW",10)
obj2=Car("AUDI",20)
obj1.f1()
obj2.f1()
