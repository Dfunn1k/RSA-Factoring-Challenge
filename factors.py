#!/usr/bin/python3
"""script that factorize as many numbers as possible into a
   product of two smaller numbers"""


def descom_number(num):
    """Extracts the first prime factor of the number, and displays the
       output formatted with the 2 respective factors.

    Args:
        num (int): the number that will be decomposed.
    Attributes:
        tmp (int): stores the number that will be decomposed so as not
                   to lose the value.
        factor_primo: the number with which we will be dividing
    """
    tmp = num
    factor_primo = 2

    while num > 1:
        if num % factor_primo == 0:
            num /= factor_primo
            print(f"{tmp}={int(num)}*{factor_primo}")
            break
        else:
            factor_primo += 1


file = open('tests/test00')
listlines = file.readlines()

for line in listlines:
    descom_number(int(line))
