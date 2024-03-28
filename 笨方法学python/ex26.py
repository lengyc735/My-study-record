def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):   # 少了个冒号：
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)      # 3.0里面print是函数，要加括号

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)   # 少了个)
    print (word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print ("--------------")
print (poem)
print ("--------------")

five = 10 - 2 + 3 - 5
print ("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000   # 除法是/，\是转义符
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # ==是判断相等，=是赋值

print ("With a starting point of: %d" % start_point)
print ("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

import ex25
words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)

# 1.检查每一行的拼写
# 2.检查每一个字符的拼写
# 3.检查每一个(),[],{}的括号是否成对
# 4.检查空格是否正确
# 5.检查函数的定义和调用是否正确
# 6.检查变量的定义和使用是否正确

# 检查代码是一个漫长的过程，不要着急，不要求快，应该耐心的慢慢看