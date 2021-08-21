import random
import string
from fastapi import FastAPI
from psycopg2 import connect


app=FastAPI()
# создание подключения к БД по параметрам
connect=connect(dbname='api_servece', user='postgres', password='666')
# инициализация набора функций для нашего подключения 
cursor=connect.cursor()

@app.get('/registration/{user_name}/{first_name}/{last_name}/{email}/{user_password}/{is_admin}/{is_activate}/')
def signal(user_name: str,first_name:str,last_name:str,email:str,user_password:str,is_admin:bool,is_activate:bool):
    str_random='qweasdzxc'
    SQL=f"""insert into token_user(user_token)
    values ('{str_random}');"""
    cursor.execute(SQL)
    connect.commit()
    SQL=f"""SELECT token_id FROM token_user;"""
    cursor.execute(SQL)
    a=cursor.fetchall()
    count=a[-1][0]
   

    #  SQL=f"""insert into profiles(user_name,first_name,last_name,email,user_password,is_admin,is_activate)
    # values ('{user_name}','{first_name}','{last_name}','{email}','{user_password}','{is_admin}','{is_activate}');"""
    # cursor.execute(SQL)
    # connect.commit()
    # print(SQL)

    # return {
    #     'user_name':user_name,
    #     'first_name':first_name,
    #     'last_name':last_name,
    #     'email':email,
    #     'user_password':user_password,
    #     'is_admin':is_admin,
    #     'is_activate':is_activate
    #     }

