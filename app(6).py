import datetime

from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import pymysql.connections
import pymysql.cursors
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie, WordCloud, Bar
#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               database='airplane')

#Define a route to hello function
# @app.route('/')
# def hello():
#     if 'username' in session:
# 		if(session['type'] == 'Customer'):
# 			return render_template('Chome.html')
#         return redirect(url_for('home'))
#     return render_template('search_result.html')

@app.route('/')
def home():
    # if(session):
    #     if session['type'] == 'Customer':
    #         return render_template('Chome.html')
    #     elif session['type'] == 'Booking Agent':
    #         return render_template('Bhome.html')
    #     elif session['type'] == 'Airline Staff':
    #         return render_template('Ahome.html')
    # else:
    return render_template('search_result.html', error = None)
# 飞机列表
@app.route("/flightlist",methods=["GET","POST"])
def flightlist():
	start_time=request.args.get("start_time",None)
	end_time=request.args.get("end_time",None)
	depart_airport=request.args.get("depart_airport",None)
	arrive_airport=request.args.get("arrive_airport",None)
	print(start_time)
	query_plane = "SELECT * FROM flight WHERE name_airline = '{}'".format(session['airline'])
	# 构造sql查询条件语句
	if depart_airport is not None and depart_airport!="":
		query_plane+=" AND depart_airport = '{}'".format(depart_airport)
	if arrive_airport is not None and arrive_airport!="":
		query_plane+=" AND arrive_airport = '{}'".format(arrive_airport)
	if start_time is not None and start_time!="":
		query_plane+=" AND depart_time >= '{}' And depart_time<='{}'".format(start_time,end_time)
		query_plane+=" AND arrive_time >= '{}' And arrive_time<='{}'".format(start_time,end_time)
	conn.ping(reconnect=True)
	cursor1 = conn.cursor()
	print(query_plane)

	cursor1.execute(query_plane)
	# stores the results in a variable
	data2 = cursor1.fetchall()
	print(data2)

	return render_template('flightlist.html', data2=data2,start_time=start_time,end_time=end_time,depart_airport=depart_airport,arrive_airport=arrive_airport)
# 飞机列表
@app.route("/planelist",methods=["GET","POST"])
def planelist():
	query_plane = "SELECT * FROM airplane WHERE name_airline = '{}'".format(session['airline'])
	conn.ping(reconnect=True)

	cursor1 = conn.cursor()

	cursor1.execute(query_plane)
	# stores the results in a variable
	data2 = cursor1.fetchall()
	print(data2)

	return render_template('planelist.html', data2=data2)
# 创建飞机
@app.route("/addPlane", methods=['GET', 'POST'])
def addPlane():
	if request.method=="GET":
		print(session['permission'])
		print(type(session['permission']))
		if str(session['permission'])=="88":
			return redirect("/planelist")
		conn.ping(reconnect=True)

		# cursor used to send queries
		cursor1 = conn.cursor()


		query_plane = "SELECT name FROM airline"

		cursor1.execute(query_plane)
		# stores the results in a variable
		data2 = cursor1.fetchall()

		return render_template('addPlane.html',data2=data2)
	else:

		name_airline = request.form['name_airline']
		plane_id = request.form['plane_id']

		query1 = "INSERT INTO airplane VALUES ('{}','{}')"
		cursor1 = conn.cursor()
		cursor1.execute(query1.format(plane_id,name_airline))
		conn.commit()
		cursor1.close()
		return redirect('/planelist')

