from functools import singledispatchmethod
class Teacher():
    # 参数类型的不同进行不同的初始化。
    @singledispatchmethod
    def __init__(self,arg):
        if arg is None :
            self.age = 0
            self.name = ''
        else:
            raise TypeError("Unsupported argument type")
    @__init__.register
    def _(self, age: int):
        self.age = age
        self.name = ''
    
    @__init__.register
    def _(self, name: str, age: int = 0):
        self.age = age
        self.name = name
    def sayHello(self):
        return f'hello, my name is {self.name},my age is {self.age}'

class Person:
    # 定义一个构造方法
    def __init__ (self, name):
          # 定义了一个name变量
          self.name =name
    # 定义一个方法
    def say_hello(self):
          return f'hello, my name is {self.name}'
    # 定义一个静态方法
    def second_hello(arg:str):
          return f'你好:{arg}'

# 定义Student类继承Person类
class Student(Person):
      # 定义一个构造方法,self表示实例本身
      def __init__(self, name,age):
            self.age=age
            # 调用父类的构造方法
            super().__init__(name)
            
     # 将方法转化为静态方法，然后创建实例，cls表示类本身而不是实例
      @classmethod
      def Create_student(cls,name,age,country):
            # 创建country变量，此代码执行后其他通过构造函数创建的实例也会有country属性,且有值
            # 相当于定义静态变量
            cls.country=country
            return cls(name,age)
      def say_hello(self):
            return f'你好, 我是{self.name},来自{self.country}，今年{self.age}'

          