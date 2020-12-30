from time import time
class Decorators:
  
  def decorator(func):
    def wrapper(self,*args,**kwargs):
      print("**************")
      func(self,*args,**kwargs)
      print("**************")
    return wrapper

  def performance_decorator(func):
    def wrapper(self,*args,**kwargs):
      print("**************")
      t1 = time()
      result = func(self,*args,**kwargs)
      t2 = time()
      print(f'It took {t2-t1} seconds')      
      print("**************")
      return result
    return wrapper

  def authentication_wrapper(func):
    
    user = {'name':'Neel', 'valid':False}
    def wrapper(self,*args,**kwargs):
      print("**************")
      if(user['name'] == args[0] and user['valid'] == True):
        func(self,*args,**kwargs)
      else:
        print(f"Message has not been sent to {args[0]}")
      print("**************")
    return wrapper

  @decorator
  def hello(self):
    print("Hello")

  @performance_decorator
  def checkPerformance(self):
    for i in range(10000):
      i*5

  @authentication_wrapper
  def sendMessage(*args,**kwargs):
    print(f"Message has been sent to {args[0]}")