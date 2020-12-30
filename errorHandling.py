import traceback
class ErrorHandling:

  #Syntax Error
  #Name Error 
  #Key Error 
  #Zero division error 
  #Value error 
  #Type Error
  def doErrorHandling(self):
    while(True):
      try:
        age = int(input("Enter your age: "))
      except (ValueError, TypeError) as err:
        print("********************************************************")
        print("Using error object, this does not show line number where error occurs.")
        print(f"{err} \nOnly numbers are allowed, please enter a number")
        print("********************************************************")

        print("\n********************************************************")
        print("Using taceback module to show file, line number also:")
        print("********************************************************")
        print(f" {traceback.print_exc()} Only numbers are allowed, please enter a number")
      except ZeroDivisionError as err:
        print(f"Enter number greater than 0 {err}")
      else:
        print(f"Thank you!!! You entered {age}")
        break;
      finally:
        print("Resources are released...")

  def doRaiseError(self):
    while(True):
      try:
        age = int(input("Enter your age: "))
        if(age <= 0 or age >= 120):
          raise ValueError("Age should be greater than 0 and less than 120")          
      except ZeroDivisionError:        
        print(f"Only numbers are allowed, please enter a number")      
      else:
        print(f"Thank you!!! You entered {age}")
        break;
      
  
