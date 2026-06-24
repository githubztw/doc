from injector import Module, Binder, Injector,inject,singleton
# 数据库基类
class Database:
    def save(self, data):
        pass
# 缓存数据库
class MemoryDatabase(Database):
    def save(self, data):
        print(f"Saving to memory: {data}")
# 服务类
class Service:
    @inject # 构造函数依赖注入
    def __init__(self, db: Database):
        self.db = db

    def do_something(self, data):
        self.db.save(data)
        
    @inject # 属性依赖注入
    def db(self) -> Database:
        pass
        
  
  
# 配置注入类  
class MyModule(Module):
    @staticmethod # 静态方法
    def create_db():
        return MemoryDatabase() 
    def configure(self, binder: Binder):
        # 绑定接口到具体实现类
        # binder.bind(Database, to=MemoryDatabase,scope=singleton)
        # 绑定接口到函数
        binder.bind(Database, to=self.create_db,scope=singleton)
        # singleton：单例模式
        # threadlocal ：每个线程有一个单独的实例
        # request ：每个请求一个实例，需要定制
        # 默认无作用域，每次请求依赖时都创建一个新的实例
        
        
        
injector = Injector([MyModule()])
service = injector.get(Service)
service.do_something("Some data")
service.db.save("next save")