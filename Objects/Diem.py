from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate
from Objects.layten import *

class Diem(Base_CLS):
    def __init__(self,Mahocsinh = '',Mamonhoc = '',Mahocky = '',Manamhoc = '',Malop = '',Maloai = '',Diem = '') -> None:
        self.Mahocsinh = Mahocsinh
        self.Mamonhoc = Mamonhoc
        self.Mahocky = Mahocky
        self.Manamhoc = Manamhoc
        self.Malop = Malop
        self.Maloai = Maloai
        self.Diem = Diem
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
        self.ten=LayTen()
        
              
        
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Xem diem hoc sinh ')
            print('1. Them thong tin diem thi')
            print('2. Sua thong tin diem thi')
            print('3. Xoa thong tin diem thi')
            print('4. Tim diem hoc sinh theo ma hoc sinh ')
            print('5. Tim diem theo lop hoc')
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
    
    def __input__if(self):
        self.Mamonhoc = input("Ma Mon Hoc: ")
        self.Mahocky = input("Ma Hoc Ky: ")
        self.Manamhoc = input("Ma Nam Hoc: ")
        self.Malop = input("Ma Lop: ")
        self.Maloai = input("Ma Loai: ")
        self.Diem = input("Diem: ")
    
    def __display_data(self,):
        layten = self.ten
        sql_cmd= "SELECT * FROM Diem "
        self.__db_cur.execute(sql_cmd)
        
        result = self.__db_cur.fetchall()
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.Monhoc(row[2]),layten.Hocky(row[3]),layten.Namhoc(row[4]),layten.Lop(row[5]),layten.Loaidiem(row[6]),row[7]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["STT","Ma Hoc Sinh","Mon Hoc","Hoc Ky","Nam Hoc","Lop","Loai Diem","Diem"],numalign="center"))
    
    def __add_data(self):
        print("************Nhap thong tin************")
        self.Mahocsinh = input("Ma Hoc Sinh: ")
        
        self.__input__if()
        try:
            sql_cmd = """
            INSERT INTO DIEM (MaHocSinh, MaMonHoc, MaHocKy, MaNamHoc, MaLop, MaLoai, Diem)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
            vals = (self.Mahocsinh,self.Mamonhoc,self.Mahocky,self.Manamhoc,self.Malop,self.Maloai,self.Diem)
            self.__db_cur.execute(sql_cmd,vals)
            self.__db_conn.commit()
            logger.info('Them moi diem thi thanh cong') 
        except:
            logger.info('Them moi diem thi khong thanh cong, vui long xem lai thong tin hoc sinh') 
    
    def __update_data(self):
        print("************Nhap thong tin************")
        STT = input("So thu tu: ")
        self.Diem=input("Diem: ")
        sql_cmd="UPDATE Diem SET Diem=%s WHERE STT=%s"
        self.__db_cur.execute(sql_cmd,(self.Diem,STT))
        self.__db_conn.commit()
        logger.info("cat nhat thong tin thanh cong")
    
    def __delete_data(self):
        print("************Nhap thong tin************")
        STT = input("So thu tu: ")
        sql_cmd= "DELETE FROM Diem WHERE STT=%s"
        self.__db_cur.execute(sql_cmd,[STT])
        if(self.__db_conn.commit()):
            logger.info("xoa thong tin khong thanh cong")
        else:
            logger.info("xoa thong tin thanh cong")

    def __search_id(self):
        layten = self.ten
        MaHocSinh = input("Ma Hoc Sinh: ")
        sql_cmd= "SELECT * FROM Diem WHERE MaHocSinh=%s"
        self.__db_cur.execute(sql_cmd,[MaHocSinh])
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin hoc sinh")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.Monhoc(row[2]),layten.Hocky(row[3]),layten.Namhoc(row[4]),layten.Lop(row[5]),layten.Loaidiem(row[6]),row[7]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["STT","Ma Hoc Sinh","Mon Hoc","Hoc Ky","Nam Hoc","Lop","Loai Diem","Diem"],numalign="left"))

    def __search_name(self):
        layten = self.ten
        MaLop = '%'+input("Ma Lop: ")+'%'
        sql_cmd= "SELECT * FROM Diem WHERE MaLop LIKE %s"
        self.__db_cur.execute(sql_cmd,[MaLop])
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin hoc sinh")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.Monhoc(row[2]),layten.Hocky(row[3]),layten.Namhoc(row[4]),layten.Lop(row[5]),layten.Loaidiem(row[6]),row[7]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["STT","Ma Hoc Sinh","Mon Hoc","Hoc Ky","Nam Hoc","Lop","Loai Diem","Diem"],numalign="left"))
        