from django.shortcuts import render
from art_gallery.models import *
from django.http import HttpResponse
import MySQLdb


def index(request):
	query_index = ""
	context = ""
	list_attr = []
	if(request.method=='POST') :
		Sql_query = request.POST.get('sql_query')
		Attr1 = request.POST.get('attr1')
		Attr2 = request.POST.get('attr2')
		list_attr.append(Attr1)
		list_attr.append(Attr2)
		Table1 = request.POST.get('table1')
		Table2 = request.POST.get('table2')
		Opr = request.POST.get('opr')
		Table1_par = request.POST.get('table1_par')
		Table2_par = request.POST.get('table2_par')
		Table_name = request.POST.get('table_name')
		Attr_name = request.POST.get('attr_name')
		Order = request.POST.get('order')
		Attr_q3_name = request.POST.get('attr_q3_name')
		Attr_q4_name = request.POST.get('attr_q4_name')
		Attr_q5_name = request.POST.get('attr_q5_name')
		Attr_q6_name = request.POST.get('attr_q6_name')
		Attr_q7_name = request.POST.get('attr_q7_name')
		Attr_q8_name = request.POST.get('attr_q8_name')
		if(str(Sql_query)!="None") :
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = str(Sql_query)
			res=sql.split(' ') 
			print sql
			query_sql=""
			list_sql=[]
			if(res[1]=="*") :
				sql1= "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'DBMS_PROJECT' AND TABLE_NAME = '%s'" %(res[3])
				cursor1 = db.cursor()
				cursor1.execute(sql1)
				data1 = cursor1.fetchall()
				print data1 
				for i in data1 :
					for j in i :
						k=0
						if k>=2:
							data1 += j
							k=k+1
						else :
							k=k+1
					list_sql.append(j)
			else :
				res2 = res[1].split(',')
				for i in res2 :
					list_sql.append(i)
			if(res[0]=='INSERT' or res[0]=='Insert' or res[0]=='DELETE' or res[0]=='Delete' or res[0]=='UPDATE' or res[0]=='Update') :
				try:
				   cursor.execute(sql)
				   db.commit()
				except:
				   db.rollback()
			else :
				cursor.execute(sql)
				data = cursor.fetchall()
				print data 
				query_sql = data
			context= {'list_sql':list_sql,'query_sql':query_sql}
			db.close()
		elif(str(Attr1)!="None" and str(Attr2)!="None") :
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT %s,%s FROM %s,%s WHERE %s.%s %s %s.%s" % (Attr1,Attr2,Table1,Table2,Table1,Table1_par,Opr,Table2,Table2_par)
			#print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			#print data 
			query_index = data
			context= {'list_attr':list_attr,'query_index':query_index}
			db.close()
		elif(str(Table_name)!="None" and str(Attr_name)!="None"):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql= "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'DBMS_PROJECT' AND TABLE_NAME = '%s'" %(Table_name)
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			list2_attr =[]
			for i in data :
				for j in i :
					k=0
					if k>=2:
						data1 += j
						k=k+1
					else :
						k=k+1
				list2_attr.append(j)
			sql = "SELECT * FROM %s ORDER BY %s %s" % (Table_name,Attr_name,Order)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query2_index = data
			context= {'list2_attr':list2_attr,'query2_index':query2_index}
			db.close()
		elif (str(Attr_q3_name)!="None" ):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT Artists.name,birthplace,age,style FROM Customer,Likes_artist,Artists WHERE Customer.cname='%s' AND Customer.cname=Likes_artist.cname AND Artists.name=Likes_artist.name" % (Attr_q3_name)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query3_index = data
			context= {'query3_index':query3_index}
			db.close()
		elif (str(Attr_q4_name)!="None" ):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT Customer.cname,address,amount FROM Customer,Likes_artist,Artists WHERE Artists.name='%s' AND Customer.cname=Likes_artist.cname AND Artists.name=Likes_artist.name" % (Attr_q4_name)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query4_index = data
			context= {'query4_index':query4_index}
			db.close()
		elif (str(Attr_q5_name)!="None" ):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT Groups.gname FROM Customer,Likes_group,Groups WHERE Customer.cname='%s' AND Customer.cname=Likes_group.cname AND Groups.gname=Likes_group.gname" % (Attr_q5_name)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query5_index = data
			context= {'query5_index':query5_index}
			db.close()
		elif (str(Attr_q6_name)!="None" ):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT Customer.cname,address,amount FROM Customer,Likes_group,Groups WHERE Groups.gname='%s' AND Customer.cname=Likes_group.cname AND Groups.gname=Likes_group.gname" % (Attr_q6_name)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query6_index = data
			context= {'query6_index':query6_index}
			db.close()
		elif (str(Attr_q7_name)!="None" ):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT Artwork.title,year,price,type,aname FROM Artwork,Belongs_to,Groups WHERE Groups.gname='%s' AND Artwork.title=Belongs_to.title AND Groups.gname=Belongs_to.gname" % (Attr_q7_name)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query7_index = data
			context= {'query7_index':query7_index}
			db.close()
		elif (str(Attr_q8_name)!="None" ):
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT Groups.gname FROM Artwork,Belongs_to,Groups WHERE Artwork.title='%s' AND Artwork.title=Belongs_to.title AND Groups.gname=Belongs_to.gname" % (Attr_q8_name)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			print data 
			query8_index = data
			context= {'query8_index':query8_index}
			db.close()
		else :
			print "hi"
	
	return render(request, 'index.html', context)

