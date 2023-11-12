from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate

class HanhKiem(Base_CLS):
    def __init__(self,MaHanhKiem = '', TenHanhKiem = '') -> None:
        self.MaHanhKiem = MaHanhKiem
        self.TenHanhKiem = TenHanhKiem
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
    
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Xem thong tin hanh kiem')
            print('1. Sua thong tin hanh kiem')
            print('2. Quay lai menu truoc do')
            user_input = input('a:')
            if user_input == '0':
                self.__display_data()
            elif user_input == '1':
                self.__update_data()
            elif user_input == '2':
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')
    
    def __display_data(self):
        sql_cmd = "SELECT * FROM HANHKIEM"
        self.__db_cur.execute(sql_cmd)
        results = self.__db_cur.fetchall()
        
        list_st=[]
        for idx,row in enumerate(results):
            st_if=[row[0],row[1]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaHanhKiem","TenHanhKiem"],numalign="left"))
    
    def __update_data(self):
        print("************Nhap thong tin************")
        self.MaHanhKiem = input("Ma Hanh Kiem: ")
        self.TenHanhKiem = input("Ten Hanh Kiem: ")
         
        sql_cmd="UPDATE HanhKiem SET TenHanhKiem = %s WHERE MaHanhKiem = %s"
        self.__db_cur.execute(sql_cmd,(self.TenHanhKiem,self.MaHanhKiem))
        self.__db_conn.commit()
        logger.info("cat nhat thong tin thanh cong")
    