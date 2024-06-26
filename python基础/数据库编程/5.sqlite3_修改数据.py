# 导入模块
import sqlite3
# 创建连接
con=sqlite3.connect('./demo.db')
# 创建游标对象
cur=con.cursor()
# 编写修改后的sql语句
sql='update t_person set pname=? where pno=?'
try:
    # 执行sql
    cur.execute(sql,(' kobe',2))
    # 提交事务
    con.commit()
    print('修改成功')
except Exception as e:
    print(e)
    print('修改失败')
    con.rollback()
finally:
    # 关闭连接
    con.close()