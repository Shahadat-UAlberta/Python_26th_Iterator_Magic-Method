# Regular Expression

import re

txt = "We on love Python"

getSpecificSeq = re.findall("on", txt)
print(getSpecificSeq)

searchChar = re.search("love", txt)
print(searchChar.span())
print(searchChar.start())
print(searchChar.end())

splitString = re.split(" ", txt)
print(splitString)

subChar = re.sub("love", "404", txt)
print(subChar)

