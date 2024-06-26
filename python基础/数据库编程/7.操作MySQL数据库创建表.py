# 导入pymysql
import pymysql
# 创建连接
con=pymysql.connect(host='localhost',user='root',password='llll',database='python_db',port=3306)
# print(con)  # 验证连接是否成功
# 创建游标对象
cur=con.cursor()
# 编写创建表的sql
sql='''
    create table t_student(
    sno int primary key auto_increment,
    sname varchar(30) not null,
    age int(2),
    score float(3,1)
    )
'''

try:
    # 执行创建表的sql
    cur.execute(sql)
    print('创建表成功')
except Exception as e:
    print(e)
    print('创建表失败')
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()