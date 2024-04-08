# 自定义异常类，继承Exception
class ShortIputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len
    
    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length},不能少于{self.min_len}个字符,请重新输入'


def main():
    while True:
        try:
            con = input('\n请输入密码： ')
            if len(con) < 3:
                raise ShortIputError(len(con),3)
        except Exception as result:
            print(result)
        else:
            print('密码输入完成')
            break


main()