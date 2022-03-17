import unittest as test
def zero(func=0): return func(0)
def one(func=1): return func(1)
def two(func=2): return func(2)
def three(func=3): return func(3)
def four(func=4): return func(4)
def five(func=5): return func(5)
def six(func=6): return func(6)
def seven(func=7): return func(7)
def eight(func=8): return func(8)
def nine(func=9): return func(9)


def plus(num1, num2=0):
    def help(num2):
        return num1+num2


def minus(num1, num2=0): return num1-num2
def times(num1, num2=1): return num1*num2


def divided_by(num2):
    def help(num1):
        return num1//num2


# tests
test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
