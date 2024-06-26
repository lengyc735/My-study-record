# 导入模块
import sqlite3
# 创建连接
con = sqlite3.connect('demo.db')
# 创建游标对象
cur = con.cursor()
# 编写插入sql
sql = 'insert into t_person(pname,age) values(?,?)'
try:
    # 执行插入多条数据的sql
    cur.executemany(sql,[('荒天帝',78879),('装三',34),('达旺',57)])
    # 提交事务
    con.commit()
    print('插入多条数据成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入多条数据失败')
finally:
    # 关闭游标连接
    cur.close()
    # 关闭数据库连接
    con.close()