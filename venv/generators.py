class MyRange:
  current = 0
  def __init__(self,first,last):
    self.first = first
    self.last = last        
  def __iter__(self):
    return self

  def __next__(self):
    if MyRange.current < self.last:
      num = MyRange.current
      MyRange.current += 1
      return num
    raise StopIteration

class MyFib:
  counter = 0
  current = 0
  previous = 0
  def __init__(self,index):
    self.index = index
            
  def __iter__(self):
    return self

  def __next__(self):
    if MyFib.counter < self.index:
      MyFib.counter += 1
      if MyFib.current == 0:
        MyFib.current = 1
      num = MyFib.current + MyFib.previous
      MyFib.previous = MyFib.current
      MyFib.current = num
      return num
    raise StopIteration

class BetterFib:
  def fib(self,number):
    a = 0
    b = 1

    for i in range(number):
      yield a
      temp = a
      a = b
      b = temp + b    

class Generators:
  def gen(self,num):
    for i in range(num):
      yield i

  def doGenerateNumbers(self,num):
    gen1 = self.gen(num)
    for i in range(num):
      print(next(gen1))

  def doSpecialForLoop(self, iterable):
    print("Special for loop using iterable")
    iterator = iter(iterable)
    while True:
      try:
        print(next(iterator))
      except StopIteration:
        break

  def doCreateRange(self,first,last):
    print("Special range using dunder methods")
    myRange = MyRange(first,last)
    for i in myRange:
      print(i)

  def doGenerateFib(self,index):
    print("Special range to create Fibinacci numbers")
    myFib = MyFib(index)
    for i in myFib:
      print(i)

  def doEfficientFib(self,number):
    bFib = BetterFib()    
    for i in bFib.fib(number):
      print(i)
     




