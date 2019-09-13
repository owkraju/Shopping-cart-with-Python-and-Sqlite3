import sqlite3
import os
def Shop():
	con=sqlite3.connect("cart.db")
	c=con.cursor()
	c.execute('''SELECT * FROM product''')
	obj=c.fetchall()
	row_count=len(obj)
	print'***************************************************************************'
	print 'ProductId  ','ProductName  ','ProductPrice  ','ProductQty'
	print '***************************************************************************'
	i=0
	count=0
	while i<row_count:
		print '  ',obj[i][0],' '*(12-len(obj)), obj[i][1],' '*(12-len(obj)), obj[i][2],' '*(12-len(obj)), obj[i][3]
		count+=obj[i][3]
		i=i+1
	print '***************************************************************************'
	print "\t Total Products in cart is:",count
	print '***************************************************************************'
def Add():
	pid=int(input("Enter ProductId:"))
	print("ProdcutId is:",pid)
	pname=raw_input("Enter ProductName:")
	print("ProductName is:",pname)
	pprice=int(input("Enter ProductPrice:"))
	print("ProductPrice is:",pprice)
	pqty=int(input("Enter ProductQuantity:"))
	print("ProductQuantity is:",pqty)
	con=sqlite3.connect("cart.db")
	c=con.cursor()
	d=c.execute("INSERT INTO product (pId,pName,pPrice,pQty) VALUES (?,?,?,?)",(pid,pname,pprice,pqty))
	con.commit()
	if(d):
			print "Inserted successfull!!!!!!!!!!\n\n"
	else:
		print "Soem error occured"
def Update():
	Shop()
	a=int(input("Enter ProductId for updating"))
	if(a):
		pname=raw_input("Enter ProductName:")
		print("ProductName is:",pname)
		pprice=raw_input("Enter ProductPrice:")
		print("ProductPrice is:",pprice)
		pqty=raw_input("Enter ProductQuantity:")
		print("ProductQuantity is:",pqty)
		con=sqlite3.connect("cart.db")
		c=con.cursor()
		d=c.execute("UPDATE product SET pName=?,pPrice=?,pQty=? WHERE pId=?",(pname,pprice,pqty,a))
		con.commit()
		c.close()
	else:
		print("Please provide correct input")

	
def Delete():
	Shop()
	a=raw_input("Enter ProductId for Deleting")
	if(a):
		con=sqlite3.connect("cart.db")
		c=con.cursor()
		c.execute('DELETE FROM product WHERE pId = ?',(a))
		con.commit()
		c.close()
	else:
		print("please give correct input")
print("Welcome to ShoppingCart With Database connection with python")
con=sqlite3.connect("cart.db")
c=con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS product (pId int,pName text,pPrice int,pQty int)''')
con.close()
while(True):
	print("1.Shop Product\n2.Add Prodcut\n3.Update Product\n4.Delete Product\n")
	a=input("Enter your option:-")
	if(a==1):
		Shop()
	elif(a==2):
		Add()
	elif(a==3):
		Update()
	elif(a==4):	
		Delete()
	else:
		print"please provide correct input"

