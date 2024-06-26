# 导入模块
import sqlite3
# 创建连接
con=sqlite3.connect('./demo.db')
# 创建游标对象
cur=con.cursor()
# 创建查询sql
sql='select * from t_person'
try:
    cur.execute(sql)
    # 获取结果集
    person_all=cur.fetchall()    # fetchone()获取一条数据
    #print(person_all)      # 返回值是列表
    for person in person_all:
        print(person)
except Exception as e:
    print(e)
    print('查询所有数据失败')
finally:
    # 关闭
    cur.close()
    con.close()