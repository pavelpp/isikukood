__author__ = 'pavel'

from random import randint

def generate():
    """generates a valid estonian personal code"""
    s_cent = randint(3, 6)
    serial_nr = randint(0, 999)
    control_nr = randint(0, 9)

    code = str(s_cent) + gen_date() + zeroes(serial_nr, 3) + str(control_nr)

    return code

def gen_date():
    """generates a valid date"""
    byear = randint(0, 99)
    bmonth = randint(1, 12)

    if bmonth == 2 and byear % 4 == 0:
        bday = randint(1, 29)
    elif bmonth == 2:
        bday = randint(1, 28)
    elif bmonth in [4, 6, 9, 11]:
        bday = randint(1, 30)
    else:
        bday = randint(1, 31)
    return zeroes(byear, 2) + zeroes(bmonth, 2) + zeroes(bday, 2)

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
