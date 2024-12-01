from collections import Counter

def get_lists_from_file():
    file_path = "files/1DecInput.txt"
    first_list = []
    second_list = []

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            
            try:
                num1, num2 = map(int, line.strip().split())
                first_list.append(num1)
                second_list.append(num2)
            except ValueError:
                print(f"Could not convert line {line_number} to two integers ({line})")

    return first_list,second_list


def count_total_distance(first_list, second_list):
    total_distance = 0

    if len(first_list) != len(second_list):
        print("Error: The lists do not have the same number of values.")
    else:   
        first_list.sort()
        second_list.sort()
    
        for i in range(len(first_list)):
            total_distance += abs(first_list[i] - second_list[i])
        
    return total_distance

def count_similarity_score(first_list, second_list):
    similarity_score = 0
    second_list_counter = Counter(second_list)

    for value in first_list:
        occurances = second_list_counter.get(value, 0)
        similarity_score += value * occurances

    return similarity_score


first_list, second_list = get_lists_from_file()

total_distance = count_total_distance(first_list, second_list)
similarity_score = count_similarity_score(first_list, second_list)

print(f"Total distance: {total_distance}")
print(f"Similarity score: {similarity_score}")