from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate

class HocLuc(Base_CLS):
    def __init__(self,MaHocLuc = '', TenHocLuc = '',DiemCanDuoi='',DiemCanTren='',DiemKhongChe='') -> None:
        self.MaHocLuc = MaHocLuc
        self.TenHocLuc = TenHocLuc
        self.DiemCanDuoi = DiemCanDuoi
        self.DiemCanTren = DiemCanTren
        self.DiemKhongChe = DiemKhongChe
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
    
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Xem thong tin hoc Luc')
            print('1. Sua thong tin hoc Luc')
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
        sql_cmd = "SELECT * FROM HocLuc"
        self.__db_cur.execute(sql_cmd)
        results = self.__db_cur.fetchall()
        
        list_st=[]
        for idx,row in enumerate(results):
            st_if=[row[0],row[1],row[2],row[3],row[4]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaHocLuc","TenHocLuc","DiemCanTren","DiemCanDuoi","DiemKhongChe"],numalign="left"))
    
    def __update_data(self):
        print("************Nhap thong tin************")
        self.MaHocLuc = input("Ma Hoc Luc: ")
        self.TenHocLuc = input("Ten Hoc Luc: ")
        self.DiemCanDuoi = input("Diem Can Duoi: ")
        self.DiemCanTren = input("Diem Can Tren: ")
        self.DiemKhongChe = input("Diem Khong Che: ")

        sql_cmd="UPDATE HocLuc SET TenHocLuc=%s,DiemCanDuoi=%s,DiemCanTren=%s,DiemKhongChe=%s WHERE MaHocLuc = %s"
        self.__db_cur.execute(sql_cmd,(self.TenHocLuc,self.DiemCanDuoi,self.DiemCanTren,self.DiemKhongChe,self.MaHocLuc))
        self.__db_conn.commit()
        logger.info("cat nhat thong tin thanh cong")
    