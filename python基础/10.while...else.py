# 循环可以和else配合使用，else下方缩进的代码是当循环正常结束之后要进行的代码
"""
【while...else 语法】
while 条件:
    条件成立循环的代码
else:
    循环正常结束之后要执行的代码
"""
i = 0
while i < 5:
    print('我爱你')
    i += 1
else:
    print('你不爱我，我要毁灭世界')

# while--else循环终止
# [1] break
i = 0
while i < 5:
    if i == 2:
        break
    print('我爱你')         #此处应执行while循环，而非if
    i += 1
else:
    print('你不爱我，我要毁灭世界')

# [2] continue
i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print('我爱你')
    i += 1
else:
    print('你不爱我，我要毁灭世界')

# 总结 break结束else不执行 continue结束else执行