class Student:
    school="LAP"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self,value):
        self.m1=value
        return self.m1
    
    @classmethod
    def info(cls):
        return cls.school
    
    @staticmethod
    def info_st():
        print("this is student avg calculator")
    
s1=Student(11,23,43)
s2=Student(31,21,54)

print(s1.avg())
print(s1.get_m1())
print(s1.set_m1(20))
print(Student.info())
Student.info_st()
