import re

class RegularExpressions:
  def doRegex(self):
    aString = "Search this inside of a text"
    pattern = re.compile(r'\w+')
    aMatch = pattern.match(aString)
    print(str(aMatch.group()))

    

