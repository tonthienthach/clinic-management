import sys

from flask import render_template, request, redirect, url_for
from my_app import app, my_login, utils
from admin import *
from my_app.models import User, Quydinh
from flask_login import login_user, logout_user
import hashlib
import cloudinary
import cloudinary.uploader


# pass Params

# Request Params

@app.route("/")
def home():
    return render_template("/home.html")


@app.route("/upload", methods=["post"])
def upload():
    avatar = request.files.get("avatar")
    if avatar:
        avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
        return "SUCCESSFUL"
    return "FAILED"


@my_login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=['get', 'post'])
def login_exe():
    username = request.form.get("username")
    password = request.form.get("password")
    # password = str(hashlib.md5(password.encode("utf-8")).digest())
    user = User.query.filter(User.username == username,
                             User.password == password).first()

    if user:  # dang nhap thanh cong
        login_user(user)
        return redirect("/admin")


@app.route("/user-login", methods=['get', 'post'])
def normal_user_login():
    err_msg = ""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        vaitro = request.form.get("role")
        # password = str(hashlib.md5(password.encode("utf-8")).digest())
        user = User.query.filter(User.username == username,
                                 User.password == password,
                                 User.role == vaitro).first()
        print(user.username)

        if user:  # dang nhap thanh cong
            login_user(user)
            if (vaitro == "Benh nhan"):
                return render_template('/BenhNhan.html')
            else:
                if (vaitro == "Y ta"):
                    return render_template('/Yta.html')
                else:
                    if (vaitro == "Bac si"):
                        return render_template('/BacSi.html')
                    else:
                        if (vaitro == "admin"):
                            return redirect("/admin")
        else:
            err_msg = "Username hoac password khong chinh xac!"

    return render_template("login_user.html", err_msg=err_msg)


@app.route("/register", methods=['get', 'post'])
def register():
    err_msg = ""
    if request.method == 'POST':
        try:
            password = request.form["password"]
            confirm_password = request.form['confirm-password']
            if password.strip() == confirm_password.strip():

                data = request.form.copy()
                del data['confirm-password']

                if utils.add_user(**data):
                    return redirect("/user-login")
                else:
                    err_msg = "Du lieu dau vao khong hop le!"
            else:
                err_msg = "Mat khau khong khop!"
        except Exception as ex:

            print("RECEIPT ERROR: " + str(ex))

    return render_template('register.html', err_msg=err_msg)


@app.route("/user-logout")
def normal_user_logout():
    logout_user()

    return redirect("/user-login")


@app.route("/dang-ki-kham-benh", methods=['get', 'post'])
def registerKhanBenh():
    err_msg = ""
    c = Quydinh.query.get(2)
    if request.method == 'POST':
        try:
            data = request.form.copy()
            if utils.count_benhnhan() < c.quydinh:
                if utils.add_benhnhan(**data):
                    return redirect(url_for("dang-ki-kham-benh"))
                else:
                    err_msg = "Du lieu dau vao khong hop le!"
            else:
                return ('so nguoi het r')

        except Exception as ex:

            print("RECEIPT ERROR: " + str(ex))

    return render_template('BenhNhan.html', err_msg=err_msg)


@app.route("/thanh-toan", methods=['get', 'post'])
def thanhtoan():
    err_msg = ""
    phieukham = utils.tienThuoc_stats()

    if request.method == 'POST':
        try:
            data = request.form.copy()
            del data['sttPhieukham1']
            if utils.add_hoadon(**data):
                return redirect(url_for("thanh-toan"))
            else:
                err_msg = "Du lieu dau vao khong hop le!"
        except Exception as ex:

            print("RECEIPT ERROR: " + str(ex))
    hoadon = utils.get_hoadon()

    return render_template('thanhtoan.html', phieukham=phieukham, hoadon=hoadon)


@app.route("/dsbn", methods=['get', 'post'])
def dsbn():
    try:
        dem = 0
        if request.method == 'POST':

            if request.form['TenBN'] == "all" or request.form['TenBN'] == 'All':
                benhnhan = utils.get_benhnhan()
                dem = dem + 1
                return render_template('Dsbn.html', benhnhan=benhnhan)

            else:
                data = request.form['TenBN']
                benhnhan = utils.get_benhnhan(data)
                dem = dem + 1
                return render_template('Dsbn.html', benhnhan=benhnhan)
        if dem == 0:
            benhnhan = utils.get_benhnhan()
            return render_template('Dsbn.html', benhnhan=benhnhan)


    except Exception as ex:

        print("RECEIPT ERROR: " + str(ex))


@app.route("/dsthuoc", methods=['get', 'post'])
def dsthuoc():
    try:
        dem = 0
        if request.method == 'POST':
            if request.form['TenThuoc'] == "all" or request.form['TenThuoc'] == 'All':
                thuoc = utils.get_thuoc()
                return render_template('DSThuoc.html', thuoc=thuoc)
                dem = dem + 1
            else:
                data = request.form['TenThuoc']
                thuoc = utils.get_thuoc(data)
                return render_template('DSThuoc.html', thuoc=thuoc)
                dem = dem + 1
        if dem == 0:
            thuoc = utils.get_thuoc()
            return render_template('DSThuoc.html', thuoc=thuoc)


    except Exception as ex:

        print("RECEIPT ERROR: " + str(ex))


@app.route("/dsphieukham", methods=['get', 'post'])
def dsphieukham():
    err_msg =""
    benhnhan= utils.get_benhnhan()
    loaibenh=utils.get_loaibenh()
    donvi= utils.get_donvi()
    thuoc= utils.get_thuoc()
    cachsd= utils.get_cachdung()

    if request.method == 'POST':
        try:

            data = request.form.copy()
            if utils.add_phieukham(**data):
                return redirect(url_for("dsphieukham"))
            else:
                err_msg = "Du lieu dau vao khong hop le!"


        except Exception as ex:

            print("RECEIPT ERROR: " + str(ex))
    phieukham = utils.get_phieukham()
    return render_template('phieukhambenh.html', err_msg =err_msg,phieukham=phieukham,benhnhan=benhnhan,loaibenh=loaibenh,donvi=donvi,thuoc=thuoc,cachsd=cachsd)


if __name__ == '__main__':
    app.run(debug=True)
