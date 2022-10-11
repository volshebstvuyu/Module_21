from datetime import datetime
from decorators import do_twice
import functools
def sum (a,b):
    print(a + b)
# sum(5,5)

def parent():
    print("Printing fron parent() function")
    def first_child():
        print("Printig from first_child() function")
        def second_child():
            print("Printing from second_child() function")
        second_child()
    first_child()
# parent()

def my_decorator(func):
    def wrapper():
        print("начало выполнения функции")
        func()
        print("конец выполнения функции")
    # return wrapper()

# def my_first_decorator():
#     print("это мой первый декоратор")
# my_first_decorator = my_decorator(my_first_decorator)
# my_first_decorator()

@my_decorator
def my_first_decorator():
    print("это мой первый декоратор")

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"
test_twice("single")
# print(test_twice.__name__)

#
decorated_value = test_twice("single")
print(decorated_value)


@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")


@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))


test_twice_without_params()
test_twice_2_params("1", "2")
test_twice("single")

def workig_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 23:
            func()
        else:
            pass
    return wrapper
def writing_tests():
    print("я пишу тесты на python")
writing_tests = workig_hours(writing_tests)
# writing_tests()

