class A:
    name2='chandra'
    def __init__(self,age,name,address):
        print(age,name,address, self.name2)
    def show(self):
        print(self.name2)

obj=A(30,"Surya","Patna")
obj.show()