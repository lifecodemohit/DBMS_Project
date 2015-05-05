import csv
import MySQLdb

MAXCOL = 4   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Artwork")

sql = """CREATE TABLE Artwork (year INT, type VARCHAR(30), title VARCHAR(60) NOT NULL, price DOUBLE, aname VARCHAR(30), PRIMARY KEY (title), FOREIGN KEY (aname) REFERENCES Artists(name)
)"""

cursor.execute(sql)

with open('Artwork.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Artwork(year,type,title,price,aname) VALUES ('%d', '%s', '%s', '%f', '%s')" % (int(row[0]),row[1],row[2],float(row[3]),row[4])
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()