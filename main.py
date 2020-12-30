from classAndStaticMethods import Person
from decorators import Decorators
from errorHandling import ErrorHandling

def aboutClassAndStaticMethods():
  person1 = Person('Neel', 16) 
  person2 = Person.fromBirthYear('Neel', 2004) 
    
  print(str(person1)) 
  print(str(person2)) 
    
  # print the result 
  print (Person.isAdult(22))

def aboutDecorators():
  deco = Decorators()
  deco.hello()
  deco.checkPerformance()
  deco.sendMessage("Neel")

def aboutErrorHandling():
  eh = ErrorHandling()
  #eh.doErrorHandling()
  eh.doRaiseError()

#aboutClassAndStaticMethods()
#aboutDecorators()
aboutErrorHandling()