def artists(request):
	query_artists = ""
	if(request.method=='POST') :
		Name = request.POST.get('name')
		Birthplace = request.POST.get('birthplace')
		Age = request.POST.get('age')
		Style = request.POST.get('style')
		#artists=Artists(name=Name,birthplace=Birthplace,age=Age,style=Style)
		Val_birthplace = request.POST.get('val_birthplace')
		Opr1 = request.POST.get('opr1')
		Val_lowage = request.POST.get('val_lowage')
		Opr2 = request.POST.get('opr2')
		Val_highage = request.POST.get('val_highage')
		Opr3 = request.POST.get('opr3')
		Val_style = request.POST.get('val_style')
		D_name = request.POST.get('d_name')
		Attr = request.POST.get('attr')
		Val = request.POST.get('val')
		U_name = request.POST.get('u_name')

		if(str(Name)!="None") :
			#print str(Name)
			print "Artists data saved"
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql="INSERT INTO Artists(name,birthplace,age,style) VALUES ('%s','%s','%d','%s')" % (Name,Birthplace,int(Age),Style)
			#artwork.save()
			print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
			#artists.save()
		elif(str(D_name)!="None") :
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			#print str(D_name)
			print "Artists data deleted"
			sql = "DELETE FROM Artists WHERE name='%s' " % (D_name)
			#print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		elif(str(U_name)!="None") :
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			#print str(D_name)
			print "Artists data updated"
			if(str(Attr)=="age") :
				sql = "UPDATE Artists SET %s='%d' WHERE name='%s' " % (Attr,int(Val),U_name)
			else :	
				sql = "UPDATE Artists SET %s='%s' WHERE name='%s' " % (Attr,Val,U_name)
			#print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		else :
			print "Run query on Artists table"
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT * FROM Artists WHERE birthplace='%s' %s age>='%d' %s age<='%d' %s style='%s' " % (Val_birthplace,Opr1,int(Val_lowage),Opr2,int(Val_highage),Opr3,Val_style)
			#print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			#print data 
			query_artists = data
			db.close()

	list_artists = Artists.objects.all()
	context= {'list_artists':list_artists,'query_artists':query_artists}
	return render(request,'artists.html',context)

def artwork(request):
	query_artwork = ""
	if(request.method=='POST') :
		Year = request.POST.get('year')
		Type = request.POST.get('type')
		Title = request.POST.get('title')
		Price = request.POST.get('price')
		Aname = request.POST.get('aname')
		D_title = request.POST.get('d_title')
		Attr = request.POST.get('attr')
		Val = request.POST.get('val')
		U_title = request.POST.get('u_title')
		Val_year = request.POST.get('val_year')
		Opr1 = request.POST.get('opr1')
		Val_lowprice = request.POST.get('val_lowprice')
		Opr2 = request.POST.get('opr2')
		Val_highprice = request.POST.get('val_highprice')
		Opr3 = request.POST.get('opr3')
		Val_type = request.POST.get('val_type')
		#artwork=Artwork(year=Year,type=Type,title=Title,price=Price,aname=Aname)
		if(str(Title)!="None") :
			#print str(Name)
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			print "Artwork data saved"
			sql="INSERT INTO Artwork(year,type,title,price,aname) VALUES ('%s','%s','%s','%f','%s')" % (Year,Type,Title,float(Price),Aname)
			#artwork.save()
			print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		elif(str(D_title)!="None") :
				db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
				cursor = db.cursor()
				#print str(D_name)
				print "Artwork data deleted"
				sql = "DELETE FROM Artwork WHERE title='%s' " % (D_title)
				#print sql
				try:
				   cursor.execute(sql)
				   db.commit()
				except:
				   db.rollback()
				db.close()
		elif(str(U_title)!="None") :
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			#print str(D_name)
			print "Artwork data updated"
			if(str(Attr)=="price") :
				sql = "UPDATE Artwork SET %s='%f' WHERE title='%s' " % (Attr,float(Val),U_title)
			else :	
				sql = "UPDATE Artwork SET %s='%s' WHERE title='%s' " % (Attr,Val,U_title)
			#print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		else :
			print "Run query on Artwork table"
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT * FROM Artwork WHERE year='%d' %s price>='%f' %s price<='%f' %s type='%s' " % (int(Val_year),Opr1,float(Val_lowprice),Opr2,float(Val_highprice),Opr3,Val_type)
			#print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			#print data 
			db.close()
			query_artwork = data
	list_artwork = Artwork.objects.all()
	context= {'list_artwork':list_artwork,'query_artwork':query_artwork}
	return render(request,'artwork.html',context)

