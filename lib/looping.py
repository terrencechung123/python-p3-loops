#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    if i == 0:
        print('Happy New Year!')
    # ipdb.set_trace()


def square_integers(int_list):
    square_integers = [i**2 for i in int_list]
    return square_integers


def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i += 1
