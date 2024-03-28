def add(a, b):
    print('ADDING %d + %d' % (a, b))
    return a + b

def subtract(a ,b):
    print("SUNTRACTING %d - %d" % (a,b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just function!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")

# 例子:斐波那契数列
def fol(n):
    a, b, i = 1, 1, 1
    ls = [1, 1]
    while i <= n - 2:
        a, b = b, a+b
        ls.append(b)
        i += 1
    return ls

test = fol(9)
print(test)