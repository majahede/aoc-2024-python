
def is_sorted(numbers):
    return numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)


def differences_within_range(numbers, min_diff = 1, max_diff = 3):
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        
        if diff < min_diff or diff > max_diff:
            return False
        
    return True

def is_safe_with_bad_level(numbers):
    if is_sorted(numbers) and differences_within_range(numbers):
            return True
    
    for i in range(len(numbers)):
        current_number = numbers[i]
        del numbers[i]

        if is_sorted(numbers) and differences_within_range(numbers):
            return True
    
        numbers.insert(i, current_number)

    return False

def get_safe_reports(include_exceptions = False):
    file_path = "files/input02.txt"
    safe_reports = 0

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            
            try:
                numbers = line.strip().split()
                numbers = [int(num) for num in numbers]

                if include_exceptions:
                    if is_safe_with_bad_level(numbers):
                        safe_reports += 1
                else:
                    if is_sorted(numbers) and differences_within_range(numbers):
                        safe_reports += 1
                    
            except ValueError:
                print(f"Could not convert line {line_number} to integers ({line})")

    return safe_reports


safe_reports = get_safe_reports()
safe_reports_including_exceptions = get_safe_reports(True)
print(f"Safe reports: {safe_reports}")
print(f"Safe reports including exceptions: {safe_reports_including_exceptions}")
