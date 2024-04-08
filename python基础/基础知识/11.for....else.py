"""
for 临时变量 in 序列：
    重复执行的代码
    ...
else:
    循环正常结束之后要执行的代码
"""

str1 = 'itheima'
for i in str1:
   print(i)
else:
   print('循环正常结束之后执行的else的代码') 

# break结束
tr1 = 'itheima'
for i in str1:
   if i == 'e':
      print('遇到e不打印')
      break
   print(i)
else:
   print('循环正常结束之后执行的else的代码') 

# continue结束
tr1 = 'itheima'
for i in str1:
   if i == 'e':
      print('遇到e不打印')
        # 这里不用加 i += 1 
      continue
   print(i)
else:                           # else与直接打印的区别在于循环能否正常结束
   print('循环正常结束之后执行的else的代码') 

