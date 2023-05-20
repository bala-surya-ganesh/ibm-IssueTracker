from flask import Flask,render_template,request,url_for,session,send_from_directory,redirect
import re
import ibm_db
import os
app = Flask(__name__)
app.secret_key = "1324"
app.config['UPLOAD_FOLDER'] = './static/images/'
print("connecting...")

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rzm08887;PWD=NM02c9OExoYdTRH2;", "", "")
print("connected")

@app.route('/')
def frontpage():
	return render_template('frontpage.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
	msg = ''
	if request.method == "POST":
		USERNAME = request.form["username"]
		PASSWORD = request.form ["password"]
		sq1 = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sq1)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			session['Loggedin'] = True
			session['USERID'] = account['USERID']
			session['USERNAME'] = account['USERNAME']
			msg = "logged in successfully"
			return redirect(url_for('post_compliant'))
		else:
			msg = "Incorrect Email/password"
	return render_template('login.html',msg=msg)


@app.route("/admin_login", methods=[ 'POST', 'GET'])
def admin_login():
	msg = ''
	if request.method == "POST":
		USERNAME = request. form[ "username" ]
		PASSWORD = request. form[ "password"]
		sq1 = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sq1)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc (stmt)
		print(account)
		if account:
			session['Loggedin'] = True
			session['USERID'] = account['USERID']
			session['USERNAME'] = account['USERNAME']
			msg = "logged in successfully !"
			return redirect(url_for("home"))
		else:
			msg = "Incorrect Email/password"
			print(msg)
			return render_template( 'admin_login.html', msg=msg)
	return render_template('admin_login.html', msg=msg)

