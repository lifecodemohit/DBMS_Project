import csv
import MySQLdb

MAXCOL = 2   #IMPORTANT

db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Belongs_to")

sql = """CREATE TABLE Belongs_to (title VARCHAR(60) NOT NULL, gname VARCHAR(30) NOT NULL, PRIMARY KEY (title,gname), FOREIGN KEY (title) REFERENCES Artwork(title), FOREIGN KEY (gname) REFERENCES Groups(gname)
)"""

cursor.execute(sql)

with open('Belongs_to.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO Belongs_to(title,gname) VALUES ('%s', '%s')" % (row[0],row[1])
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
		   db.rollback()

db.close()