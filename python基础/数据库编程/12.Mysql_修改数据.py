# 导入模块
import pymysql
# 创建连接
con=pymysql.connect(host='127.0.0.1',user='root',password='llll',database='python_db',port=3306)
# print(con)   # 检查连接
# 创建游标对象
cur=con.cursor()
# 编写修改的sql语句
sql='update t_student set sname=%s where sno=%s'
try:
    # 执行sql
    cur.execute(sql,('阿龙',1))
    con.commit()
    print('修改成功')
except Exception as e:
    print(e)
    con.rollback()
    print('修改失败')
finally:
    con.close()