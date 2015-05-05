import csv
import MySQLdb

MAXCOL = 2   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Likes_group")

sql = """CREATE TABLE Likes_group (cname VARCHAR(30) NOT NULL, gname VARCHAR(30) NOT NULL, PRIMARY KEY (cname,gname), FOREIGN KEY (cname) REFERENCES Customer(cname), FOREIGN KEY (gname) REFERENCES Groups(gname)
)"""

cursor.execute(sql)

with open('Likes_group.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Likes_group(cname,gname) VALUES ('%s', '%s')" % (row[0],row[1])
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()