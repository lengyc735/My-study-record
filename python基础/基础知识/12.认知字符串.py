# 字符串--str
a = 'hellow world'    
print(a)
print(type(a))

b = "我要无敌了"
print(type(b))

# 三引号也可以表示字符串 双引三引可以直接换行
c = '''wo就是天意'''
print(c,type(c))

d = """我命由我，不由天"""
print(d,type(d))

e = """wo命由我
不由天"""
print(e,type(e))

# I'm lyc 不可以使用'I'm lyc'   应在中间的引号前加上转义符\
f = 'I\'m lyc'         # 等效于  f = "I'm lyc"
print(f,type(f))