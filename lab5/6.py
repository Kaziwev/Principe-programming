import re

text = input(str(""))
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)