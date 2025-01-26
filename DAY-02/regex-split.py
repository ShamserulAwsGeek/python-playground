import re
text = "apple, banana, cherry,orange,grapes"
pattern = r","
spilt_result = re.split(pattern, text)
print("original text:", text)
print("split result:", spilt_result)