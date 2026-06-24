from abc import ABC, abstractmethod
# 定义接口类
class MyInterface(ABC):
    @abstractmethod
    def sayHello(self):
        pass
    
class MyClass(MyInterface):
    def sayHello(self):
        return "Hello, World!"
    
    
def use_interface(obj:MyInterface):
   return obj.sayHello()
    
m=MyClass()
print(use_interface(m))