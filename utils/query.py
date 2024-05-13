from pymysql import *

conn = connect(host='localhost',user='root', password='qq44882960', database='hourse_data',port=3306)
cursor = conn.cursor()

def query(sql,params,type='no_select'):
    params = tuple(params)
    cursor.execute(sql,params)
    if type != 'no_select':
        data_list = cursor.fetchall()
        conn.commit()
        return data_list
    else:
        conn.commit()