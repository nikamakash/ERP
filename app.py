from flask import Flask, request, redirect, session, flash, render_template, Response
import pytz
import datetime
import sqlite3
import smtplib
import socket
import numpy as np
# import winsound
import matplotlib.pyplot as plt
import os
import csv

timezone = pytz.timezone('Asia/Calcutta')
today = datetime.datetime.now(tz=timezone)
time, date = (today.strftime("%I:%M %p"), today.date().__format__("%d %B, %Y"))
app = Flask(__name__)
app.secret_key = 'ERP'


@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/admin')
def admin():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('select * from students;')
    students = cursor.fetchall()
    cursor.execute('select * from faculty;')
    faculties = cursor.fetchall()
    return render_template('admin.html', students=students, faculties=faculties)


# ***************************************************************************
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/student', methods=["GET", "POST"])
def registerstudent():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        insert = 'insert into students(name,email,password) values(?,?,?);'
        cursor.execute(insert, (name, email, password))
        conn.commit()
        conn.close()
        flash('Registration Success ...!')
        return redirect("/")
    return render_template('registration.html')


@app.route('/register/faculty', methods=["GET", "POST"])
def registerfaculty():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        insert = 'insert into faculty(name,email,password) values(?,?,?);'
        cursor.execute(insert, (name, email, password))
        conn.commit()
        conn.close()
        flash('Registration Success ...!')
        return redirect("/")
    return render_template('registration.html')


@app.route("/register/mgmt", methods=["GET", "POST"])
def registermgmt():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        insert = 'insert into mgmt(name,email,password) values(?,?,?);'
        cursor.execute(insert, (name, email, password))
        conn.commit()
        conn.close()
        flash('Registration Success ...!')
        return redirect("/")
    return render_template('registration.html')


@app.route('/register/principal', methods=["GET", "POST"])
def registerprincipal():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        insert = 'insert into principal(name,email,password) values(?,?,?);'
        cursor.execute(insert, (name, email, password))
        conn.commit()
        conn.close()
        flash('Registration Success ...!')
        return redirect("/")
    return render_template('registration.html')


# ***********************************************************************


@app.route("/Logout/LogoutStudent", methods=["GET", "POST"])
def LogoutStudent():
    session.pop('user', None)
    session.pop('name', None)
    session.pop('id', None)
    flash('Logged Out Successfully..', "success")
    return redirect("/")


@app.route("/Logout/LogoutFaculty", methods=["GET", "POST"])
def LogoutFaculty():
    session.pop('user', None)
    session.pop('name', None)
    session.pop('id', None)
    flash('Logged Out Successfully..', "success")
    return redirect("/")


@app.route("/Logout/Logoutmgmt", methods=["GET", "POST"])
def LogoutMgmt():
    session.pop('user', None)
    session.pop('name', None)
    session.pop('id', None)
    flash('Logged Out Successfully..', "success")
    return redirect("/")


# ************************************************************************************


@app.route("/Login/StudentLogin", methods=["GET", "POST"])
def StudentLogin():
    if request.method == "POST":
        email_ = request.form['email']
        pass_ = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        select = 'select * from students where email=? and password=?;'
        cursor.execute(select, (email_, pass_))
        print(email_, pass_)
        data = cursor.fetchone()
        conn.close()
        print(data)
        if data is not None:
            result = data
            if len(result) > 0:
                session['user'] = result[2]
                session['name'] = result[1]
                session['id'] = result[0]
                flash('Logged In Successfully !..', "success")
                return redirect('/Dashboard')
        flash('Invalid Credentials ...')
        return render_template("Login.html")
    return render_template("Login.html")


