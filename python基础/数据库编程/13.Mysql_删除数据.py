# 导入模块
import pymysql
# 创建连接
con=pymysql.connect(host='127.0.0.1',user='root',password='llll',database='python_db',port=3306)
# print(con)   # 检查连接
# 创建游标对象
cur=con.cursor()
# 编写删除的sql语句
sql='delete from t_student where sname=%s '
try:
    # 执行sql
    cur.execute(sql,('阿龙'))
    con.commit()
    print('删除成功')
except Exception as e:
    print(e)
    con.rollback()
    print('删除失败')
finally:
    con.close()