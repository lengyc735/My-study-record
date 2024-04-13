# 导入模块
import sqlite3
# 创建连接
con=sqlite3.connect('./demo.db')
# 创建游标对象
cur=con.cursor()
# 编写删除的sql语句
sql='delete from t_person where pno=?'
try:
    # 执行sql
    cur.execute(sql,(2,))  # 注意:此处传入的值必须是元组
    # 提交事务
    con.commit()
    print('删除成功')
except Exception as e:
    print(e)
    print('删除失败')
    con.rollback()
finally:
    # 关闭连接
    con.close()