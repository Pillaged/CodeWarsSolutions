def zero(func=0): return 0 if not func else func(0)
def one(func=1): return 1 if not func else func(1)
def two(func=2): return 2 if not func else func(2)
def three(func=3): return 3 if not func else func(3)
def four(func=4): return 4 if not func else func(4)
def five(func=5): return 5 if not func else func(5)
def six(func=6): return 6 if not func else func(6)
def seven(func=7): return 7 if not func else func(7)
def eight(func=8): return 8 if not func else func(8)
def nine(func=9): return 9 if not func else func(9)


def plus(num1): return lambda num2: num1+num2
def minus(num1): return lambda num2: num1-num2
def times(num1): return lambda num2: num1*num2
def divided_by(num1): return lambda num2: num1//num2

