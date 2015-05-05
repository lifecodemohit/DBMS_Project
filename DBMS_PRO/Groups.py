import csv
import MySQLdb

MAXCOL = 1   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Groups")

sql = """CREATE TABLE Groups (gname VARCHAR(30) NOT NULL, PRIMARY KEY (gname))"""

cursor.execute(sql)

with open('Groups.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Groups(gname) VALUES ('%s')" % (row[0])
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()