# 	添加一个航班
@app.route("/addFlight", methods=['GET', 'POST'])
def addFlight():
	if request.method=="GET":
		conn.ping(reconnect=True)

		query1 = "SELECT * FROM airport"
		# cursor used to send queries
		cursor1 = conn.cursor()
		# executes query
		cursor1.execute(query1)
		# stores the results in a variable
		data1 = cursor1.fetchall()
		print(data1)

		query_plane = "SELECT id FROM airplane WHERE name_airline = '{}'"

		cursor1.execute(query_plane.format(session['airline']))
		# stores the results in a variable
		data2 = cursor1.fetchall()
		print(data2)

		return render_template('addFlight.html',data2=data2,data1=data1)
	else:
		conn.ping(reconnect=True)

		flight_num = request.form['flight_num']
		depart_time = request.form['depart_time']
		arrive_time = request.form['arrive_time']
		price = request.form['price']
		name_airline = request.form['name_airline']
		plane_id = request.form['plane_id']
		depart_airport = request.form['depart_airport']
		arrive_airport = request.form['arrive_airport']
		query1 = "INSERT INTO flight VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')"
		cursor1 = conn.cursor()
		cursor1.execute(query1.format(flight_num,depart_time,arrive_time,price,'up_coming',name_airline,plane_id,depart_airport,arrive_airport))
		conn.commit()
		cursor1.close()
		return redirect('/flightlist')
# 更改航班状态
@app.route("/flightstatus", methods=['GET', 'POST'])
def flightstatus():
	conn.ping(reconnect=True)

	id=request.args.get("id")
	status=request.args.get("status")
	sql="update flight set status='{}' where flight_num='{}'".format(status,id)
	# cursor used to send queries
	cursor1 = conn.cursor()
	# executes query
	cursor1.execute(sql)
	conn.commit()
	return redirect("/flightlist")


# 机场列表查询
@app.route("/airportlist",methods=["GET","POST"])
def airportlist():
	conn.ping(reconnect=True)

	query_plane = "SELECT * FROM airport"

	cursor1 = conn.cursor()

	cursor1.execute(query_plane)
	# stores the results in a variable
	data2 = cursor1.fetchall()
	print(data2)

	return render_template('airportlist.html', data2=data2)

# 添加机场
@app.route("/addAirport", methods=['GET', 'POST'])
def addAirport():
	conn.ping(reconnect=True)

	if request.method=="GET":
		# 如果每月权限将跳转到列表
		if str(session['permission'])=="88":
			return redirect("/airportlist")
		# cursor used to send queries

		return render_template('addAirport.html')
	else:

		name = request.form['name']
		city = request.form['city']

		query1 = "INSERT INTO airport VALUES ('{}','{}')"
		cursor1 = conn.cursor()
		cursor1.execute(query1.format(name,city))
		conn.commit()
		cursor1.close()
		return redirect('/airportlist')
#代理列表查询
@app.route("/agentlist",methods=["GET","POST"])
def agentlist():
	conn.ping(reconnect=True)

	query_plane = "SELECT * FROM works_for"

	cursor1 = conn.cursor()

	cursor1.execute(query_plane)
	# stores the results in a variable
	data2 = cursor1.fetchall()

	return render_template('workforlist.html', data2=data2)

# 添加代理
@app.route("/addagent", methods=['GET', 'POST'])
def addagent():
	conn.ping(reconnect=True)

	if request.method=="GET":
		# 没权限跳转代理列表
		if str(session['permission']) == "88":
			return redirect("/agentlist")
		# cursor used to send queries

		return render_template('addWorkfor.html')
	else:

		email = request.form['email']

		query1 = "INSERT INTO works_for VALUES ('{}','{}')"
		cursor1 = conn.cursor()
		cursor1.execute(query1.format(session['airline'],email))
		conn.commit()
		cursor1.close()
		return redirect('/agentlist')
@app.route('/chome')
def chome():
	conn.ping(reconnect=True)

	return redirect("/viewCus")

@app.route('/bhome')
def bhome():
	conn.ping(reconnect=True)

	return render_template('Bhome.html')
@app.route('/ahome')
def ahome():
	conn.ping(reconnect=True)

	print(session['type'])
	return render_template('Ahome.html')
# 退出登陆
@app.route("/logout")
def logout():
	conn.ping(reconnect=True)

	session['username']=""
	session['type']=""
	return redirect('/')
