'''
学员管理系统
1.添加学员
2.删除学员
3.修改学员信息
4.查询所有学员信息
5.显示所有学员信息
6.退出系统
'''

def info_print():
    print('-'*20)
    print('\n请选项功能：')
    print('1·添加学员')
    print('2·删除学员')
    print('3·修改学员')
    print('4·查询学员')
    print('5·显示所有学员')
    print('6·退出系统')
    print('-'*20)

info = []

# 添加学员的函数
def add_info():
    '''添加学员函数'''
    print('\n请输入您要添加学员的信息')
    new_name = input('请输入名字： ')
    new_id = input('请输入学号：')
    new_tel = input('请输入电话: ')

    global info

    for i in info:
        if new_name == i['name']:
            print('该用户已存在')
            return   # 此处return的作用是退出函数

    info_dict = {}

    info_dict['name'] = new_name
    info_dict['id'] = new_id
    info_dict['tel'] = new_tel

    info.append(info_dict)
    print(f'\n您添加的学员信息为{info}')

def del_info():
    """删除学员"""
    
    del_name = input('\n请输入您要删除的学员： ')

    global info

    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('\n该学员不存在')
    
    print(info)

def modify_info():
    """修改函数"""

    modify_name = input('请输入您想要修改的学员的名字： ')

    global info

    for i in info:
        if modify_name == i['name']:
            i['id'] = input('请输入您想修改的id： ')
            i['tel'] = input('请输入您想修改的手机号： ')
            break
    else:
        print('这位学员不存在')

    print(info)

def  search_info():
    """查找学员"""

    search_name = input('\n请输入您要查找的学员名字： ')

    global info

    for i in info:
        if search_name == i['name']:
            print('\n您想要查找的学员信息如下：')
            print(f'该学员的名字为{i['name']},学号为{i['id']},电话为{i['tel']}') 
            break
        else:
            print('该学员不存在')

    print(info)

def print_info():
    """显示所有学员"""
    print('\n名字\t学号\t电话')
    for i in info:
        print(f'{i["name"]}\t{i["id"]}\t{i['tel']}')

while True:

    info_print()

    user_num = int(input('\n请输入对应功能的序号： '))

    if user_num == 1:
        print('添加')
        add_info()
    elif user_num == 2:
        print('删除')
        del_info()
    elif user_num == 3:
        print('修改')
        modify_info()
    elif user_num == 4:
        print('查询')
        search_info()
    elif user_num == 5:
        print('显示所有')
        print_info()
    elif user_num == 6:
        exit_flag = input('确定要退出吗？请输入 yes or no: ')
        if exit_flag == 'yes':
            print('\n成功退出')
            break
    else:
        print('输入错误')