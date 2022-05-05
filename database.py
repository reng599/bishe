import pymssql

def dbinit():
	connect = pymssql.connect('LAPTOP-ORS00ARI', 'sa', '123', 'EDUC')
	if connect:
		print("数据库连接成功!")

	return connect

def dbinsert(name,password,phone,mailaddr,conn):
	res = True
	insert = """insert into pyTable(name,password,phone,mail) values(%s,%s,%s,%s)"""
	cursor = conn.cursor()
	try:
		cursor.execute(insert,(name,password,phone,mailaddr))
		conn.commit()
	except Exception as e:
		print('insert failed')
		conn.rollback()
		res = False
	finally:
		return res

def dbsearch(name,conn):
	search = """select * from pyTable where name=%s"""
	cursor = conn.cursor()
	res = None
	try:
		cursor.execute(search,name)
		res = cursor.fetchone()
	except Exception as e:
		print('search failed')
		res = None
	finally:
		return res


def dbinsertinfo(user,time,fromcamera,emailalert,conn):
	iscamera = 1 if fromcamera == '0' else 0
	emailed = 1 if emailalert == True else 0
	insert = """insert into fallTable(username,falltime,fromcamera,emailalert) values(%s,%s,%d,%d)"""
	cursor = conn.cursor()
	try:
		cursor.execute(insert,(user,time,iscamera,emailed))
		conn.commit()
	except Exception as e:
		print("insert info falled "+str(e))
		conn.rollback()
	finally:
		pass

def dbsearchinfo(name,conn):
	search = """select * from fallTable where username=%s"""
	cursor = conn.cursor()
	res = None
	try:
		cursor.execute(search,name)
		res = cursor.fetchall()
	except Exception as e:
		print('search info falled '+str(e))
		res = None
	finally:
		return res

def dbupdatepwd(name,newpwd,conn):
	update = """update pyTable set password=%s where name=%s"""
	cursor = conn.cursor()
	try:
		cursor.execute(update,(newpwd,name))
		conn.commit()
		res = True
	except Exception as e:
		print("update pwd failed "+str(e))
		conn.rollback()
		res = False
	finally:
		return res


def dbupdatephone(name,newphone,conn):
	update = """update pyTable set phone=%s where name=%s"""
	cursor = conn.cursor()
	
	try:
		cursor.execute(update,(newphone,name))
		conn.commit()
		res = True
	except Exception as e:
		print("update phone failed "+str(e))
		conn.rollback()
		res = False
	finally:
		return res


def dbupdatemail(name,newmail,conn):
	update = """update pyTable set mail=%s where name=%s"""
	cursor = conn.cursor()
	try:
		cursor.execute(update,(newmail,name))
		conn.commit()
		res = True
	except Exception as e:
		print("update mail failed "+str(e))
		conn.rollback()
		res = False
	finally:
		return res

def dbclose(conn):
	if conn:
		conn.close()
	print('database closed')


if __name__ == '__main__':
	import datetime
	conn = dbinit()
	res = dbsearchinfo('test',conn)
	test = res[0][1].strftime('%Y-%m-%d %H:%M:%S')
	print(test)
	dbclose(conn)