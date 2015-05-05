import csv
import MySQLdb

MAXCOL = 2   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Likes_artist")

sql = """CREATE TABLE Likes_artist (cname VARCHAR(30) NOT NULL, name VARCHAR(30) NOT NULL, PRIMARY KEY (cname,name), FOREIGN KEY (cname) REFERENCES Customer(cname), FOREIGN KEY (name) REFERENCES Artists(name)
)"""

cursor.execute(sql)

with open('Likes_artist.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Likes_artist(cname,name) VALUES ('%s', '%s')" % (row[0],row[1])
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()