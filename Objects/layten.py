from Database_mysql.Data import *

class LayTen:
        
        def __init__(self) -> None:
                db_obj = SQLConn()
                self.__db_conn = db_obj.create_conn()
                self.__db_cur = self.__db_conn.cursor()
        
        def Monhoc(self,a):
                
                sql_cmd= "SELECT TenMonHoc FROM MonHoc WHERE MaMonHoc=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten
        
        def Hocky(self,a):
                
                sql_cmd= "SELECT TenHocKy FROM HocKy WHERE MaHocKy=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten

        def Namhoc(self,a):
                
                sql_cmd= "SELECT TenNamHoc FROM NamHoc WHERE MaNamHoc=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten

        def Lop(self,a):
                
                sql_cmd= "SELECT TenLop FROM Lop WHERE MaLop=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten

        def Loaidiem(self,a):
                
                sql_cmd= "SELECT TenLoai FROM LoaiDiem WHERE MaLoai=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten
        def GioiTinh(self,a):
                if a == 0:
                        ten = 'Nam'
                else: ten = 'Nữ'
                return ten
        def DanToc(self,a):
                sql_cmd= "SELECT TenDanToc FROM DanToc WHERE MaDanToc=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten
        def TonGiao(self,a):
                sql_cmd= "SELECT TenTonGiao FROM TonGiao WHERE MaTonGiao=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten
        def MaNghe(self,a):
                sql_cmd= "SELECT TenNghe FROM NgheNghiep WHERE MaNghe=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten
        def KhoiLop(self,a):
                sql_cmd= "SELECT TenKhoiLop FROM KhoiLop WHERE MaKhoiLop=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten
        def GiaoVien(self,a):
                sql_cmd= "SELECT TenGiaoVien FROM GiaoVien WHERE MaGiaoVien=%s"
                self.__db_cur.execute(sql_cmd,[a])
                result = self.__db_cur.fetchall()
                ten= "".join(str(x) for x in result[0])
                return ten