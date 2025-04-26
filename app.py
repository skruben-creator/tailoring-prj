from flask import Flask, render_template, flash, request, session, send_file

from datetime import datetime
import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '789546321452145a'


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/adminlogin")
def adminlogin():
    return render_template('adminlogin.html')

@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/USER", methods=['GET', 'POST'])
def USER():
    if request.method == 'POST':

        uname = request.form['uname']
        age = request.form['age']
        gender = request.form['gender']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + uname + "','" + age + "','" + gender + "'" ",'" + mobile + "','" + email + "','" + password +"' )")

        conn.commit()
        conn.close()
        flash('New User Register Successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM regtb ")
        data = cur.fetchall()


    return render_template('user.html',data=data)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():

    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + uname + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash("UserName or Password is wrong...!")

            return render_template('user.html')

        else:


            conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + uname + "' and password='" + password + "'")
            data = cur.fetchall()
            flash("Your are Logged In...!")

            return render_template('userhome.html', data=data)

@app.route("/ADMINLOGIN", methods=['GET', 'POST'])
def ADMINLOGIN():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            return render_template('adminhome.html', data=data)


        else:
            flash("Username or Password is wrong")
            return render_template('adminlogin.html')

@app.route("/adminhome")
def adminhome():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()

    return render_template('adminhome.html',data=data)

@app.route("/userhome")
def userhome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + uname + "' ")
    data = cur.fetchall()

    return render_template('userhome.html',data=data)

@app.route("/bookappointment")
def bookappointment():
    return render_template('book_appointment.html')


@app.route("/BOOKAPPOINTMENT", methods=['GET', 'POST'])
def BOOKAPPOINTMENT():
    if request.method == 'POST':
        username=session['uname']

        name = request.form['name']
        mobile = request.form['mobile']
        landmark = request.form['landmark']
        city = request.form['city']
        pincode = request.form['pincode']
        buildingFloor = request.form['buildingFloor']
        serviceType = request.form['serviceType']
        appointmentDate = request.form['appointmentDate']
        appointmentTime = request.form['appointmentTime']
        garmentCount = request.form['garmentCount']
        message = request.form['message']
        session["mobile"]=request.form['mobile']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cursor = conn.cursor()
        cursor.execute( "INSERT INTO bookapp VALUES ('','" + name + "','" + mobile + "','" + landmark + "' ,'" + city + "','" + pincode + "','" + buildingFloor +"','" + serviceType +"','" + appointmentDate +"','" + appointmentTime +"','" + garmentCount +"','" + message +"','waiting','"+username+"','','Not Paid')")


        conn.commit()
        conn.close()
        flash('Booking Successfully Waiting For Conformation')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  bookapp where username='"+session['uname']+"' ")
        data = cur.fetchall()
        return render_template('Uviewstatus.html', data=data)






@app.route("/Uviewstatus")
def Uviewstatus():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookapp where username='" + uname + "' and status='waiting' ")
    data2 = cur.fetchall()
    cur.execute("SELECT * FROM bookapp where username='" + uname + "' and status='Accept' ")
    data = cur.fetchall()
    cur.execute("SELECT * FROM bookapp where username='" + uname + "' and status='Reject' ")
    data1 = cur.fetchall()
    return render_template('Uviewstatus.html', data=data,data1=data1,data2=data2)

@app.route("/Aviewbook")
def Aviewbook():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookapp where status='waiting'")
    data = cur.fetchall()
    return render_template('Aviewbook.html', data=data)




@app.route("/Accept")
def Accept():
    id = request.args.get('id')
    session['aid'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookapp where id='" +session['aid']+ "' ")
    data = cursor.fetchone()
    if data:
        mobile = data[2]
        conn.commit()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cursor = conn.cursor()
        cursor.execute("update bookapp set status='Accept' where id='" + str(session['aid']) + "' ")

        conn.commit()
        sendmsg(mobile, "Your booking has been accepted successfully!")
        conn.close()

        flash('Accepted Successfully!')
        return render_template('Aviewbook.html')


@app.route("/Reject")
def Reject():
    id = request.args.get('id')
    session['rid'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookapp where id='" +session['rid']+ "' ")
    data = cursor.fetchone()
    if data:
        mobile = data[2]
        conn.commit()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cursor = conn.cursor()
        cursor.execute("update bookapp set status='Reject' where id='" + str(session['rid']) + "' ")

        conn.commit()
        sendmsg(mobile, "Your booking has been  Rejected!")
        conn.close()

        flash('Rejected!')
        return render_template('Aviewbook.html')

@app.route("/Update")
def Update():
    id = request.args.get('id')
    session['sid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookapp where id='" + session['sid'] + "' ")
    data = cursor.fetchone()
    if data:
        mobile = data[2]
        conn.commit()
        session['mobileu']=mobile
        return render_template('Aupdate.html')

@app.route("/messupdate", methods=['GET', 'POST'])
def messupdate():
    if request.method == 'POST':
        king=session['mobileu']


        abc = request.form['messagea']



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cursor = conn.cursor()
        cursor.execute("update bookapp set mess='"+abc+"' where id='" + str(session['sid']) + "' ")

        conn.commit()
        sendmsg(king,abc)
        conn.close()

        flash('Updated Successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookapp where status='Accept' ")
        data = cur.fetchall()

        return render_template('messupdate.html',data=data)



@app.route("/AdminAccept")
def AdminAccept():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookapp where status='Accept' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookapp where status='Reject' ")
    data1 = cur.fetchall()

    return render_template('messupdate.html',data=data,data1=data1)

@app.route("/payment")
def payment():
    id = request.args.get('id')
    session['did'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cursor = conn.cursor()
    cursor.execute("update bookapp set payment='PAID' where id='" + str(session['did']) + "' ")
    conn.commit()

    conn.close()

    flash('Payment Paid Successfully!')
    return render_template('Uviewstatus.html')

@app.route("/Upaymentdetails")
def Upaymentdetails():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookapp  where username='" + uname + "' ")
    data = cur.fetchall()

    return render_template('Upaymentdetails.html',data=data)


@app.route("/apaymentdetails")
def apaymentdetails():
    return render_template('Apaymentdetails.html')

@app.route("/APAYMENTDETAILS", methods=['GET', 'POST'])
def APAYMENTDETAILS():
    if request.method == 'POST':


        mobilee= request.form['mobilee']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='tailorshopdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookapp  where mobile='" + mobilee + "' ")
        data = cur.fetchall()

        return render_template('Apaymentdetails.html', data=data)


@app.route("/desgin")
def desgin():
    return render_template('Add_design.html')



























def sendmsg(targetno,message):
    import requests
    requests.post("http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")






















if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)