#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql

#code goes here

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="cyberpower550",db="ian2")
	db.query("""SELECT musicName FROM music;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="cyberpower550",db="ian2")
	db.query("""SELECT DISTINCT musicDescription from Music;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="cyberpower550",db="ian2")
	#db.query("""SELECT * FROM vineyard WHERE vineyardID NOT IN (SELECT * FROM vineyard as a, funding AS b WHERE  
	#	a.vineyardID = b.vineyardID;)""")
	db.query("""SELECT musicName FROM music WHERE statusID =1;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()
	
while buffer:
	print("""
	0.Exit
	1.See bands
	2.See genres
	3.See what bands touring
	""")
	buffer=input("Choose a number ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()