#Define route for login
@app.route('/login',methods=['GET', 'POST'])
def login():
	conn.ping(reconnect=True)

	if request.method=="GET":
		return render_template('login.html')


	type = request.form.get("logtype")
	username = request.form['username']
	password = request.form['password']

	if type == 'Customer':
		query1 = "SELECT * FROM customer WHERE email = '{}' and password = '{}'"
		query2 = "SELECT * FROM customer WHERE email = '{}'"

	elif type == 'Agent':
		query1 = "SELECT * FROM agent WHERE email = '{}' and password = '{}'"
		query2 = "SELECT * FROM agent WHERE email = '{}'"
	elif type == 'Airline Staff':
		query1 = "SELECT * FROM airline_staff WHERE username = '{}' and password = '{}'"
		query2 = "SELECT * FROM airline_staff WHERE username = '{}'"

	# cursor used to send queries
	cursor1 = conn.cursor()
	# executes query
	cursor1.execute(query1.format(username, password))
	# stores the results in a variable
	data1 = cursor1.fetchone()
	cursor2 = conn.cursor()
	cursor2.execute(query2.format(username))
	data2 = cursor2.fetchone()
	# fetchall() if data rows > 2, and close the cursors
	# Then creates a session for the the user
	# The session is a built in
	cursor1.close()
	cursor2.close()
	error = None

	if (data2):
		if (data1):
			session['username'] = username
			session['type'] = type
			session['email'] = data1[0]
			if (type == 'Customer'):
				return redirect("/")
			elif (type == 'Agent'):
				return redirect("/")
			elif (type == 'Airline Staff'):
				query3 = "SELECT permission_id FROM airline_staff WHERE username = '{}'".format(username)
				query4 = "SELECT name_airline FROM airline_staff WHERE username = '{}'".format(username)
				cursor3 = conn.cursor()
				cursor3.execute(query3)
				data3 = cursor3.fetchone()
				cursor3.close()
				cursor4 = conn.cursor()
				cursor4.execute(query4)
				data4 = cursor4.fetchone()
				cursor4.close()
				session['permission'] = data3[0]
				session['airline'] = data4[0]
				session['username'] = username
				return redirect("/")
		else:
			error = "The password is incorrect"
			return render_template('login.html', error=error)
	else:
		# returns an error message to the html page
		error = 'Username does not exist'
		return render_template('login.html', error=error)


#Define route for register
@app.route('/register')
def register():
	conn.ping(reconnect=True)

	return render_template('register.html')

		
# 注册
#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
	conn.ping(reconnect=True)

	#grabs information from the forms
	rtype = request.args.get('user')
	if rtype == 'Customer':
		return render_template('Cregister.html')
	elif rtype == 'Booking Agent':
		return render_template('Bregister.html')
	elif rtype == 'Airline Staff':
		return render_template('Aregister.html')

@app.route('/Cregister', methods=['GET', 'POST'])
def Cregister():
	conn.ping(reconnect=True)

	username = request.form['username']
	password = request.form['password']
	name = request.form['name']
	building_number = request.form['building_number']
	street = request.form['street']
	city = request.form['city']
	state = request.form['state']
	phone_number = request.form['phone_number']
	passport_number = request.form['passport_number']
	passport_expiration = request.form['passport_expiration']
	passport_country = request.form['passport_country']
	date_of_birth = request.form['date_of_birth']
	query = "SELECT * FROM customer WHERE email = '{}'"
	cursor = conn.cursor()
	cursor.execute(query.format(username))
	data = cursor.fetchone()
	error = None

	if(data):
		error = "This user already exists"
		return render_template('Cregister.html', error = error)
	else:
		insert = "INSERT INTO customer VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')"
		 
	cursor.execute(insert.format(username, name, password ,building_number, street, city, state, phone_number, passport_number, passport_expiration, passport_country, date_of_birth))
	conn.commit()
	cursor.close()
	return render_template('index.html')

@app.route('/Bregister', methods=['GET', 'POST'])
def Bregister():
	conn.ping(reconnect=True)

	username = request.form['username']
	password = request.form['password']
	agent_id = request.form['booking_agent_id']

	query = "SELECT * FROM agent WHERE email = '{}'"
	cursor = conn.cursor()
	cursor.execute(query.format(username))
	data = cursor.fetchone()
	error = None

	if(data):
		error = "This user already exists"
		return render_template('Bregister.html', error = error)
	else:
		insert = "INSERT INTO agent VALUES('{}', '{}', '{}')"

	cursor.execute(insert.format(username, password , agent_id))
	conn.commit()
	cursor.close()
	return render_template('index.html')
	
