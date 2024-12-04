import re

def extract_between_and_before(content, between_pattern, before_pattern):
    between_matches = re.findall(between_pattern, content, flags=re.DOTALL)
    between_content = ''.join(between_matches)

    before_match = re.search(before_pattern, content, flags=re.DOTALL)
    before_content = before_match.group(1) if before_match else ""

    return between_content, before_content

def extract_and_calculate(pattern, content):
    matches = re.findall(pattern, content)
    return calculate_total(matches)

def calculate_total(matches):
    total = 0

    for match in matches:
        numbers = re.findall(r'\d+', match)
        total += int(numbers[0]) * int(numbers[1])

    return total

mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
between_pattern = r"(?<=do\(\)).*?(?=don't\(\))"
before_pattern = r"^(.*?)(?=do\(\)|don't\(\))"

file_path = 'files/input03.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

part_one_result = extract_and_calculate(mul_pattern, file_content)

between_string, before_string = extract_between_and_before(file_content, between_pattern, before_pattern)
combined_content = between_string + before_string
part_two_result = extract_and_calculate(mul_pattern, combined_content)

print(f"Part One Result: {part_one_result}")
print(f"Part Two Result: {part_two_result}")