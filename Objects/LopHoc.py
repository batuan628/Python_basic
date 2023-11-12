from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate
from Objects.layten import *

class LopHoc(Base_CLS):
    def __init__(self,MaLop = '',TenLop = '',MaKhoiLop = '',MaNamHoc = '',SiSo = '',MaGiaoVien = '') -> None:
        self.MaLop = MaLop
        self.TenLop = TenLop
        self.MaKhoiLop = MaKhoiLop
        self.MaNamHoc = MaNamHoc
        self.SiSo = SiSo
        self.MaGiaoVien = MaGiaoVien
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
        self.ten=LayTen()
        
              
        
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Xem cac lop hoc ')
            print('1. Them thong tin lop hoc')
            print('2. Sua thong tin lop hoc')
            print('3. Xoa thong tin lop hoc')
            print('4. Tim lop hoc theo ma lop ')
            print('4. Tim lop hoc theo ten lop ')
            print('6. Quay lai menu truoc do')
            user_input = input('a:')
            if user_input == '0':
                self.__display_data()
            elif user_input == '1':
                self.__add_data()
            elif user_input == '2':
                self.__update_data()
            elif user_input == '3':
                self.__delete_data()
            elif user_input == '4':
                self.__search_id()
            elif user_input == '5':
                self.__search_name()
            elif user_input == '6':
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')
    
    def __input__if(self):
        self.TenLop = input("Ten Lop: ")
        self.MaKhoiLop = input("Ma Khoi Lop: ")
        self.MaNamHoc = input("Ma Nam Hoc: ")
        self.SiSo = input("Si So: ")
        self.MaGiaoVien = input("Ma Giao Vien: ")
    
    def __display_data(self,):
        layten = self.ten
        sql_cmd= "SELECT * FROM Lop "
        self.__db_cur.execute(sql_cmd)
        
        result = self.__db_cur.fetchall()
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.KhoiLop(row[2]),layten.Namhoc(row[3]),row[4],layten.GiaoVien(row[5])]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaLop","TenLop","KhoiLop","NamHoc","SiSo","GiaoVien"],numalign="center"))
    
    def __add_data(self):
        print("************Nhap thong tin************")
        self.MaLop = input("Ma Lop: ")
        
        self.__input__if()
        try:
            sql_cmd = """
            INSERT INTO Lop (MaLop,TenLop,MaKhoiLop,MaNamHoc,SiSo,MaGiaoVien)
            VALUES (%s,%s,%s,%s,%s,%s)
            """
            vals = (self.MaLop,self.TenLop,self.MaKhoiLop,self.MaNamHoc,self.SiSo,self.MaGiaoVien)
            self.__db_cur.execute(sql_cmd,vals)
            self.__db_conn.commit()
            logger.info('Them moi Lop hoc thanh cong') 
        except:
            logger.info('Them moi Lop hoc khong thanh cong, vui long xem lai thong tin ')
    
    def __update_data(self):
        print("************Nhap thong tin************")
        try:
            self.MaLop = input("Ma Lop: ")
            self.SiSo = input("Si So: ")
            self.MaGiaoVien = input("Ma Giao Vien: ")
            sql_cmd="UPDATE Lop SET SiSo=%s,MaGiaoVien=%s WHERE MaLop=%s"
            self.__db_cur.execute(sql_cmd,(self.SiSo,self.MaGiaoVien,self.MaLop))
            self.__db_conn.commit()
            logger.info("cat nhat thong tin thanh cong")
        except:
            logger.info("cat nhat thong tin khong thanh cong")
    def __delete_data(self):
        print("************Nhap thong tin************")
        self.MaLop = input("Ma Lop: ")
        sql_cmd= "DELETE FROM Lop Where MaLop =%s"
        self.__db_cur.execute(sql_cmd,[self.MaLop])
        if(self.__db_conn.commit()):
            logger.info("xoa thong tin khong thanh cong")
        else:
            logger.info("xoa thong tin thanh cong")

    def __search_id(self):
        layten = self.ten
        self.MaLop = input("Ma Lop: ")
        sql_cmd= "SELECT * FROM Lop WHERE MaLop=%s"
        self.__db_cur.execute(sql_cmd,[self.MaLop])
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin hoc sinh")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.KhoiLop(row[2]),layten.Namhoc(row[3]),row[4],layten.GiaoVien(row[5])]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaLop","TenLop","KhoiLop","NamHoc","SiSo","GiaoVien"],numalign="center"))
    
    def __search_name(self):
        layten = self.ten
        self.TenLop = '%'+input("Ten Lop: ")+'%'
        sql_cmd= "SELECT * FROM Lop WHERE TenLop LIKE %s"
        self.__db_cur.execute(sql_cmd,[self.TenLop])
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin lop hoc")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.KhoiLop(row[2]),layten.Namhoc(row[3]),row[4],layten.GiaoVien(row[5])]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaLop","TenLop","KhoiLop","NamHoc","SiSo","GiaoVien"],numalign="center"))
