def break_words(stuff):
    """This function will break up words for us.这个函数会帮我们把句子分割成单词"""
    words = stuff.split(' ')  # split方法会返回一个列表
    return words

def sort_words(words):
    """sorts the words. 对单词进行排序"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after poping it off. 弹出并打印第一个单词"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after poping it off. 弹出并打印最后一个单词"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words. 接收一个完整的句子并返回排序后的单词"""
    words = break_words(sentence)    #调用break_words函数
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence. 打印句子的第一个和最后一个单词"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# 这段代码相当于一个模块，可以被其他程序导入