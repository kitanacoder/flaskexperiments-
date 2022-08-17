import MySQLdb

def dconnect():
	db = MySQLdb.connect(host = 'localhost', user = 'root', passwd='iloveyoualeksandr1010', db = 'newcars')
	curs = db.cursor()
	return db, curs

def readdb():
	dat = []
	db, curs = dconnect()
	curs.execute('select * from newcars')
	dat = curs.fetchall()
	return dat

def add(cc, bb, en, br):
	db, curs = dconnect()
	curs.execute('insert into newcars values (%s, %s, %s, %s)', (cc, bb, en, br))
	db.commit()



