class Files:
  def doReadFile(self):
    file = open("test.txt")    
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())

    file.seek(0)
    # Use readlines to get a list
    print("\n******************************")
    print("Use readlines to get a list")
    print("******************************")
    lineList = file.readlines()
    for aLine in lineList:
      print(aLine)

    file.close()

  def doWithOpenFileHandling(self):
    try:
      with open("test.txt") as testFile:
        print("\n******************************")
        print("Use \"with-open\", no need to close the file")
        print("******************************")
        lineList = testFile.readlines()
        for aLine in lineList:
          print(aLine)
    except FileNotFoundError as err:
      print(f"File does not exist {err}")
      raise err    

  def doTryExceptInFileHandling(self):
    try:
      with open("tes.txt") as testFile:
        print("\n******************************")
        print("Use \"with-open\", no need to close the file")
        print("******************************")
        lineList = testFile.readlines()
        for aLine in lineList:
          print(aLine)
    except FileNotFoundError as err:
      print(f"File does not exist {err}")
      raise err
      

  def doWriteFile(self):
    with open("test.txt",mode="r") as testFile:
      print("\n******************************")
      print("Use mode to write to a file")
      print("******************************")
      lineList = testFile.readlines()
      for aLine in lineList:
        print(aLine)
      with open("test_w.txt",mode="w") as testwFile:
        for aLine in lineList:
          testwFile.write(aLine)
  
  # Use r+ read and write mode, should be carefule to manage the cursor, else
  # it will overwrite. Better use append mode 
    