def belongs_to(request):
	if(request.method=='POST') :
		Title = request.POST.get('title')
		Gname = request.POST.get('gname')
		D_title = request.POST.get('d_title')
		D_ganme = request.POST.get('d_gname')
		if(str(Title)!="None" and str(Gname)!="None") :
			#print str(Name)
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			print "Belongs_to data saved"
			sql="INSERT INTO Belongs_to(title,gname) VALUES ('%s','%s')" % (Title,Gname)
			print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		elif(str(D_title)!="None"and str(D_gname)!="None") :
				db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
				cursor = db.cursor()
				#print str(D_name)
				print "Belongs_to data deleted"
				sql = "DELETE FROM Belongs_to WHERE title='%s' AND gname='%s' " % (D_title,D_gname)
				#print sql
				try:
				   cursor.execute(sql)
				   db.commit()
				except:
				   db.rollback()
				db.close()
	#list_bt = Belongs_to.objects.all()
	#print list_bt
	#context= {'list_bt':list_bt}
	context=""
	return render(request,'belongs_to.html',context)

def customer(request):
	query_cust = ""
	if(request.method=='POST') :
		Cname = request.POST.get('cname')
		Address = request.POST.get('address')
		Amount = request.POST.get('amount')
		D_cname = request.POST.get('d_cname')
		Attr = request.POST.get('attr')
		Val = request.POST.get('val')
		U_cname = request.POST.get('u_cname')
		Val_addr = request.POST.get('val_addr')
		Opr1 = request.POST.get('opr1')
		Val_lowamount = request.POST.get('val_lowamount')
		Opr2 = request.POST.get('opr2')
		Val_highamount = request.POST.get('val_highamount')
		#artwork=Artwork(year=Year,type=Type,title=Title,price=Price,aname=Aname)
		if(str(Cname)!="None") :
			#print str(Name)
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			print "Customer data saved"
			sql="INSERT INTO Customer(cname,address,amount) VALUES ('%s','%s','%f')" % (Cname,Address,float(Amount))
			#artwork.save()
			print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		elif(str(D_cname)!="None") :
				db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
				cursor = db.cursor()
				#print str(D_name)
				print "Customer data deleted"
				sql = "DELETE FROM Customer WHERE cname='%s' " % (D_cname)
				#print sql
				try:
				   cursor.execute(sql)
				   db.commit()
				except:
				   db.rollback()
				db.close()
		elif(str(U_cname)!="None") :
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			#print str(D_name)
			print "Customer data updated"
			if(str(Attr)=="amount") :
				sql = "UPDATE Customer SET %s='%f' WHERE cname='%s' " % (Attr,float(Val),U_cname)
			else :	
				sql = "UPDATE Customer SET %s='%s' WHERE cname='%s' " % (Attr,float(Val),U_cname)
			#print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		else :
			print "Run query on Customer table"
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			sql = "SELECT * FROM Customer WHERE address='%s' %s amount>=%f %s amount<=%f " % (Val_addr,Opr1,float(Val_lowamount),Opr2,float(Val_highamount))
			#print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			#print data 
			db.close()
			query_cust = data
	list_cust = Customer.objects.all()
	context= {'list_cust':list_cust,'query_cust':query_cust}
	return render(request,'customer.html',context)

def groups(request):
	query_cust = ""
	if(request.method=='POST') :
		Gname = request.POST.get('gname')
		D_gname = request.POST.get('d_gname')
		if(str(Gname)!="None") :
			#print str(Name)
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			print "Groups data saved"
			sql="INSERT INTO Groups(gname) VALUES ('%s')" % (Gname)
			#artwork.save()
			print sql
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			db.close()
		else:
			db = MySQLdb.connect("localhost","root","mohit1995","DBMS_PROJECT")
			cursor = db.cursor()
			#print str(D_name)
			print "Froups data deleted"
			sql = "DELETE FROM Groups WHERE gname='%s' " % (D_gname)
			#print sql
			try:
				cursor.execute(sql)
				db.commit()
			except:
				db.rollback()
				db.close()
	list_grp = Groups.objects.all()
	context= {'list_grp':list_grp}
	return render(request,'groups.html',context)

def likes_artist(request):
	return HttpResponse("Likes_artist!!")

def likes_group(request):
	return HttpResponse("likes_group!!")
