class Solution:
    def intToRoman(self, num: int) -> str:

        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

        roman_str = ""

        for value in sorted(roman_map.keys(), reverse=True):  # Sort keys in descending order
            count = num // value  # How many times can we use this numeral?
            roman_str += roman_map[value] * count  # Append the corresponding numeral `count` times
            num %= value  # Reduce num by removing counted values
        
        return roman_str
        