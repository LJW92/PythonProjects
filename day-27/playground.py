def add(*args):
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    print(type(args))
    return sum_of_args


print(add(3, 5, 6))

def calculate(**kwargs):
    print(kwargs)


calculate(add=3, cheng = 5)
