from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)      # seek()函数是在Python中用于改变文件读写指针位置的函数

def print_a_line(line_count, f):
    print(line_count, f.readline())      # 打印行数，和这行的内容

current_file = open(input_file)

print('First let\'s print the whole file:\n')

print_all(current_file)    # 打印文件全部内容

print("Now let's rewind, kind of like a tape")

rewind(current_file)   # 将文件的读写指针移动到文件的开始位置

print('Let\'s print three lines:')

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print_a_line(3,current_file)   # 行数可以直接写
