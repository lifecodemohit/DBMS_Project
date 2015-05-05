import csv
import MySQLdb

MAXCOL = 3   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Customer")

sql = """CREATE TABLE Customer (cname VARCHAR(30)  NOT NULL, address VARCHAR(100), amount DOUBLE, PRIMARY KEY (cname))"""

cursor.execute(sql)

with open('Customer.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Customer(cname,address,amount) VALUES ('%s', '%s', '%f')" % (row[0],row[1],float(row[2]))
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()