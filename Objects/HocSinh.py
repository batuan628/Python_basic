from Database_mysql.Data import *
from Objects.Base_class import *
from tabulate import tabulate
from Objects.layten import *

class HocSinh(Base_CLS):
    def __init__(self,MaHocSinh='',HoTen='',GioiTinh='',NgaySinh='',DiaChi='',MaDanToc='',MaTonGiao='',HoTenCha='',MaNgheCha='',HoTenMe='',MaNgheMe='',Email='') -> None:
        self.MaHocSinh = MaHocSinh
        self.HoTen = HoTen
        self.GioiTinh = GioiTinh
        self.NgaySinh = NgaySinh
        self.DiaChi = DiaChi
        self.MaDanToc = MaDanToc
        self.MaTonGiao = MaTonGiao
        self.HoTenCha = HoTenCha
        self.MaNgheCha = MaNgheCha
        self.HoTenMe = HoTenMe
        self.MaNgheMe = MaNgheMe
        self.Email = Email
        db_obj = SQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
        self.ten=LayTen()
    
    
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Xem 10 diem hoc sinh gan nhat')
            print('1. Them thong tin hoc sinh')
            print('2. Sua thong tin hoc sinh')
            print('3. Xoa thong tin hoc sinh')
            print('4. Tim hoc sinh theo ma hoc sinh ')
            print('5. Tim hoc sinh theo ten hoc sinh')
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
        self.HoTen = input("Ho Ten: ")
        self.GioiTinh = int(input("Gioi Tinh(0:Nam,1:Nữ): "))
        self.NgaySinh = input("Ngay Sinh: ")
        self.DiaChi = input("Dia Chi: ")
        self.MaDanToc = input("Ma Dan Toc: ")
        self.MaTonGiao = input("Ma Ton Giao: ")
        self.HoTenCha = input("Ho Ten Cha: ")
        self.MaNgheCha = input("Ma Nghe Cha: ")
        self.HoTenMe = input("Ho Ten Me: ")
        self.MaNgheMe = input("Ma Nghe Me: ")
        self.Email = input("Email: ")
    def __display_data(self):
        layten = self.ten
        sql_cmd= "SELECT * FROM HocSinh"
        self.__db_cur.execute(sql_cmd)
        
        result = self.__db_cur.fetchall()
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.GioiTinh(row[2]),row[3],row[4],layten.DanToc(row[5]),layten.TonGiao(row[6]),row[7],layten.MaNghe(row[8]),row[9],layten.MaNghe(row[10]),row[11]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaHocSinh","HoTen","GioiTinh","NgaySinh","DiaChi","MaDanToc","MaTonGiao","HoTenCha","MaNgheCha","HoTenMe","MaNgheMe","Email"],numalign="left"))
    
     
    def __add_data(self):
        print("************Nhap thong tin************")
        self.MaHocSinh = input("Ma Hoc Sinh: ")
        
        self.__input__if()
        try:
            sql_cmd = """
            INSERT INTO HocSinh (MaHocSinh,HoTen,GioiTinh,NgaySinh,DiaChi,MaDanToc,MaTonGiao,HoTenCha,MaNgheCha,HoTenMe,MaNgheMe,Email)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            vals = (self.MaHocSinh,self.HoTen,self.GioiTinh,self.NgaySinh,self.DiaChi,self.MaDanToc,self.MaTonGiao,self.HoTenCha,self.MaNgheCha,self.HoTenMe,self.MaNgheMe,self.Email)
            self.__db_cur.execute(sql_cmd,vals)
            self.__db_conn.commit()
            logger.info('Them moi hoc sinh thanh cong') 
        except:
            logger.info('Them moi hoc sinh khong thanh cong, vui long xem lai thong tin hoc sinh') 
    
     
    def __update_data(self):
        print("************Nhap thong tin************")
        self.MaHocSinh = input("Ma Hoc Sinh: ")
        self.__input__if()
        sql_cmd="UPDATE HocSinh SET HoTen=%s,GioiTinh=%s,NgaySinh=%s,DiaChi=%s,MaDanToc=%s,MaTonGiao=%s,HoTenCha=%s,MaNgheCha=%s,HoTenMe=%s,MaNgheMe=%s,Email=%s WHERE MaHocSinh=%s"
        self.__db_cur.execute(sql_cmd,(self.HoTen,self.GioiTinh,self.NgaySinh,self.DiaChi,self.MaDanToc,self.MaTonGiao,self.HoTenCha,self.MaNgheCha,self.HoTenMe,self.MaNgheMe,self.Email,self.MaHocSinh))
        self.__db_conn.commit()
        logger.info("cat nhat thong tin thanh cong")
    
     
    def __delete_data(self):
        print("************Nhap thong tin************")
        self.MaHocSinh = input("Ma Hoc Sinh: ")
        sql_cmd= "DELETE FROM HocSinh WHERE MaHocSinh=%s"
        self.__db_cur.execute(sql_cmd,[self.MaHocSinh])
        if(self.__db_conn.commit()):
            logger.info("xoa thong tin khong thanh cong")
        else:
            logger.info("xoa thong tin thanh cong")
    
     
    def __search_id(self):
        layten = self.ten
        self.MaHocSinh = input("Ma Hoc Sinh: ")
        sql_cmd= "SELECT * FROM HocSinh Where MaHocSinh=%s"
        self.__db_cur.execute(sql_cmd,[self.MaHocSinh])
        
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin hoc vien")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.GioiTinh(row[2]),row[3],row[4],layten.DanToc(row[5]),layten.TonGiao(row[6]),row[7],layten.MaNghe(row[8]),row[9],layten.MaNghe(row[10]),row[11]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaHocSinh","HoTen","GioiTinh","NgaySinh","DiaChi","MaDanToc","MaTonGiao","HoTenCha","MaNgheCha","HoTenMe","MaNgheMe","Email"],numalign="left"))
    
     
    def __search_name(self):
        layten = self.ten
        self.TenHocSinh = '%'+input("Ten Hoc Sinh: ")+'%'
        sql_cmd= "SELECT * FROM HocSinh Where HoTen LIKE %s"
        self.__db_cur.execute(sql_cmd,[self.TenHocSinh])
        
        result = self.__db_cur.fetchall()
        if len(result) == 0 :
            logger.error("khong co thong tin hoc vien")
            return
        list_st=[]
        for idx,row in enumerate(result):
            st_if=[row[0],row[1],layten.GioiTinh(row[2]),row[3],row[4],layten.DanToc(row[5]),layten.TonGiao(row[6]),row[7],layten.MaNghe(row[8]),row[9],layten.MaNghe(row[10]),row[11]]
            list_st.append(st_if)
        print(tabulate(list_st, headers=["MaHocSinh","HoTen","GioiTinh","NgaySinh","DiaChi","MaDanToc","MaTonGiao","HoTenCha","MaNgheCha","HoTenMe","MaNgheMe","Email"],numalign="left"))
    