@app.route("/Login/FacultyLogin", methods=["GET", "POST"])
def FacultyLogin():
    if request.method == "POST":
        email_ = request.form['email']
        pass_ = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        select = 'select * from faculty where email=? and password=?;'
        cursor.execute(select, (email_, pass_))
        print(email_, pass_)
        data = cursor.fetchone()
        conn.close()
        print(data)
        if data is not None:
            result = data
            if len(result) > 0:
                session['user'] = result[2]
                session['name'] = result[1]
                session['id'] = result[0]
                flash('Logged In Successfully !..', "success")
                return redirect('/FacultyDashboard')
        flash('Invalid Credentials ...')
        return render_template("Login.html")
    return render_template("Login.html")


@app.route("/Login/ManagementLogin", methods=["GET", "POST"])
def ManagementLogin():
    if request.method == "POST":
        email_ = request.form['email']
        pass_ = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        select = 'select * from mgmt where email=? and password=?;'
        cursor.execute(select, (email_, pass_))
        print(email_, pass_)
        data = cursor.fetchone()
        conn.close()
        print(data)
        if data is not None:
            result = data
            if len(result) > 0:
                session['user'] = result[2]
                session['name'] = result[1]
                session['id'] = result[0]
                flash('Logged In Successfully !..', "success")
                return redirect('/mgmtDashboard')
        flash('Invalid Credentials ...')
        return render_template("Login.html")
    return render_template("Login.html")


@app.route("/Login/PrincipalLogin", methods=["GET", "POST"])
def PrincipalLogin():
    if request.method == "POST":
        email_ = request.form['email']
        pass_ = request.form['password']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        select = 'select * from principal where email=? and password=?;'
        cursor.execute(select, (email_, pass_))
        print(email_, pass_)
        data = cursor.fetchone()
        conn.close()
        print(data)
        if data is not None:
            result = data
            if len(result) > 0:
                session['user'] = result[2]
                session['name'] = result[1]
                session['id'] = result[0]
                flash('Logged In Successfully !..', "success")
                return redirect('/mgmtDashboard')
        flash('Invalid Credentials ...')
        return render_template("Login.html")
    return render_template("Login.html")


# ***************************************************************


@app.route("/Dashboard", methods=["GET", "POST"])
def Dashboard():
    if request.method == "POST":
        if session['user']:
            attendance = request.form['attendance']
            print(session['id'])
            print(attendance)
            print(today.date().day)
            print(today.date().month)
            print(today.date().year)

            if attendance == '0':
                conn = sqlite3.connect('attendance.db')
                cursor = conn.cursor()
                attend = "INSERT into attendance(type, user_id, name,  attendance, date, month, year)" \
                         " VALUES( 'student',?,?,?,?,?,? ); "
                cursor.execute(attend, (session['id'], session['name'], 0, today.date().day,
                                        today.date().month, today.date().year))
                conn.commit()
                conn.close()
                flash('Attendance Saved Successfully !..')
                return redirect("/FacultyDashboard/sendmail")

            elif attendance == '1':
                conn = sqlite3.connect('attendance.db')
                cursor = conn.cursor()
                attend = "INSERT into attendance(type, user_id, name, attendance, date, month, year)" \
                         " VALUES( 'student',?,?,?,?,?,? ); "
                cursor.execute(attend, (session['id'], session['name'], 1, today.date().day,
                                        today.date().month, today.date().year))
                print(cursor.fetchall())
                conn.commit()
                conn.close()
                flash('Attendance Saved Successfully !..', "success")
                return render_template("attendanceDone.html")
            else:
                flash('Error ...!')
                return redirect('/')

    return render_template('dashboard.html', user=session['name'], date=date)


