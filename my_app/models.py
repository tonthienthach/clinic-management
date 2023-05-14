from sqlalchemy import  Column, String, Integer, Boolean, DateTime, ForeignKey,Date
from my_app import db
from flask_login import UserMixin
from datetime import datetime,date
from sqlalchemy.orm import relationship



class BenhNhan(db.Model):
    MaBN= Column(Integer, primary_key=True)
    TenBN= Column(String(50),nullable=False)
    Gtinh= Column(String(50),nullable=False)
    Nsinh= Column(Integer,nullable=False)
    Dchi = Column(String(50), nullable=False)
    NgayKham=Column(Date, default=date.today())
    phieuKB = relationship('PhieuKB', backref='benhnhan', lazy=True)
    hoadon = relationship('HoaDon', backref='benhnhan', lazy=True)

class NhanVien(db.Model):
    MaNV= Column(Integer, primary_key=True)
    TenNV= Column(String(50),nullable=False)
    NSinh = Column(Date,nullable=False)
    Gtinh= Column(String(50),nullable=False)
    DChi = Column(String(50), nullable=False)
    ChucVu= Column(String(50),nullable=False)
    SDT= Column(String(50),nullable=False)


class LoaiBenh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    Ten= Column(String(50), nullable= False)


class LoaiDonvi(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    donvi = Column(String(50), nullable=False)

class CachDung(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    cachdung = Column(Integer, nullable=False)



class Thuoc (db.Model):
    MaThuoc = Column(Integer, primary_key=True)
    TenThuoc= Column(String(50),nullable=False)
    Donvi  = Column(String(50),nullable=False)
    Gia = Column(Integer,nullable=False)
    phieukb = relationship('PhieuKB',backref="thuoc",lazy=True)

class PhieuKB(db.Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    NgayKham = Column(Date, default=date.today())
    MaBN = Column(Integer, ForeignKey(BenhNhan.MaBN), nullable=False)
    LoaiBenh =  Column(String(50),nullable=False)
    TrieuChung =  Column(String(50),nullable=False)
    MaThuoc = Column(Integer, ForeignKey(Thuoc.MaThuoc),nullable=False)
    SoLuong =Column(Integer,nullable=False)
    CachSD = Column(Integer, nullable=False)

   # hoadon = relationship('HoaDon', backref='phieukb', lazy=True)


class HoaDon(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    MaBN= Column(Integer, ForeignKey(BenhNhan.MaBN),nullable=False)
    sttPhieukham = Column(Integer,ForeignKey(PhieuKB.id), nullable=False)
    tienkham= Column(Integer, nullable=False)
    tienthuoc= Column(Integer, nullable=False)

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    role = Column(String(50), nullable= False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
class Quydinh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten= Column(String(50), nullable=False)
    quydinh= Column(Integer, nullable=False)









def __str__(self):
    return self.name

if __name__ == '__main__':
    db.create_all()