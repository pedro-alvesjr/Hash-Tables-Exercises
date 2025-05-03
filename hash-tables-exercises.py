def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates

def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return[]

# Testes para find_duplicates
assert find_duplicates([1, 2, 3, 2, 4, 5, 1]) == [1, 2]
assert find_duplicates([1, 2, 3, 4, 5]) == []
assert find_duplicates([1, 1, 1, 1]) == [1]

# Testes para first_non_repeating_char
assert first_non_repeating_char("aabbcdd") == "c"
assert first_non_repeating_char("aabbcc") == None
assert first_non_repeating_char("abc") == "a"
assert first_non_repeating_char("") == None

# Testes para two_sum
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([1, 2, 3], 7) == []
