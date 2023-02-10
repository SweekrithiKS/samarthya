class Car:
    def __init__( self,company, model):
        self.company=company
        self.model=model
    def func(self):
        print(f"hello my company is {self.company}  and my model {self.model}")
    def __str__(self):
        return "company:" +self.company + ", model:"+str(self.model)
p1=Car("tesla",136)
p1.func()
print(p1) 