@app.route("/FacultyDashboard", methods=["GET", "POST"])
def FacultyDashboard():
    if request.method == "POST":
        if session['user']:
            attendance = request.form['attendance']
            print(attendance)

            if attendance == '0' or attendance == 'Send Leave Mail':
                conn = sqlite3.connect('attendance.db')
                cursor = conn.cursor()
                attend = "INSERT into attendance(type, user_id, name, attendance, date, month, year)" \
                         " VALUES( " \
                         "'faculty',?,?,?,?,?,? ); "
                cursor.execute(attend, (session['id'], session['name'], 0, today.date().day,
                                        today.date().month, today.date().year))
                conn.commit()
                conn.close()
                flash('Attendance Saved Successfully !..')
                return redirect("/FacultyDashboard/sendmail")

            elif attendance == '1':
                conn = sqlite3.connect('attendance.db')
                cursor = conn.cursor()
                attend = "INSERT into attendance(type, user_id, name, attendance, date, month, year)" \
                         " VALUES( 'faculty',?,?,?,?,?,? ); "
                cursor.execute(attend, (
                    session['id'], session['name'], 1, today.date().day, today.date().month,
                    today.date().year))
                conn.commit()
                conn.close()
                flash('Attendance Saved Successfully !..', "success")
                return render_template("attendanceDone.html")
            else:
                flash('Error ...!')
                return redirect('/')

    return render_template('facultydashboard.html', user=session['name'], date=date)


@app.route("/FacultyDashboard/sendmail", methods=["GET", "POST"])
def sendmail():
    sender = ['senderpmail@gmail.com']
    receivers = ['senderpmail@gmail.com']

    if request.method == "POST":
        subject = request.form['type']
        msg = request.form['msg']
        data = f"""
                Sender:{session['user']}
                {date} {time} 
                {msg}
                """
        message = 'Subject: {}\n\n{}'.format(subject, data)
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        emailq = "insert into emails( name, email_id, date, reason, message) values( ?, ?, ?, ?, ? );"
        cursor.execute(emailq, (session['name'], session['user'], date, subject, msg))
        conn.commit()
        conn.close()

        try:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login('senderpmail@gmail.com', "Arn@4403")
            s.sendmail(sender[0], receivers[0], message, )
            s.quit()
            print("Successfully sent email")
            flash('Attendance Saved Successfully !..', "success")
            return render_template("attendanceDone.html")


        except socket.gaierror:
            print("Internet Connection not found")
            flash('Attendance Saved Successfully !..', "success")
            return render_template("attendanceDone.html")
        except Exception:
            return redirect('/FacultyDashboard/sendmail')

    return render_template("sendmail.html")


# *************************************************************************


@app.route("/mgmtDashboard")
def mgmtdashboard():
    return render_template("mgmtdashboard.html")


@app.route("/mgmtDashboard/studentview", methods=["GET", "POST"])
def studentview():
    if request.method == 'POST':
        year = request.form['Year']
        month = request.form['Month']

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        fetch = "select date, attendance from attendance where year=? and month=? and type='student';"
        cursor.execute(fetch, (year, month))
        data = cursor.fetchall()
        print(data)
        print("***********************")

        if data:
            def cal(dataset):
                store = []
                l = set([i[0] for i in dataset])
                for dates in l:
                    count, absent = 0, 0
                    for j in dataset:
                        while j[0] == dates:
                            if j[1] == 1:
                                count = count + 1
                            else:
                                absent = absent + 1
                            break
                    total = count + absent
                    store.append([dates, count, total, int((count * 100) / total)])
                return store

            res = cal(data)
            monthper = [i[3] for i in res]
            avg = int(sum(monthper) / len(monthper))
            months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                      7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                      12: 'December'}
            dic = int(month)
            session['filter'] = [months[dic], year, avg]
            if res:
                location = 'static/bar.png'
                os.remove(location)
                day = [i[0] for i in res]
                per = [i[3] for i in res]
                y_pos = np.arange(1, len(day) + 1)
                plt.figure(figsize=(13, 5))
                plt.bar(y_pos, per, color=(0.5, 0.1, 0.5, 0.6))
                plt.title("Attendance Percentage")
                plt.xlabel('Dates')
                plt.ylabel('Attendance %')
                plt.ylim(0, 100)
                plt.xticks(day)
                plt.savefig('static/bar.png')
                # if avg < 50:
                    # winsound.PlaySound('Complete', winsound.SND_ALIAS)
                return redirect('/analytics')
        flash('No Data Found...!')
        return redirect('/mgmtDashboard/studentview')
    return render_template('studentview.html')


