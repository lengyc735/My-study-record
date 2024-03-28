tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."    # \n is a new line
backslash_cat = "I'm \\ a \\ cat."       # 特殊符号要用\转义

fat_cat = """                          
I'll do a list:
\t* Cat food
\t* Fishies
\t* catnip\n\t* Grass
"""
 # 三个双引号可以换行
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

