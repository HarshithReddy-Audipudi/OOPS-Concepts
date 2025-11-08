class Student_d:
    def __init__(self,name,r_no,id):
        self.name=name
        self.r_no=r_no
        self.id=id
    def info(self):
        print(self.name,self.r_no,self.id)
    
    class student_extra:
        def __init__(self,sub,marks):
            self.sub=sub
            self.marks=marks
        
        def info_extra(self):
            print(self.sub,self.marks)
obj1=Student_d("harsha",11,1234)
obj1.info()
new_obj=Student_d.student_extra("maths",100)
new_obj.info_extra()

