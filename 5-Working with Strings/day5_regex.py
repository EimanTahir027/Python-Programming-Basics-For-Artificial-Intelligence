import re

text = "Contact me at 123-456-7890"
digits = re.findall(r"\d+", text)
print(digits)

updated_text = re.sub(r"\d", "X", text)
print(updated_text)
