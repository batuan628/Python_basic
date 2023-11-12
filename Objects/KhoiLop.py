from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate



class KhoiLop(Base_CLS):
    def __init__(self) -> None:
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
    
    def __search_name(self):
        sql_cmd = "SELECT * FROM KhoiLop"
        self.__db_cur.execute(sql_cmd)
        results = self.__db_cur.fetchall()
        
        list_st=[]
        for idx,row in enumerate(results):
            st_if=[row[0],row[1]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaKhoiLop","TenKhoiLop"],numalign="left"))

    def ListKhoiLop(self):
        self.__search_name()