@app.route('/Aregister', methods=['GET', 'POST'])
def Aregister():
	conn.ping(reconnect=True)

	username = request.form['username']
	password = request.form['password']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	date_of_birth = request.form['date_of_birth']
	authcode = request.form['authcode']
	if authcode=="12345678":
		permission_id=90
	else:

		permission_id = 88
	name_airline = request.form['name_airline']
	query = "SELECT * FROM airline_staff WHERE username = '{}'"
	cursor1 = conn.cursor()
	cursor1.execute(query.format(username))
	data1 = cursor1.fetchone()
	error = None
	if(data1):
		error = "This user already exists"
		return render_template('Aregister.html', error = error)
	else:
		query = "SELECT * FROM airline WHERE name = '{}'"

		cursor2 = conn.cursor()
		cursor2.execute(query.format(name_airline))
		data2 = cursor2.fetchone()
		
		error = None
		if(data2 == None):
			error = "The airline does not exist"
			return render_template('Aregister.html', error = error)
		insert = "INSERT INTO airline_staff VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')"
		print(insert)
		
	cursor1.execute(insert.format(username, password ,first_name, last_name, date_of_birth, permission_id, name_airline))
	conn.commit()
	cursor1.close()
	return redirect("/login")
# 搜索
@app.route('/search', methods = ['Get', 'POST'])
def search():
	conn.ping(reconnect=True)

	dep = request.form['dep_city_port']
	des = request.form['des_city_port']
	date = request.form['date']
	query1 = "SELECT f.flight_num, f.depart_time, f.arrive_time FROM flight f JOIN airport a on f.depart_airport = a.name JOIN\
	 airport b on f.arrive_airport = b.name WHERE (f.depart_airport = '{}' OR a.name = '{}' ) AND\
	 (f.arrive_airport = '{}' OR b.name = '{}') AND depart_time LIKE '{}%' AND status != '1'"

	cursor1 = conn.cursor()
	print(query1.format(dep,dep,des,des,date))
	cursor1.execute(query1.format(dep,dep,des,des,date))
	data1 = cursor1.fetchall()
	error = None
	cursor1.close()
	if(data1):
		return render_template('search_result.html', result = data1, error = None)
	else:
		error = "No result found."
		return render_template('search_result.html', error = error)
# 用户购买
@app.route("/cbuy")
def cbuy():
	conn.ping(reconnect=True)

	id=request.args.get("id",None)
	print(id)
	cursor1 = conn.cursor()
	sql="insert into ticket(flight_num,customer_email) values('{}','{}')"
	cursor1.execute(sql.format(id,session['email']))
	conn.commit()
	return redirect("/viewCus")
# 查看用户自己的飞行航班历史记录
@app.route('/viewCus')
def view_my_flight():
	conn.ping(reconnect=True)

	username= session['username']

	start_time=request.args.get("start_time",None)
	end_time=request.args.get("end_time",None)
	depart_airport=request.args.get("depart_airport",None)
	arrive_airport=request.args.get("arrive_airport",None)
	print(start_time)
	query_plane = "SELECT * FROM flight f right join ticket t on t.flight_num=f.flight_num WHERE customer_email = '{}'".format(session['email'])
	if depart_airport is not None and depart_airport!="":
		query_plane+=" AND depart_airport = '{}'".format(depart_airport)
	if arrive_airport is not None and arrive_airport!="":
		query_plane+=" AND arrive_airport = '{}'".format(arrive_airport)
	if start_time is not None and start_time!="":
		query_plane+=" AND depart_time >= '{}' And depart_time<='{}'".format(start_time,end_time)
		query_plane+=" AND arrive_time >= '{}' And arrive_time<='{}'".format(start_time,end_time)
	cursor1 = conn.cursor()
	print(query_plane)

	cursor1.execute(query_plane)
	# stores the results in a variable
	data2 = cursor1.fetchall()
	print(data2)

	return render_template('viewCus.html', data2=data2,start_time=start_time,end_time=end_time,depart_airport=depart_airport,arrive_airport=arrive_airport)
