import re

file_path = 'files/input03.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', file_content)

total = 0
for match in matches:
    numbers = re.findall(r'\d+', match)
    total += int(numbers[0]) * int(numbers[1])


print(total)