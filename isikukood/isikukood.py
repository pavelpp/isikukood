import datetime

__author__ = 'pavel'

from random import randint
import subprocess


def get_cent(birth_date):
    year = str(birth_date.year)
    if year[:2] == "18":
        return randint(1,2)
    elif year[:2] == "19":
        return randint(3,4)
    elif year[:2] == "20":
        return randint(5,6)
    else:
        return None

def generate():
    """generates a valid estonian personal code"""
    serial_nr = randint(1, 999)
    birth_date = gen_date_alt()
    s_cent = get_cent(birth_date)
    code = str(s_cent) + birth_date.strftime("%y%m%d") + zeroes(serial_nr, 3)
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

def gen_date_alt():
    person_date = datetime.date(1800,1,1)+datetime.timedelta(days=randint(1,109573))
    return person_date #.strftime("%y%m%d")

def get_bday(month, year):
    if month == 2 and is_leap(year):
        bday = randint(1, 29)
    elif month == 2:
        bday = randint(1, 28)
    elif month in [4, 6, 9, 11]:
        bday = randint(1, 30)
    else:
        bday = randint(1, 31)
    return bday

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else: return False

def control_nr(code):
    code = [int(i) for i in code]
    weight1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weight2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum1 = sum([x*y for x,y in zip(code, weight1)])
    sum2 = sum([x*y for x,y in zip(code, weight2)])
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

def copy_to_clipboard(isik):
    cmd = 'echo \"%s\" | pbcopy' % isik
    subprocess.check_output(cmd, shell=True)
    cmd = 'osascript -e \'display notification "genereeritud isikukood %s" with title "Teade"\'' % isik
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    isik = generate()
    copy_to_clipboard(isik)
    #gen_date_alt(20)