# 查看代理购买的飞行航班
@app.route('/viewAgent')
def view_agent_flight():
	conn.ping(reconnect=True)

	username= session['username']

	start_time=request.args.get("start_time",None)
	end_time=request.args.get("end_time",None)
	depart_airport=request.args.get("depart_airport",None)
	arrive_airport=request.args.get("arrive_airport",None)
	print(start_time)
	query_plane = "SELECT * FROM flight f right join ticket t on t.flight_num=f.flight_num WHERE agent_email = '{}'".format(session['email'])
	if depart_airport is not None and depart_airport!="":
		query_plane+=" AND depart_airport = '{}'".format(depart_airport)
	if arrive_airport is not None and arrive_airport!="":
		query_plane+=" AND arrive_airport = '{}'".format(arrive_airport)
	if start_time is not None and start_time!="":
		query_plane+=" AND depart_time >= '{}' And depart_time<='{}'".format(start_time,end_time)
		query_plane+=" AND arrive_time >= '{}' And arrive_time<='{}'".format(start_time,end_time)
	cursor1 = conn.cursor()
	print(query_plane)

	cursor1.execute(query_plane)
	# stores the results in a variable
	data2 = cursor1.fetchall()
	print(data2)

	return render_template('viewAgent.html', data2=data2,start_time=start_time,end_time=end_time,depart_airport=depart_airport,arrive_airport=arrive_airport)
# 绘制柱状图，展示半年内前五的客户
@app.route("/getagentchart1")
def etagentchart1():
	conn.ping(reconnect=True)

	starttime = datetime.datetime.today() - datetime.timedelta(days=180)
	starttime = starttime.strftime('%Y-%m-%d')
	sql="select * from (select count(1) as co,t.customer_email from ticket t left join flight f on t.flight_num=f.flight_num  where t.agent_email='{}' and f.arrive_time>='{}' group by t.customer_email ) as t1 order by t1.co desc limit 5"
	cursor=conn.cursor()
	cursor.execute(sql.format(session['email'],starttime))
	data0=cursor.fetchall()

	bar = Bar()
	# data = grouped.to_dict()
	# data = [[k, v] for k, v in data.items()]
	x_info = [x[1] for x in data0]
	y_info = [x[0] for x in data0]
	bar.add_xaxis(x_info)
	bar.add_yaxis("Ticket Num", y_info)
	bar.set_global_opts(
		legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),

	)
	return bar.dump_options_with_quotes()

# 绘制柱状图，展示一年内前五的客户

@app.route("/getagentchart2")
def etagentchart2():
	conn.ping(reconnect=True)

	starttime = datetime.datetime.today() - datetime.timedelta(days=365)
	starttime = starttime.strftime('%Y-%m-%d')
	sql="select * from (select ifnull(sum(f.price),0)/10 as co,t.customer_email from ticket t left join flight f on t.flight_num=f.flight_num  where t.agent_email='{}' and f.arrive_time>='{}' group by t.customer_email ) as t1 order by t1.co desc limit 5"
	cursor=conn.cursor()
	cursor.execute(sql.format(session['email'],starttime))
	data0=cursor.fetchall()

	bar = Bar()
	# data = grouped.to_dict()
	# data = [[k, v] for k, v in data.items()]
	x_info = [x[1] for x in data0]
	y_info = [x[0] for x in data0]
	bar.add_xaxis(x_info)
	bar.add_yaxis("Price Agent", y_info)
	bar.set_global_opts(
		legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),

	)
	return bar.dump_options_with_quotes()
@app.route('/chartAgent1', methods = ['GET', 'POST'])
def chartAgent1():
	conn.ping(reconnect=True)



	return render_template('chartAgent1.html')
