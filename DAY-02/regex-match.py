import re
text = "The quick brown fox"
pattern = r"quick"
match = re.match(pattern, text)
if match:
    print("match found", match.group())   
else:
    print("no match")