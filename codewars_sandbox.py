# task1
"""For example, if we run 9119 through the function,
811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer"""

square = lambda num: int(''.join([str(int(digit) ** 2) for digit in str(num)]))

# task2
"""Is square number?"""


def is_square(n):
    if n < 0:
        return False
    n = float(n ** 0.5)
    if n % 1 == 0:
        return True
    else:
        return False


# task3
"""Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1."""


def binary_array_to_number(arr):
    result = 0
    for elem in arr:
        result = result * 2 + elem
    return result


# task4
"""You probably know the "like" system from Facebook and other pages. People can "like" 
blog posts, pictures or other items. We want to create the text that should be displayed
next to such an item. Implement a function likes :: [String] -> String, which must take
in input array, containing the names of people who like an item. It must return the display
text """


def likes(names) -> str:
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return '{0} likes this'.format(names[0])
    elif len(names) == 2:
        return '{0} and {1} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{0}, {1} and {2} like this'.format(names[0], names[1], names[2])
    else:
        return '{0}, {1} and {2} others like this'.format(names[0], names[1], int(len(names) - 2))


# task 5
"""You need to create a fibonacci function that given a signature array/list, returns the first n elements - signature
 included of the so seeded sequence."""


def tribonacci(signature, n):
    result = [signature[0], signature[1]]

    def tribonachchi_gen(sign, n):
        pre_prev, prev, current = sign
        k = n - 2
        while k > 0:
            k -= 1
            yield current
            pre_prev, prev, current = prev, current, pre_prev + prev + current

    tribonachchi_gen(signature, n)
    result.extend(list(tribonachchi_gen(signature, n)))
    return result


# task 6
"""Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character 
of the final pair with an underscore ('_').
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']"""


def solution(work_string):
    lst = list(work_string)
    if len(lst) % 2 != 0:
        lst.append('_')
    for elem in range(len(lst)):
        if elem < len(lst):
            lst[elem] += lst.pop(elem + 1)
    return lst


# task 7
"""A Narcissistic Number is a number which is the sum of its own digits, each raised to the power 
of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10)."""


def narcissistic(num):
    result = 0
    for digit in str(num):
        result += int(digit) ** len(str(num))
    return result == num


# task 8
"""Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
If there are multiple elements with the same value, remove the one with a lower index. 
If you get an empty array/list, return an empty array/list.
remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]"""


def remove_smallest(numbers):
    nums_array = numbers.copy()
    for index, value in enumerate(nums_array):
        if value == min(nums_array):
            nums_array.pop(index)
            break
    return nums_array


# task 9
"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
without any elements with the same value next to each other and preserving the original order of elements.
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]"""


def unique_in_order(string_of_elements):
    current = ''
    result = []
    for i in string_of_elements:
        if i != current:
            result.append(i)
        current = i
    return result


# task 10
"""Bob is preparing to pass IQ test. The most frequent task in this test is to find out which 
one of the given numbers differs from the others. Bob observed that one number usually differs 
from the others in evenness. Help Bob — to check his answers, he needs a program that among 
the given numbers finds one that is different in evenness, and return a position of this number.
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even"""


def iq_test(digits):
    counter_even = 0
    counter_odd = 0
    for digit in digits.split():
        if int(digit) % 2 == 0:
            counter_even += 1
        else:
            counter_odd += 1
    if counter_even > counter_odd:
        for index, digit in enumerate(digits.split()):
            if int(digit) % 2 != 0:
                return index + 1
    else:
        for index, digit in enumerate(digits.split()):
            if int(digit) % 2 == 0:
                return index + 1


# task 11
"""Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) 
for strings. All words must have their first letter capitalized without spaces.
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord"""

camel_case = lambda name: ''.join([x.title() for x in name.split()])

# task 12
"""Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]"""


def move_zeros(arr):
    help_list = []
    help_list_2 = []
    for elem in arr:
        if (elem == 0 or elem == 0.0) and (type(elem) == int or type(elem) == float):
            help_list.append(elem)
        else:
            help_list_2.append(elem)
    help_list_2.extend(help_list)
    return help_list_2


def move_zeros_best(array):
    return [a for a in array if isinstance(a, bool) or a != 0] + [a for a in array if
                                                                  not isinstance(a, bool) and a == 0]


# task 13
"""Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and 
returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts 
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, 
can be considered as 0.
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}) -> 2"""


def cakes(need_dict, current_dict):
    amounts = []
    for key, val in need_dict.items():
        for k, v in current_dict.items():
            if key == k:
                amounts.append(current_dict[k] / need_dict[key])
    if len(amounts) == len(need_dict):
        return round(min(amounts))
    else:
        return 0


# task 14
"""Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890" """


def create_phone_number(arr):
    return '({0}) {1}-{2}'.format(''.join([str(elem) for elem in arr])[:3],
                                  ''.join([str(elem) for elem in arr])[3:6],
                                  ''.join([str(elem) for elem in arr])[6:])


# task 15
"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution_15(line: str, arr: list) -> str:
    mas = []
    for line_elem in line.split('\n'):
        for index, char in enumerate(line_elem):
            if char in arr:
                line_elem = line_elem[:index].rstrip()
        mas.append(line_elem)
    return str('\n'.join(mas))


# task 16
"""In this kata you have to create all permutations of an input string and remove 
duplicates, if present. This means, you have to shuffle all letters from the input 
in all possible orders.
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']"""
import itertools


def permutations(line: str):
    return [''.join(elem) for elem in set(itertools.permutations(line))]


# task 17
"""Write a function, which takes a non-negative integer (seconds) as input and 
returns the time in a human-readable format (HH:MM:SS)
The maximum time never exceeds 359999 (99:59:59)"""


def convert_time(seconds: int):
    hours = (seconds // 3600)
    minutes = seconds // 60 - (hours * 60)
    seconds = seconds - (minutes * 60 + hours * 3600)
    return '{0:=02}:{1:=02}:{2:=02}'.format(hours, minutes, seconds)


# task 18
"""Explosive Sum"""


def sum_exp(n: int):
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            table[j] += table[j - i]
    return table[n] + 1


# task 19
"""You are going to be given an array of integers. Your job is to take that array and find an index N where the 
sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index 
that would make this happen, return -1."""


def sum_equal(arr: list):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    return -1


# task 20
"""Matrix determinant"""


# import numpy as np


def mat_det(matrix: list):
    return int(round(np.linalg.det(matrix)))


# task 21
"""Interval sum"""


def interval_sum(list_of_intervals):
    final_list = []
    for interval in list_of_intervals:
        for elem in range(interval[0], interval[1]):
            final_list.append(elem)
    return len(set(final_list))


# task 22
def binary_search(arr: list, item: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

# task 23
