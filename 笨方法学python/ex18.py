# this one is like your script with argv
def print_two(*args):     
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this just takes no argument
def print_none():            # 不放参数也可以
    print("I got nothin")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# def 就是定义(define)的意思
# *args(asterisk args)，和脚本argv非常相似，参数必须在圆括号()中才能正常工作