@app.route("/mgmtDashboard/facultyview", methods=["GET", "POST"])
def facultyview():
    if request.method == 'POST':
        year = request.form['Year']
        month = request.form['Month']
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        fetch = "select date, attendance from attendance where year=? and month=? and type='faculty';"
        cursor.execute(fetch, (year, month))
        data = cursor.fetchall()
        print(data)

        if data:
            def cal(dataset):
                store = []
                l = set([i[0] for i in dataset])
                for dates in l:
                    count, absent = 0, 0
                    for j in dataset:
                        while j[0] == dates:
                            if j[1] == 1:
                                count = count + 1
                            else:
                                absent = absent + 1
                            break
                    total = count + absent
                    store.append([dates, count, total, int((count * 100) / total)])
                return store

            res = cal(data)
            monthper = [i[3] for i in res]
            avg = int(sum(monthper) / len(monthper))
            months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                      7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                      12: 'December'}
            dic = int(month)
            session['filter'] = [months[dic], year, avg]
            if res:
                location = 'static/bar.png'
                os.remove(location)
                day = [i[0] for i in res]
                per = [i[3] for i in res]
                y_pos = np.arange(1, len(day) + 1)
                plt.figure(figsize=(13, 5))
                plt.bar(y_pos, per, color=(0.5, 0.1, 0.5, 0.6))
                plt.title("Attendance Percentage")
                plt.xlabel('Dates')
                plt.ylabel('Attendance %')
                plt.ylim(0, 100)
                plt.xticks(day)
                plt.savefig('static/bar.png')
                # if avg < 50:
                    # winsound.PlaySound('Complete', winsound.SND_ALIAS)
                return redirect('/analytics')
        flash('No Data Found...!')
        return redirect('/mgmtDashboard/facultyview')
    return render_template('facultyview.html')


@app.route('/mgmtDashboard/individual/student', methods=['GET', 'POST'])
def student_analysis():
    if request.method == 'POST':
        name = request.form['Name']
        month = request.form['Month']
        year = request.form['Year']
        print(name, month, year)

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        fetch = "select date, attendance from attendance where year=? and month=? and" \
                " type='student' and name=?;"
        cursor.execute(fetch, (year, month, name))
        data = cursor.fetchall()
        session['data'] = data
        all_data = "select user_id, name, attendance, date, month, year from attendance where year=? and month=?" \
                   " and type='student' and name=?;"
        cursor.execute(all_data, (year, month, name))
        csv_data = cursor.fetchall()
        session['data'] = csv_data
        print(data)

        if data:
            def cal(dataset):
                store = []
                l = set([i[0] for i in dataset])
                for dates in l:
                    count, absent = 0, 0
                    for j in dataset:
                        while j[0] == dates:
                            if j[1] == 1:
                                count = count + 1
                            else:
                                absent = absent + 1
                            break
                    total = count + absent
                    store.append([dates, count, total, int((count * 100) / total)])
                return store

            res = cal(data)
            monthper = [i[3] for i in res]
            avg = int(sum(monthper) / len(monthper))
            months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                      7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                      12: 'December'}
            dic = int(month)
            string = f" {name} in {months[dic]}"
            session['filter'] = [string, year, avg]
            if res:
                location = 'static/bar.png'
                os.remove(location)
                day = [i[0] for i in res]
                per = [i[3] for i in res]
                y_pos = np.arange(1, len(day) + 1)
                plt.figure(figsize=(13, 5))
                plt.bar(y_pos, per, color=(0.5, 0.1, 0.5, 0.6))
                plt.title("Attendance Percentage")
                plt.xlabel('Dates')
                plt.ylabel('Attendance %')
                plt.ylim(0, 100)
                plt.xticks(day)
                plt.savefig('static/bar.png')
                # if avg < 50:
                    # winsound.PlaySound('Complete', winsound.SND_ALIAS)
                return redirect('/analytics/bystudent')
        flash('No Data Found...!')
        return redirect('/mgmtDashboard/individual/student')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('select name from students;')
    students = cursor.fetchall()
    return render_template('individual_student.html', students=students)


