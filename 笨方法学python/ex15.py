from sys import argv   #从sys模块导入argv

script, filename = argv    # 解包argv

txt = open(filename)       # open()打开文件

print("Here's your file %r:" % filename)
print(txt.read())      # read()读取文件内容

print("Type the filename again:")
file_again = input("> ")      # 等待用户输入

txt_again = open(file_again)

print(txt_again.read())