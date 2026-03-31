from abc import ABC, abstractmethod

class Absclass(ABC):
    def display(self, x):
        print("The value is", x)

    @abstractmethod
    def task(self):
        print("I am in Absclass")

class testclass(Absclass):
    def task(self):
        print("We are inside the testclass class")

testobj = testclass()
testobj.task()
testobj.display(100)

