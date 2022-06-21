class calculator:
    num = 100 #class variables
    def __init__(self,a,b): #constructor
        self.first_number= a
        self.second_number= b
        print("I am called automatically when object is created")

    def getData(self):
        print("executing method")

    def summation(self):  #method = def
        return self.first_number + self.second_number + calculator.num


obj=calculator(2,3) #syntax to create objects in python (= 2+3)
obj.getData()
print(obj.summation())

obj1=calculator(4,5) #syntax to create objects in python (= 4+5)
obj1.getData()
print(obj1.summation())
