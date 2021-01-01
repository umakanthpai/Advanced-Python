from classAndStaticMethods import Person
from decorators import Decorators
from errorHandling import ErrorHandling
from generators import Generators
from files import Files

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

def aboutGenerators():
  gen = Generators()
  #gen.doGenerateNumbers(15)
  #gen.doSpecialForLoop([2,4,7])
  #gen.doCreateRange(0,7)
  #gen.doGenerateFib(10)
  gen.doEfficientFib(20)

def aboutFiles():
  aFile = Files()
  #aFile.doReadFile()
  aFile.doWithOpenFileHandling()
  #aFile.doTryExceptInFileHandling()
  #aFile.doWriteFile()

#aboutClassAndStaticMethods()
#aboutDecorators()
#aboutErrorHandling()
#aboutGenerators()
aboutFiles()
