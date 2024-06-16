import re

text = " the quick brown fox and therese a blackend hourse and balacked kitecn"
pattern = r"black"

search = re.search(pattern,text)
if search:
    print("pattern found", search.group())
else:
    print("not found")