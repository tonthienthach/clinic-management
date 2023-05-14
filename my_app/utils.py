from my_app.models import User, BenhNhan, Thuoc, HoaDon, PhieuKB, Quydinh, LoaiBenh, LoaiDonvi, CachDung
from my_app import app, db
from flask_login import current_user
from sqlalchemy import func
import hashlib
def add_user(name,username, password, role):
    #password = str(hashlib.md5(password.encode("utf-8")).digest())
    user = User(name=name,
                username=username,
                password=password,
                role=role)
    db.session.add(user)

    try:
        db.session.commit()
        return True
    except:
        return False

def add_benhnhan(TenBN,Gtinh,Nsinh,Dchi):
    benhnhan = BenhNhan(TenBN=TenBN,
                Gtinh=Gtinh,
                Nsinh=Nsinh,
                Dchi=Dchi)
    db.session.add(benhnhan)

    try:
        db.session.commit()
        return True
    except:
        return False

def add_hoadon(sttPhieukham,MaBN,tienthuoc):
    c = Quydinh.query.get(1)

    hoadon = HoaDon(
                sttPhieukham=sttPhieukham,
                MaBN=MaBN,
                tienkham=c.quydinh,
                tienthuoc=tienthuoc)
    db.session.add(hoadon)

    try:
        db.session.commit()
        return True
    except:
        return False
def add_phieukham(MaBN,LoaiBenh,TrieuChung,MaThuoc,SoLuong,CachSD):
    phieukham = PhieuKB(
                MaBN=MaBN,
                LoaiBenh=LoaiBenh,
                TrieuChung=TrieuChung,
                MaThuoc=MaThuoc,
                SoLuong=SoLuong,
                CachSD=CachSD

    )
    db.session.add(phieukham)

    try:
        db.session.commit()
        return True
    except:
        return False


def count_benhnhan():
    return BenhNhan.query.count()

def get_benhnhan(kw=None) :
    benhnhan = BenhNhan.query
    if kw:
        benhnhan= BenhNhan.query.filter(BenhNhan.TenBN.contains(kw))
    return benhnhan.all()

def get_thuoc(kw=None) :
    thuoc= Thuoc.query
    if kw:
        thuoc= Thuoc.query.filter(Thuoc.TenThuoc.contains(kw))
    return thuoc.all()

def get_phieukham(kw=None) :
    phieukham= PhieuKB.query
    if kw:
        phieukham= PhieuKB.query.filter(PhieuKB.id.contains(kw))
    return phieukham.all()

def get_hoadon(kw=None) :
    hoadon = HoaDon.query
    return hoadon.all()

def get_loaibenh(kw=None) :
    loaibenh = LoaiBenh.query
    return loaibenh.all()

def get_donvi(kw=None) :
    donvi = LoaiDonvi.query
    return donvi.all()

def get_cachdung(kw=None) :
    cachdung = CachDung.query
    return cachdung.all()






def thuoc_stats_by_cate():
    return db.session.query(Thuoc.MaThuoc, Thuoc.TenThuoc,Thuoc.Donvi, func.sum(PhieuKB.SoLuong), func.count(PhieuKB.MaThuoc))\
            .join(PhieuKB, PhieuKB.MaThuoc==Thuoc.MaThuoc, isouter=True)\
            .group_by(Thuoc.MaThuoc, Thuoc.TenThuoc,Thuoc.Donvi).all()
def doanhthu_stats():
    return db.session.query(PhieuKB.NgayKham, func.count(PhieuKB.MaBN), func.sum(HoaDon.tienkham+HoaDon.tienthuoc))\
            .join(HoaDon, HoaDon.sttPhieukham==PhieuKB.id, isouter=True)\
            .group_by(PhieuKB.NgayKham).all()
def hoadon_stats():
    return db.session.query(HoaDon.id, BenhNhan.TenBN, PhieuKB.NgayKham, HoaDon.tienkham, HoaDon.tienthuoc, func.sum(HoaDon.tienkham+HoaDon.tienthuoc))\
            .join(BenhNhan, BenhNhan.MaBN == HoaDon.MaBN, isouter=True).join(PhieuKB, PhieuKB.id == HoaDon.sttPhieukham, isouter=True)\
            .group_by(HoaDon.id).all()

def tienThuoc_stats():
    return  db.session.query(PhieuKB.id,PhieuKB.MaBN,func.sum(PhieuKB.SoLuong * Thuoc.Gia)) \
        .join(Thuoc,Thuoc.MaThuoc==PhieuKB.MaThuoc,isouter=True) \
        .group_by(PhieuKB.id).all()


