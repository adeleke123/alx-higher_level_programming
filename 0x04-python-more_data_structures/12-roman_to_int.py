#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

    if type(roman_string) != str or roman_string is None:
        return 0

    nums = [roman_dict[i] for i in roman_string]
    result = 0

    for i in range(len(nums)):
        result += nums[i]
        if nums[i - 1] < nums[i] and i != 0:
            result -= (nums[i - 1] + nums[i - 1])
    return result