@app.route('/mgmtDashboard/individual/faculty', methods=['GET', 'POST'])
def faculty_analysis():
    if request.method == 'POST':
        name = request.form['Name']
        month = request.form['Month']
        year = request.form['Year']
        print(name, month, year)

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        fetch = "select date, attendance from attendance where year=? and month=? and" \
                " type='faculty' and name=?;"
        cursor.execute(fetch, (year, month, name))
        data = cursor.fetchall()
        all_data = "select user_id, name, attendance, date, month, year from attendance where year=? and" \
                   " month=? and type='faculty' and name=?;"
        cursor.execute(all_data, (year, month, name))
        csv_data = cursor.fetchall()
        session['data'] = csv_data
        print(data)

        if data:
            def cal(dataset):
                store = []
                l = set([i[0] for i in dataset])
                for dates in l:
                    count, absent = 0, 0
                    for j in dataset:
                        while j[0] == dates:
                            if j[1] == 1:
                                count = count + 1
                            else:
                                absent = absent + 1
                            break
                    total = count + absent
                    store.append([dates, count, total, int((count * 100) / total)])
                return store

            res = cal(data)
            monthper = [i[3] for i in res]
            avg = int(sum(monthper) / len(monthper))
            months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                      7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                      12: 'December'}
            dic = int(month)
            string = f" {name} in {months[dic]}"
            session['filter'] = [string, year, avg]
            if res:
                location = 'static/bar.png'
                os.remove(location)
                day = [i[0] for i in res]
                per = [i[3] for i in res]
                y_pos = np.arange(1, len(day) + 1)
                plt.figure(figsize=(13, 5))
                plt.bar(y_pos, per, color=(0.5, 0.1, 0.5, 0.6))
                plt.title("Attendance Percentage")
                plt.xlabel('Dates')
                plt.ylabel('Attendance %')
                plt.ylim(0, 100)
                plt.xticks(day)
                plt.savefig('static/bar.png')
                if avg < 50:
                    subject = 'Low Attendance'
                    msg = f"hello, {session['name']}.your attendance is below 50 % for this month."
                    conn = sqlite3.connect('attendance.db')
                    cursor = conn.cursor()
                    emailq = "insert into low_email( name, email_id, date, reason, message) " \
                             "values( ?, ?, ?, ?, ? );"
                    cursor.execute(emailq, (session['name'], session['user'], date, subject, msg))
                    conn.commit()
                    conn.close()
                    # winsound.PlaySound('Complete', winsound.SND_ALIAS)
                return redirect('/analytics/byfaculty')
        flash('No Data Found...!')
        return redirect('/mgmtDashboard/individual/faculty')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('select name from faculty;')
    faculty = cursor.fetchall()
    return render_template('individual_faculty.html', facultys=faculty)


@app.route('/analytics', methods=['GET', 'POST'])
def analytics():
    return render_template('std_graphview.html', filter=session['filter'])


@app.route('/analytics/bystudent', methods=['GET', 'POST'])
def student_analytics():
    return render_template('onestd_graphview.html', filter=session['filter'])


@app.route('/analytics/byfaculty', methods=['GET', 'POST'])
def faculty_analytics():
    return render_template('onefac_graphview.html', filter=session['filter'])


@app.route("/get_csv")
def get_csv():
    with open('attendance.csv', 'w') as f:
        data = session['data']
        fields = ['Id', 'Name', 'Attendance', 'Date', 'Month', 'Year']
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data)
        f.close()
    with open('attendance.csv') as f:
        info = f.read()
        f.close()
        return Response(info, mimetype="text/csv",
                        headers={"Content-disposition": "attachment; filename=attendance.csv"})


# **********************************************************************

if __name__ == "__main__":
    app.run(port=5000)
