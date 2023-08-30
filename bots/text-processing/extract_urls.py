import re
with open('urls.txt', 'r') as file:
    urls = file.read()


# print(urls)
pattern = re.compile(r'https?://(www\.)?(\w+)\.com')
matches = pattern.finditer(urls)

for match in matches:
  print(match.group(0))