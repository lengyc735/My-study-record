'''
包：
  包将有联系的模块组织在一起，即放到同一个文件夹下，
  并且在这个文件夹创建一个名字为__init__.py文件，
  那么这个文件夹就称之为包
'''

'''
导入包中的模块(方法1)
  import 包名.模块名
  
调用：
  包名.模块名.函数名()
'''

'''
方法二：
    注意：必须在__init__.py文件中添加__all__ = [].控制允许导入的模块

    from 包名 import *
    
    调用：
        模块名.函数名()
'''