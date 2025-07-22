import re
result = re.search(r'\d+', 'There are 123 apples')
print(result.group())