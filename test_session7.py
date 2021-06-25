import os
import inspect
import re
import random
import session7 as s7
import pytest

README_CONTENT_CHECK_FOR = [
    'generate_my_next_number',
    'min_count',
    'docstring',
    'fibonacci',
    'called',
    'closure',
    'global',
    'count',
    'dictioanry',
    'variable'
]


def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(s7, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_readme_contents():
    readme_words = [word for line in open(
        'README.md', 'r') for word in line.split()]
    assert len(
        readme_words) >= 550, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 15, 'You are not writing proper heading'


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_docstring_check():
    # more than 50
    f1 = s7.docstring_check(s7.myfibonacci)
    assert f1() == True, 'just do a character by character count..it is easy'

    # zero
    f1 = s7.docstring_check(test_readme_exists)
    assert f1() == False, 'just do a character by character count..it is easy'

    # less than 50
    f1 = s7.docstring_check(test_function_name_had_cap_letter)
    assert f1() == False, 'just do a character by character count..it is easy'


def test_myfibonacci():
    mylist = [1, 2, 3, 5, 8, 13]
    f1 = s7.myfibonacci()
    for i in mylist:
        assert i == f1(), 'You are not able to generate a fabonacci series, time to visit childhood again'


def test_mycounter():
    f1 = s7.mycounter(s7.add)
    for i in range(1, 11):
        assert f1(random.randint(1, 100), random.randint(1, 100)
                  ) == i, " arre counting karni h bro....!! Simple"


def test_div():
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(1, 100)
        assert(s7.div(number1, number2) == number1 /
               number2), 'you learned division in 1st?? or you skipped it..'
        number2 = random.randint(-100, -1)
        assert(s7.div(number1, number2) == number1 /
               number2), 'you learned division in 1st?? or you skipped it..'


def test_div_for_error():
    number1 = random.randint(-100, 100)
    number2 = 0
    with pytest.raises(ValueError, match=r".* divide .*"):
        s7.div(number1, number2), "you are not GOD!!, puny Human"


def test_add():
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        assert(s7.add(number1, number2) == number1 +
               number2), 'you learned addition in 1st?? or you skipped it..'


def test_mul():
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        assert(s7.mul(number1, number2) == number1 *
               number2), 'you learned multiplication in 1st?? or you skipped it..'


def test_sub():
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        assert(s7.sub(number1, number2) == number1 -
               number2), 'you learned substraction in 1st?? or you skipped it..'


def test_mycounter_with_global_dict():
    mydict_val = {'add': 4, 'mul': 3, 'div': 2, 'sub': 1}
    fn = s7.add
    value = s7.mycounter_with_global_dict(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s7.mul
    value = s7.mycounter_with_global_dict(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s7.div
    value = s7.mycounter_with_global_dict(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s7.sub
    value = s7.mycounter_with_global_dict(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    assert s7.mydict == mydict_val, 'just count how many times each funtion is called..'


def test_mycounter_with_global_dict_v2():
    mydict_val = {'add': 4, 'mul': 3, 'div': 2, 'sub': 1}
    mypersonaldict = {'add': 0, 'mul': 0, 'div': 0, 'sub': 0}
    fn = s7.add
    value = s7.mycounter_with_global_dict_2(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s7.mul
    value = s7.mycounter_with_global_dict_2(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s7.div
    value = s7.mycounter_with_global_dict_2(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s7.sub
    value = s7.mycounter_with_global_dict_2(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    assert mypersonaldict == mydict_val, 'just count how many times each funtion is called..'


def test_check_annot():

    assert bool(s7.add.__annotations__) == True, "Annotations missing"
    assert bool(s7.sub.__annotations__) == True, "Annotations missing"
    assert bool(s7.mul.__annotations__) == True, "Annotations missing"
    assert bool(s7.div.__annotations__) == True, "Annotations missing"
    assert bool(
        s7.mycounter_with_global_dict_2.__annotations__) == True, "Annotations missing"


def test_check_docs():

    assert bool(s7.docstring_check.__doc__) == True, "Docstring missing"
    assert bool(s7.myfibonacci.__doc__) == True, "Docstring missing"
    assert bool(s7.add.__doc__) == True, "Docstring missing"
    assert bool(s7.sub.__doc__) == True, "Docstring missing"
    assert bool(s7.mul.__doc__) == True, "Docstring missing"
    assert bool(s7.div.__doc__) == True, "Docstring missing"
    assert bool(s7.mycounter.__doc__) == True, "Docstring missing"
    assert bool(
        s7.mycounter_with_global_dict.__doc__) == True, "Docstring missing"
    assert bool(
        s7.mycounter_with_global_dict_2.__doc__) == True, "Docstring missing"


def test_check_closure():
    f1 = s7.docstring_check(s7.myfibonacci)
    assert bool(
        f1.__closure__) == True, "Bhai Closure hi toh banana tha.. kyu bana diya"
    f1 = s7.myfibonacci()
    assert bool(
        f1.__closure__) == True, "Bhai Closure hi toh banana tha.. kyu bana diya"
    f1 = s7.mycounter(s7.add)
    assert bool(
        f1.__closure__) == True, "Bhai Closure hi toh banana tha.. kyu bana diya"
    fn = s7.add
    f1 = s7.mycounter_with_global_dict(fn)
    assert bool(
        f1.__closure__) == True, "Bhai Closure hi toh banana tha.. kyu bana diya"
    mypersonaldict = {'add': 0, 'mul': 0, 'div': 0, 'sub': 0}
    fn = s7.add
    f1 = s7.mycounter_with_global_dict_2(fn, mypersonaldict)
    assert bool(
        f1.__closure__) == True, "Bhai Closure hi toh banana tha.. kyu bana diya"
