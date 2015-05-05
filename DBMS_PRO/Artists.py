import csv
import MySQLdb

MAXCOL = 4   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Artists")

sql = """CREATE TABLE Artists (name VARCHAR(30) NOT NULL, birthplace VARCHAR(30), age INT, style VARCHAR(30), PRIMARY KEY (name))"""

cursor.execute(sql)

with open('Artists.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Artists(name,birthplace,age,style) VALUES ('%s', '%s', '%d', '%s')" % (row[0],row[1],int(row[2]),row[3])
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()