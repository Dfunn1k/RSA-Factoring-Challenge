#!/usr/bin/python3

def descom_number(num):
    """"""
    tmp = num
    factor_primo = 2
    while num > 1:
        if num % factor_primo == 0:
            num /= factor_primo
            print(f"{tmp}={int(num)}*{factor_primo}")
            break
        else:
            factor_primo+=1


file = open('tests/rsa-1')
listlines = file.readlines()
for line in listlines:
    descom_number(int(line))
