from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose,Admin,AdminIndexView
from flask_login import logout_user, current_user
from flask import redirect
from my_app.models import Thuoc, PhieuKB, BenhNhan, NhanVien, User, LoaiBenh, LoaiDonvi, CachDung, Quydinh
from my_app import app,db,utils
class MyAdminIndex(AdminIndexView):
    @expose("/")
    def index(self):
        stats = utils.thuoc_stats_by_cate()
        return self.render('admin/index.html',stats = stats)


admin = Admin(app=app,
              name="Phong Mach Tu",
              template_mode="bootstrap4",
              index_view=MyAdminIndex())

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class ThuocModelView(AuthenticatedView):

    column_list = (
        'TenThuoc', 'Donvi',  'Gia')
    column_labels = {
        'TenThuoc':'Tên Thuốc',
        'Donvi':'Đơn vị',
        'Gia':'Giá sản phẩm'
    }
    can_export = True;

    can_export = True;


class PhieuKBModelView(AuthenticatedView):
    column_display_pk = True
    column_display_all_relations = True
    column_list = (
    'NgayKham','benhnhan.TenBN','TrieuChung','LoaiBenh', 'thuoc.TenThuoc', 'SoLuong','CachSD')
    column_labels = {
        'NgayKham': 'Ngày Khám',
        'benhnhan.TenBN': 'Tên Bệnh Nhân',
        'TrieuChung':'Triệu Chứng',
        'LoaiBenh':'Dự đoán loại bênh',
        'thuoc.TenThuoc':'Tên Thuốc',
        'SoLuong': 'Số lượng',
        'CachSD':'Cách sử dụng'
    }
    can_export = True;
class NhanVienModelView(AuthenticatedView):
    column_display_pk = True
    column_display_all_relations = True
    column_list = (
        'TenNV','NSinh','Gtinh','DChi','SDT','ChucVu')
    column_labels = {
        'TenNV': 'Tên Nhân Viên',
        'NSinh':'Ngày Sinh',
        'DChi':'Địa Chỉ',
        'Gtinh': 'Giới Tính',
        'ChucVu': 'Chức vụ',
        'SDT': 'Số điện thoại'
    }
    can_export = True;
class BenhNhanModelView(AuthenticatedView):
    column_display_pk = True
    column_display_all_relations = True
    column_list = (
        'TenBN','Nsinh','Gtinh','Dchi','NgayKham')
    column_labels = {
        'TenBN': 'Tên Bệnh Nhân',
        'Dchi':'Địa Chỉ',
        'Nsinh':'Năm Sinh',
        'Gtinh': 'Giới Tính',
        'NgayKham':'Ngày Bắt Đầu Khám'
    }
    can_export = True;
class HoaDonView(BaseView):
    @expose("/")
    def index(self):
        stats = utils.hoadon_stats()
        return self.render("admin/hoadon.html", stats=stats)

    def is_accessible(self):
        return current_user.is_authenticated


class DanhSachTKModelView(AuthenticatedView):
    column_display_pk = True
    column_display_all_relations = True
    column_list = ('name', 'active', 'role','username')
    column_labels = {
        'name':'Họ tên',
        'active':'Tích cực',
        'role':'Quyền người dùng',
        'username':'Tên Tài Khoản'
    }
    can_export = True;

class StatsView(BaseView):
    @expose("/")
    def index(self):
        stats = utils.doanhthu_stats()
        return self.render("admin/stats.html",stats=stats)
    def is_accessible(self):
        return current_user.is_authenticated
class StatsView1(BaseView):
    @expose("/")
    def index(self):
        stats = utils.thuoc_stats_by_cate()
        return self.render("admin/stats1.html",stats=stats)

    def is_accessible(self):
        return current_user.is_authenticated
def is_accessible(self):
    return current_user.is_authenticated

class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/user-login')

    def is_accessible(self):
        return current_user.is_authenticated


class LoaiBenhModelView(AuthenticatedView):
    column_list = ('id','Ten')
    column_labels = {
        'id': 'ID',
        'Ten': 'Tên Loại Bệnh',
    }
    can_export = True;

class DonViModelView(AuthenticatedView):
    column_list = ('id', 'donvi')
    column_labels = {
        'id': 'ID',
        'donvi': 'Đơn vị'
    }
    can_export = True;
class CachDungModelView(AuthenticatedView):
    column_list = ('id', 'cachdung')
    column_labels = {
        'id': 'ID',
        'cachdung': 'Cách dùng'
    }
    can_export = True;

class TienKhamvaSonguoiModelView(AuthenticatedView):
    column_list = ('id', 'ten','quydinh')
    column_labels = {
        'id': 'ID',
        'ten': 'Tên',
        'quydinh': 'quy định'
    }
    can_export = True;


admin.add_view(ThuocModelView(Thuoc, db.session, name="Danh Muc Thuốc"))
admin.add_view(PhieuKBModelView(PhieuKB, db.session, name="Phiếu Khám Bệnh"))
admin.add_view(HoaDonView(name="Danh sách Hóa đơn"))
admin.add_view(StatsView1(name="Thống kê báo cáo sử dụng thuốc"))
admin.add_view(StatsView(name="Thống kê báo cáo doanh thu"))
admin.add_view(BenhNhanModelView(BenhNhan,db.session,name="Danh sách bệnh nhân "))
admin.add_view(NhanVienModelView(NhanVien,db.session,name="Danh sách nhân viên"))
admin.add_view(TienKhamvaSonguoiModelView(Quydinh,db.session,name="Tiền khám và số người tối đa"))
admin.add_view(LoaiBenhModelView(LoaiBenh,db.session,name="Loai Benh"))
admin.add_view(DonViModelView(LoaiDonvi,db.session,name="Don vi"))
admin.add_view(CachDungModelView(CachDung,db.session,name="Cach dung"))
admin.add_view(DanhSachTKModelView(User,db.session,name="Chỉnh sửa Tài Khoản"))
admin.add_view(LogoutView(name="Đăng xuất"))
