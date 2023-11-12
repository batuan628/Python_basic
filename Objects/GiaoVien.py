from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate
from Objects.layten import *

class GiaoVien(Base_CLS):
    def __init__(self,MaGiaoVien = '',  TenGiaoVien ='', DiaChi = '', DienThoai='', MaMonHoc='') -> None:
        self.MaGiaoVien = MaGiaoVien
        self.TenGiaoVien = TenGiaoVien
        self.DiaChi = DiaChi
        self.DienThoai = DienThoai
        self.MaMonHoc = MaMonHoc
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
        self.ten=LayTen()
    
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Xem 10 giao vien gan nhat')
            print('1. Them thong tin giao vien')
            print('2. Sua thong tin giao vien')
            print('3. Xoa thong tin giao vien')
            print('4. Tim kiem giao vien theo ma giao vien ')
            print('5. Tim giao vien theo ten giao vien')
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
            elif user_input =='5':
                self.__search_name()
            elif user_input == '6':
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')
                
    def input_if(self):
        self.TenGiaoVien = input("Ten Giao Vien: ")
        self.DiaChi = input("Dia Chi: ")
        self.DienThoai = input("Dien Thoai: ")
        self.MaMonHoc = input("Ma Mon Hoc: ")
    
    def __display_data(self):
        layten = self.ten
        sql_cmd= "SELECT * FROM GiaoVien limit 10"
        self.__db_cur.execute(sql_cmd)
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin giao vien")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],row[2],row[3],layten.Monhoc(row[4])]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaGiaoVien","TenGiaoVien","DiaChi","DienThoai","MonHoc"],numalign="left"))
    
    def __add_data(self):
        print("************Nhap thong tin************")
        self.MaGiaoVien = input("Ma Giao Vien: ")
        
        self.input_if()
        try:
            sql_cmd = """
            INSERT INTO GiaoVien (MaGiaoVien, TenGiaoVien, DiaChi, DienThoai, MaMonHoc)
            VALUES (%s,%s,%s,%s,%s)
            """
            vals = (self.MaGiaoVien,self.TenGiaoVien,self.DiaChi,self.DienThoai,self.MaMonHoc)
            self.__db_cur.execute(sql_cmd,vals)
            self.__db_conn.commit()
            logger.info('Them moi giao vien thanh cong')
        except:
            logger.info('Them moi giao vien khong thanh cong, vui long xem lai thong tin giao vien') 
    
    def __update_data(self):
        print("************Nhap thong tin************")
        self.MaGiaoVien = input("Ma Giao Vien: ")
         
        self.input_if()
        sql_cmd="UPDATE GiaoVien SET TenGiaoVien=%s, DiaChi=%s, DienThoai=%s, MaMonHoc=%s WHERE MaGiaoVien=%s"
        self.__db_cur.execute(sql_cmd,(self.TenGiaoVien,self.DiaChi,self.DienThoai,self.MaMonHoc,self.MaGiaoVien))
        self.__db_conn.commit()
        logger.info("cat nhat thong tin thanh cong")
    
    def __delete_data(self):
        print("************Nhap thong tin************")
        self.MaGiaoVien = input("Ma Giao Vien: ")
        sql_cmd= "DELETE FROM GiaoVien WHERE MaGiaoVien=%s"
        self.__db_cur.execute(sql_cmd,[self.MaGiaoVien])
        if(self.__db_conn.commit()):
            logger.info("xoa thong tin khong thanh cong")
        else:
            logger.info("xoa thong tin thanh cong")
    
    def __search_id(self):
        layten = self.ten
        self.MaGiaoVien = input("Ma Giao Vien: ")
        sql_cmd= "SELECT * FROM GiaoVien WHERE MaGiaoVien=%s"
        self.__db_cur.execute(sql_cmd,[self.MaGiaoVien])
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin giao vien")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],row[2],row[3],layten.Monhoc(row[4])]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaGiaoVien","TenGiaoVien","DiaChi","DienThoai","MonHoc"],numalign="left"))
    
    def __search_name(self):
        layten = self.ten
        self.TenGiaoVien = '%'+input("Ten Giao Vien: ")+'%'
        sql_cmd= "SELECT * FROM GiaoVien WHERE TenGiaoVien LIKE %s"

        self.__db_cur.execute(sql_cmd,[self.TenGiaoVien])
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin giao vien")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],row[2],row[3],layten.Monhoc(row[4])]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaGiaoVien","TenGiaoVien","DiaChi","DienThoai","MonHoc"],numalign="left"))