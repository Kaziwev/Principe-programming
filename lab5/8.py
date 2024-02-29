import re
text = "Python"
print(re.findall('[A-Z][^A-Z]*', text))