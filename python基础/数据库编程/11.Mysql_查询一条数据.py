# 导入模块
import pymysql
# 创建连接
con=pymysql.connect(host='localhost',user='root',password='llll',database='python_db',port=3306)
# 创建游标对象
cur=con.cursor()
# 编写查询的sql语句
sql='select * from t_student where age=24'
try:
    # 执行sql
    cur.execute(sql)
    # 处理结果集
    student=cur.fetchone()
    # print(students)    # 此处返回值为元组
    sno=student[0]
    sname=student[1]
    age=student[2]
    score=student[3]
    print('sno:',sno,'sname:',sname,'age:',age,'score:',score)
except Exception as e:
    print(e)
    print('查询所有数据失败')
finally:
    # 关闭连接
    con.close()