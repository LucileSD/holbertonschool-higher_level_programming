#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        one = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        two = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        result = 0
        i = 0
        roman_concate = ""
        while i < len(roman_string):
            if i + 1 < len(roman_string):
                roman_concate = roman_string[i] + roman_string[i + 1]
            if roman_string in two:
                result += two[roman_concate]
                i += 1
            elif roman_string[i] in one:
                result += one[roman_string[i]]
            i += 1
        return result
    else:
        return 0
