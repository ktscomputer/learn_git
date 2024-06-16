import re

text = "finding words between the txt such as blacked cat and balacked kiten"

pattern = r"words"

match = re.match(pattern, text)
if match:
    print("Match found",match.group())
else:
    print("no such words") 


    

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")