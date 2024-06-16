import re

text = "days are very beutiful"

pattern = r"days"

search = re.search(pattern,text)

if search:
    print(search.group())
else:
    print("not found")

    