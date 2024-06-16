import re
text = "days and month are calulatin the time "

pattern = r"days"

replacement = "year"

changed_word  = re.sub(pattern , replacement,text)

print(changed_word)