# 查询一年内收入前五，销售数量前五，和一月内销售数量前五的客户列表
@app.route("/aagentTop")
def aagentTop():
	conn.ping(reconnect=True)

	starttime = datetime.datetime.today() - datetime.timedelta(days=365)
	starttime = starttime.strftime('%Y-%m-%d')
	sql="select * from (select ifnull(sum(f.price),0)/10 as co,t.agent_email from ticket t left join flight f on t.flight_num=f.flight_num  where  f.arrive_time>='{}' and t.agent_email is not null group by t.agent_email ) as t1 order by t1.co desc limit 5"
	cursor=conn.cursor()
	print(sql.format(starttime))
	cursor.execute(sql.format(starttime))
	data0=cursor.fetchall()
	sql="select * from (select count(1) as co,t.agent_email from ticket t left join flight f on t.flight_num=f.flight_num  where  f.arrive_time>='{}' and t.agent_email is not null  group by t.agent_email ) as t1 order by t1.co desc limit 5"
	cursor=conn.cursor()
	cursor.execute(sql.format(starttime))
	data1=cursor.fetchall()

	sql = "select * from (select count(1) as co,t.agent_email from ticket t left join flight f on t.flight_num=f.flight_num  where f.arrive_time>='{}' and t.agent_email is not null  group by t.agent_email ) as t1 order by t1.co desc limit 5"
	cursor = conn.cursor()
	starttime = datetime.datetime.today() - datetime.timedelta(days=30)

	cursor.execute(sql.format(starttime))
	data2 = cursor.fetchall()

	return render_template('agentTop.html',data0=data0,data1=data1,data2=data2)
# 查询每月销售柱状图
@app.route('/getchartCus')
def getchart():  # put application's code here
	conn.ping(reconnect=True)

	starttime = request.args.get("start_time", None)
	endtime = request.args.get("end_time", None)
	sql="select DATE_FORMAT(arrive_time, '%Y-%m'),ifnull(sum(price),0) from ticket t left join flight f on t.flight_num=f.flight_num where f.arrive_time<='{}' and f.depart_time>='{}' and t.customer_email='{}' group by DATE_FORMAT(arrive_time, '%Y-%m')"
	cursor=conn.cursor()
	cursor.execute(sql.format(endtime,starttime,session['email']))

	data0=cursor.fetchall()
	print(data0)
	bar = Bar()
    # data = grouped.to_dict()
    # data = [[k, v] for k, v in data.items()]
	x_info = [x[0] for x in data0]
	y_info = [x[1] for x in data0]
	bar.add_xaxis(x_info)
	bar.add_yaxis("Price", y_info)
	bar.set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),

    )
	return bar.dump_options_with_quotes()

# 过去一年的每月收入枝状图 staff
@app.route("/report1")
def report1():
	conn.ping(reconnect=True)

	return render_template('chartStafff.html')
# 绘每月收入图表
@app.route('/getchartStaff')
def getchartStaff():  # put application's code here
	conn.ping(reconnect=True)

	starttime = datetime.datetime.today() - datetime.timedelta(days=365)
	starttime = starttime.strftime('%Y-%m-%d')
	sql="select DATE_FORMAT(f.arrive_time, '%Y-%m'),sum(f.price) from ticket t left join flight f on f.flight_num=t.flight_num where f.name_airline='{}'  and f.arrive_time>='{}' group by DATE_FORMAT(f.arrive_time, '%Y-%m')"
	cursor=conn.cursor()
	cursor.execute(sql.format(session['airline'],starttime))

	data0=cursor.fetchall()
	bar = Bar()
    # data = grouped.to_dict()
    # data = [[k, v] for k, v in data.items()]
	x_info = [x[0] for x in data0]
	y_info = [x[1] for x in data0]
	bar.add_xaxis(x_info)
	bar.add_yaxis("Price", y_info)
	bar.set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),

    )
	return bar.dump_options_with_quotes()