@app.route("/agent_login", methods=[ 'POST', 'GET'])
def agent_login():
	msg = ''
	if request.method == "POST":
		USERNAME = request.form["username" ]
		PASSWORD = request.form ["password"]
		sql = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param (stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			session[ 'Loggedin'] = True
			session[ 'USERID'] = account['USERID']
			session[ 'USERNAME' ] = account["USERNAME"]
			msg = "logged in successfully"
			return redirect(url_for('home'))
		else:
			msg = "Incorrect Email/password"
			return render_template('agent_login.html', msg=msg)
	return render_template('agent_login.html', msg=msg)


@app.route("/register",methods=['POST', 'GET'])
def register():
	msg = ''
	if request.method == "POST":
		USERNAME = request.form[ "username" ]
		EMAIL = request.form["email" ]
		PASSWORD = request.form["password" ]
		ROLE = 0
		sql = "SELECT * FROM USERN WHERE EMAIL=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, EMAIL)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			msg = "Your signup deatils are already exists in the database Please login"
			return render_template("login.html")
		elif not re.match(r'[^@]+@[^@1+1. [^@]+',EMAIL):
			msg = "Invalid Email Address!"
		else:
			sql = "SELECT count(*) FROM USERN"
			stmt = ibm_db.prepare(conn, sql)
			ibm_db.execute(stmt)
			length = ibm_db.fetch_assoc(stmt)
			print(length)
			insert_sq1 = "INSERT INTO USERN VALUES (?,?,?,?,?)"
			prep_stmt = ibm_db.prepare(conn, insert_sq1)
			ibm_db.bind_param(prep_stmt, 1, length['1']+1)
			ibm_db.bind_param(prep_stmt, 2, ROLE)
			ibm_db.bind_param(prep_stmt, USERNAME)
			ibm_db.bind_param(prep_stmt, EMAIL)
			ibm_db.bind_param(prep_stmt, 5, PASSWORD)
			ibm_db.execute(prep_stmt)
			msg = "You have successfully registered !"
	return render_template('register.html', msg=msg)


@app.route('/admin_register', methods=['POST', "GET"])
def admin_register():
	msg=''
	if request.method == "POST":
		USERNAME = request.form["username" ]
		EMAIL = request.form["email"]
		PASSWORD = request.form["password"]
		ROLE = 1
		secret_key = request.form["secret"]
		sql = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			secret_key == "12345"
			msg = "Your signup deatils are already exists in the database Please login"
			return render_template('login.htm1')
		else:
			secret_key == "12345"
			sql="SELECT count (*) FROM USERN"
			stmt = ibm_db.prepare(conn, sql)
			ibm_db.execute(stmt)
			length = ibm_db.fetch_assoc(stmt)
			print(length)
			insert_sq1 = "INSERT INTO USERN VALUES (?,?, ?, ?, ?)"
			prep_stmt = ibm_db.prepare(conn, insert_sq1)
			ibm_db.bind_param(prep_stmt, 1, length['1']+1)
			ibm_db.bind_param(prep_stmt, 2, ROLE)
			ibm_db.bind_param(prep_stmt, 3, USERNAME)
			ibm_db.bind_param(prep_stmt, 4, EMAIL)
			ibm_db.bind_param(prep_stmt, 5, PASSWORD)
			ibm_db.execute(prep_stmt)
			msg = "You have successfully registered"
			return redirect(url_for('admin_login'))
	return render_template('admin_register.html',msg=msg)


@app.route('/agent_register', methods=['POST', 'GET'])
def agent_register():
	msg=''
	if request .method == 'POST':
		USERNAME = request.form[ "username" ]
		EMAIL = request.form["email"]
		PASSWORD = request.form[ "password" ]
		ROLE = 2
		secret_key = request.form["secret" ]
		sql = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt,2,PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			secret_key = "12345"
			msg = "Your signup deatils are already exists in the database Please login"
			return render_template("login.htm1")
		else:
			secret_key = "12345"
			sql = "SELECT count(*) FROM USERN"
			stmt = ibm_db.prepare(conn, sql)
			ibm_db.execute(stmt)
			length = ibm_db.fetch_assoc(stmt)
			print(length)
			insert_sql = "INSERT INTO USERN VALUES(?,?,?,?,?)"
			prep_stmt = ibm_db.prepare(conn, insert_sql)
			ibm_db.bind_param(prep_stmt, 1, length['1' ]+1)
			ibm_db.bind_param(prep_stmt, 2, ROLE)
			ibm_db.bind_param(prep_stmt, 3, USERNAME)
			ibm_db.bind_param(prep_stmt, 4, EMAIL)
			ibm_db.bind_param(prep_stmt, 5, PASSWORD)
			ibm_db.execute(prep_stmt)
			msg = "You have successfully registered"
			return redirect(url_for('agent_login'))
	return render_template("agent_register.html",msg=msg)


@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('USERID', None)
	return render_template('indexold.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
	sql = "SELECT * FROM USERN WHERE USERID=?"
	stmt = ibm_db.prepare(conn,sql)
	print(str(session['USERID']))
	ibm_db.bind_param(stmt,1, str(session['USERID']))
	ibm_db.execute(stmt)
	User = ibm_db.fetch_tuple(stmt)
	print(User)
	print("data fetched")
	if User[1] == '0':
		if request.method == "POST":
			f = request.files["image"]
			TITLE = request. form.get("title")
			DESCRIPTION = request.form.get("description")
			LAT = request. form.get("lat")
			LONG = request. form.get("lon")
			IMAGE_ID="0"
			if(LAT== "" and LONG == ""):
				return render_template('homeuser.html', data=0)
			else:
				sql = "SELECT * FROM USERN WHERE USERID = ?" +str(session['USERID'])
				stmt = ibm_db.prepare(conn, sql)
				ibm_db.execute(stmt)
				data = ibm_db. fetch_assoc(stmt)
				print (data)
				sq1 = "INSERT INTO TICKETS VALUES(?,?, NULL,?,?,NULL,?,?,?)"
				stmt1 = ibm_db.prepare(conn, sql)
				ibm_db.bind_param(stmt1, 1, data['USERID'])
				ibm_db.bind_param(stmt1, 2, data['USERNAME'])
				ibm_db.bind_param(stmt1, 3, TITLE)
				ibm_db.bind_param(stmt1, 4, DESCRIPTION)
				ibm_db.bind_param(stmt1, LAT)
				ibm_db.bind_param(stmt1, 6, LONG)
				ibm_db.bind_param(stmt1,IMAGE_ID)
				ibm_db.execute(stmt1)
	return render_template('adminhome.html')

@app.route('/post_compliant', methods=['POST', 'GET'])
def post_compliant():
    sql = "SELECT * FROM USERN WHERE USERID = ?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,str(str(session['USERID'])))
    ibm_db.execute(stmt)
    data = ibm_db.fetch_assoc(stmt)
    print(data)
    TITLE = request.form['issue']
    DESCRIPTION = request.form['desc']
    LAT = request.form['lat']
    LONG = request.form['long']
    img = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
    img.save(path)
    sql = "INSERT INTO TICKETS VALUES(?,?, NULL,?,?,NULL,?,?,?)"
    stmt1 = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt1, 1, data['USERID'])
    ibm_db.bind_param(stmt1, 2, data['USERNAME'])
    ibm_db.bind_param(stmt1, 3, TITLE)
    ibm_db.bind_param(stmt1, 4, DESCRIPTION)
    ibm_db.bind_param(stmt1, 5, LAT)
    ibm_db.bind_param(stmt1, 6, LONG)
    ibm_db.bind_param(stmt1, 7, path)
    ibm_db.execute(stmt1)
    return render_template('post_com.html')

@app.route('/status')
def status():
    sql = "SELECT * FROM TICKETS"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.execute(stmt)
    data_li = []
    data = ibm_db.fetch_assoc(stmt)
    print(data)
    while data!=False:
        print(data)
        data = ibm_db.fetch_assoc(stmt)
        data_li.append(data)
    return render_template('viewstatus.html',data=data_li)

@app.route('/admin_home')
def admin_home():
    sql = "SELECT * FROM TICKETS"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.execute(stmt)
    data_li = []
    data = ibm_db.fetch_assoc(stmt)
    print(data)
    while data!=False:
        print(data)
        data = ibm_db.fetch_assoc(stmt)
        data_li.append(data)
    return render_template('adminhome.html',data=data_li)

if __name__=="__main__":
	app.run(debug=True)