import mysql.connector as con
from os import system
from aicommunication import speak

mydb = con.connect(
	host ="localhost",
	user = "root",
	password = ""
)

def alert(string):
	print(string)
	speak(string)


def createTable(tname):
	qry = "CREATE TABLE IF NOT EXISTS "+tname+"("
	fields = int(input("Enter No of Fields :"))
	try:		
		for i in range(fields):
			fname = input("Enter Field Name :")
			qry = qry+fname+" "
			attr = input("Enter Attribute Ex:[ VARCHAR(10) / BIGINT(10) / etc ]")
			qry = qry+attr+","
		qry = qry[:-1]
		qry = qry+")"
		print(qry)
		try:
			cursor.execute(qry)
			alert("Created Table")
		except Exception as e:
			print(e)


	except Exception as e:
		print("Error in Qry Creation ")

cursor = mydb.cursor()


alert("Hii I'm Your MySQL Manager ")

while True:
	print('1.CREATE DataBase\n2.Drop DataBase\n3.Display DataBases\n4.Clear Screen\n5.Select DataBase\n6.EXIT')

	speak('Enter Choice ')

	inp = int(input())

	if inp == 1:
		print("What is name of DataBase :")
		db = input()
		cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db}")
		alert("Created DataBase")

	if inp == 2:
		print("What is name of DataBase :")
		db = input()
		cursor.execute(f"DROP DATABASE {db}")
		alert("Dropped DataBase")

	if inp == 3:
		cursor.execute("SHOW DATABASES")
		for i in cursor:
			print(i)

	if inp == 4:
		system('cls')

	if inp == 5:
		speak("Enter DATABASE name ")
		db = input("Enter DATABASE name :")
		try:
			cursor.execute(f'use {db}')
			speak(f"Selected Database {db}")
			while True:
				tname = ''
				print('1.CREATE Table\n2.Delete Table\n3.Display Table\n4.\n5.Clear Screen\n6.Main Menu')
				speak('Enter Choice ')
				inp = int(input())
				
				if inp == 1:
					speak("Enter table name ")
					tname = input("Enter table name :")
					createTable(tname)

				if inp == 2:
					try:
						alert("Enter table name ");
						tname = input()
						cursor.execute(f"DROP TABLE {tname}")
						alert(f"Table {tname} Deleted ")
					except Exception as e:
						print(e)

				if inp == 3:
					try:
						cursor.execute("SHOW TABLES")
						for i in cursor:
							print(i)
					except Exception as e:
						print(e)

				if inp == 4:


				if inp == 5:
					system('cls') 

				if inp == 6:
					break

		except Exception as e:
			alert("There Was Error Selecting Database !")

			
	if inp == 6:
		exit(0)