# 画饼图
@app.route('/getpie1')
def getpie1():  # put application's code here
	conn.ping(reconnect=True)


	starttime = datetime.datetime.today() - datetime.timedelta(days=30)
	starttime = starttime.strftime('%Y-%m-%d')

	sql="select sum(f.price) from ticket t left join flight f on f.flight_num=t.flight_num where f.name_airline='{}' and t.agent_email is null and f.arrive_time>='{}'"
	cursor=conn.cursor()
	cursor.execute(sql.format(session['airline'],starttime))

	data0=cursor.fetchone()
	sql="select sum(f.price) from ticket t left join flight f on f.flight_num=t.flight_num where f.name_airline='{}' and t.agent_email is not null and f.arrive_time>='{}'"
	cursor.execute(sql.format(session['airline'],starttime))

	data1=cursor.fetchone()
	pie = Pie()
	data = [["no agent", data0[0]], ["agent", data1[0]]]
	pie.add("three months", data)
	pie.set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),

    )
	return pie.dump_options_with_quotes()
# 过去一年收入对比
@app.route('/getpie2')
def getpie2():  # put application's code here
	conn.ping(reconnect=True)


	starttime = datetime.datetime.today() - datetime.timedelta(days=365)
	starttime = starttime.strftime('%Y-%m-%d')

	sql="select sum(f.price) from ticket t left join flight f on f.flight_num=t.flight_num where f.name_airline='{}' and t.agent_email is null and f.arrive_time>='{}'"
	cursor=conn.cursor()
	cursor.execute(sql.format(session['airline'],starttime))

	data0=cursor.fetchone()
	sql="select sum(f.price) from ticket t left join flight f on f.flight_num=t.flight_num where f.name_airline='{}' and t.agent_email is not null and f.arrive_time>='{}'"
	cursor.execute(sql.format(session['airline'],starttime))

	data1=cursor.fetchone()
	pie = Pie()
	data = [["no agent", data0[0]], ["agent", data1[0]]]
	print(data)
	pie.add("a year", data)
	pie.set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),

    )
	return pie.dump_options_with_quotes()

@app.route("/Viewreports")
def Viewreports():
	conn.ping(reconnect=True)

	return render_template('Viewreports.html')

# 查看最频繁的一个客户，并且展示他的航行记录
@app.route("/Viewfrequentcustomers")
def Viewfrequentcustomers():
	conn.ping(reconnect=True)


	cursor=conn.cursor()
	sql="select * from (select t.customer_email,count(1) as co from ticket t left join flight f on f.flight_num=t.flight_num where name_airline='{}' and arrive_time>='{}' group by t.customer_email) as c order by c.co desc limit 1"
	starttime = datetime.datetime.today() - datetime.timedelta(days=365)
	starttime = starttime.strftime('%Y-%m-%d')
	cursor.execute(sql.format(session['airline'],starttime))
	data=cursor.fetchone()
	if data is not None:

		sql="select f.flight_num,f.depart_time,f.arrive_time from ticket t left join flight f on f.flight_num=t.flight_num where name_airline='{}' and customer_email='{}'"
		cursor.execute(sql.format(session['airline'],data[0]))
		data2=cursor.fetchall()
	else:
		data2=[]
	return render_template("Viewfrequentcustomers.html",data=data,data2=data2)
# 查看职员列表
@app.route("/airstafflist")
def airstafflist():
	conn.ping(reconnect=True)

	cursor=conn.cursor()
	sql="select * from airline_staff where name_airline='{}'"
	cursor.execute(sql.format(session['airline']))
	print(sql.format(session['airline']))
	data=cursor.fetchall()

	return render_template("airstafflist.html",data=data)

# 修改权限
@app.route("/addairstaffauth",methods=['GET','POST'])
def addairstaffauth():
	conn.ping(reconnect=True)

	# 无权限修改则返回到列表页
	if str(session['permission'])=="88":
			return redirect("/airstafflist")
	cursor=conn.cursor()
	username=request.args.get("username",None)
	sql="update airline_staff set permission_id='89' where username='{}'"
	cursor.execute(sql.format(username))
	conn.commit()
	return redirect("/airstafflist")


