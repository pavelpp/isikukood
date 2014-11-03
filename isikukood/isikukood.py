__author__ = 'pavel'

from random import randint

def generate():
    """generates a valid estonian personal code"""
    s_cent = randint(3, 6)
    serial_nr = randint(0, 999)
    code = str(s_cent) + gen_date() + zeroes(serial_nr, 3)
    final_code = code + control_nr(code)

    return final_code

def gen_date():
    """generates a valid date"""
    byear = randint(0, 99)
    bmonth = randint(1, 12)


    if bmonth == 2 and is_leap(byear):
        bday = randint(1, 29)
    elif bmonth == 2:
        bday = randint(1, 28)
    elif bmonth in [4, 6, 9, 11]:
        bday = randint(1, 30)
    else:
        bday = randint(1, 31)
    return zeroes(byear, 2) + zeroes(bmonth, 2) + zeroes(bday, 2)


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else: return False

def control_nr(code):
    sum1 = 1*int(code[0]) + 2*int(code[1]) + 3*int(code[2]) + 4*int(code[3]) + 5*int(code[4]) + \
           6*int(code[5]) + 7*int(code[6]) + 8*int(code[7]) + 9*int(code[8]) + 1*int(code[9])
    sum2 = 3*int(code[0]) + 4*int(code[1]) + 5*int(code[2]) + 6*int(code[3]) + 7*int(code[4]) + \
            8*int(code[5]) + 9*int(code[6]) + 1*int(code[7]) + 2*int(code[8]) + 3*int(code[9])
    if sum1 % 11 != 10:
        return str(sum1 % 11)
    elif sum2 % 11 != 10:
        return str(sum2 % 11)
    else: return "0"

def zeroes(number, length):
    """adds leading zeroes, where necessary"""
    if length == 2:
        return "%02d" %  number
    elif length == 3:
        return "%03d" % number

def run_times(times):
    for n in range(times):
        print(generate())

run_times(10)
