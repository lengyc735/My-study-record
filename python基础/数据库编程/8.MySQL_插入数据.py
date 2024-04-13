# 导入模块
import pymysql
# 创建连接
con=pymysql.connect(host='localhost',user='root',password='llll',database='python_db',port=3306)
# print(con)  # 检查连接是否成功
# 创建游标对象
cur=con.cursor()
# 编写插入数据的sql
sql='insert into t_student(sname,age,score) value(%s,%s,%s)'
try:
    # 执行sql
    cur.execute(sql, ('小王八',38,99))
    # 提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    # 关闭连接
    con.close()