# 代理购买
@app.route("/abuy",methods=['GET','POST'])
def abuy():
	conn.ping(reconnect=True)

	flight_num=request.args.get("flight_num",None)
	cemail=request.args.get("email",None)
	cursor1=conn.cursor()
	sql="select * from works_for wf left join flight f on f.name_airline=wf.name where wf.email='{}' and f.flight_num='{}'"
	cursor1.execute(sql.format(session['email'],flight_num))
	data=cursor1.fetchone()
	if data is None:
		return jsonify({"code":0})
	sql="insert into ticket(flight_num,customer_email,agent_email) values('{}','{}','{}')"
	print(sql.format(flight_num,cemail,session['email']))
	cursor1.execute(sql.format(flight_num,cemail,session['email']))
	conn.commit()
	return jsonify({"code":1})



# 代理查询销售额和消暑数量，近一个月
@app.route("/showagent")
def showagent():
	conn.ping(reconnect=True)

	starttime = request.args.get("start_time", None)
	endtime = request.args.get("end_time", None)
	if starttime is None:
		starttime = datetime.datetime.today() - datetime.timedelta(days=30)
		endtime = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
		starttime = starttime.strftime('%Y-%m-%d')

	sql="select ifnull(sum(price),0)/10,count(1) from ticket t left join flight f on t.flight_num=f.flight_num where t.agent_email='{}' and f.arrive_time<='{}' and f.depart_time>='{}'"
	cursor = conn.cursor()
	print(sql.format(session['email'],endtime, starttime))
	cursor.execute(sql.format(session['email'],endtime, starttime))
	data0 = cursor.fetchone()
	print(data0)
	return render_template("chartAgent.html",data0=data0)

# 查看过去三个月和一年中，最热门的城市
@app.route("/ViewTopdestinations")
def ViewTopdestinations():
	conn.ping(reconnect=True)

	starttime = datetime.datetime.today() - datetime.timedelta(days=90)
	starttime2 = datetime.datetime.today() - datetime.timedelta(days=365)
	starttime=starttime.strftime('%Y-%m-%d')
	starttime2=starttime2.strftime('%Y-%m-%d')
	cursor=conn.cursor()
	query_sql="select * from (select count(1) as co,a.city from ticket t left join flight f on f.flight_num=t.flight_num left join airport a on a.name=f.arrive_airport where f.arrive_time>='{}' GROUP BY a.city) as t order by t.co DESC limit 3"
	cursor.execute(query_sql.format(starttime))
	data0=cursor.fetchall()
	cursor.execute(query_sql.format(starttime2))
	data1=cursor.fetchall()
	return render_template("viewTopdestinations.html",data0=data0,data1=data1)

@app.route('/chartCus', methods = ['GET', 'POST'])
def chartCus():
	conn.ping(reconnect=True)

	starttime=request.args.get("start_time",None)
	endtime=request.args.get("end_time",None)
	if starttime is None:
		starttime=datetime.datetime.today()-datetime.timedelta(days=180)
		starttime2=datetime.datetime.today()-datetime.timedelta(days=365)
		endtime=(datetime.datetime.today()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
		starttime=starttime.strftime('%Y-%m-%d')
		starttime2=starttime2.strftime('%Y-%m-%d')
	else:
		starttime2=starttime
	sql="select ifnull(sum(price),0) from ticket t left join flight f on t.flight_num=f.flight_num where f.arrive_time<='{}' and f.depart_time>='{}' and t.customer_email='{}'"
	cursor=conn.cursor()
	cursor.execute(sql.format(endtime,starttime2,session['email']))
	data0=cursor.fetchall()

	return render_template('chartCus.html',data0=data0,start_time=starttime,end_time=endtime)
@app.route("/tickets")
def tickets():
	id=request.args.get("id")
	conn.ping(reconnect=True)
	sql="select * from ticket where flight_num={}".format(id)

	cursor=conn.cursor()
	cursor.execute(sql)
	data0=cursor.fetchall()
	return render_template("ticketslist.html",data0=data0)


app.secret_key = 'I love NYU Shanghai'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5001, debug = True)
