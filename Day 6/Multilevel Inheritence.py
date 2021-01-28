class Parent1:
    def func1(self):
        print("This is a parent function")
class Parent2:
    def func2(self):
        print("This is a parent function")
class Child(Parent1,Parent2):
        def func3(self):
            print("This is a child function")
ob=Child()
ob.func1()
ob.func3()
