import csv
import mysql.connector

#Open FradualentTransactions, eventually will open all 4 files
f = open("UntaggedTransactions_Pt1.csv", 'r')
g = open("untagged_clean_1.csv", 'w')
h = open("rejects_1.csv", 'w')
reader = csv.reader(f, delimiter =",")
for row in reader:
    if len(row[0].split(',')) ==55:
        g.write(row[0] + '\n')
    else:
        h.write(row[0] + '\n')
f.close()
g.close()
h.close()

f = open("UntaggedTransactons_Pt2.csv", 'r')
g = open("untagged_clean_2.csv", 'w')
h = open("rejects_2.csv", 'w')
reader = csv.reader(f, delimiter =",")
for row in reader:
    if len(row[0].split(',')) ==55:
        g.write(row[0] + '\n')
    else:
        h.write(row[0] + '\n')
f.close()
g.close()
h.close()

f = open("UntaggedTransactions_Pt3.csv", 'r')
g = open("untagged_clean_3.csv", 'w')
h = open("rejects_3.csv", 'w')
reader = csv.reader(f, delimiter =",")
for row in reader:
    if len(row[0].split(',')) ==55:
        g.write(row[0] + '\n')
    else:
        h.write(row[0] + '\n')
f.close()
g.close()
h.close()

with open('FraudulentTransactions_2017.csv', 'rb') as f:
    reader = csv.reader(f)
    fraud_headers = next(reader)
    fraud_headers = fraud_headers[0].split(',')

with open('UntaggedTransactions_Pt1.csv', 'rb') as g:
    reader = csv.reader(g)
    untagged_headers = next(reader)
    untagged_headers = untagged_headers[0].split(',')

#Configuration of MYSQL database
config = {
  'user': 'root',
  'password': 'PASSWORD',
  'host': '127.0.0.1',
  #'database': 'test',
  'raise_on_warnings': True,
}

#Get the Column Headers for Fraud Table
fraud_columns = [label + " varchar(255), " for label in fraud_headers]
last = len(fraud_headers)
fraud_columns[last-1] = fraud_columns[last-1].replace(',', ')')
fraud_columns = ''.join(fraud_columns)

#Get Columns for Untagged Table
untagged_columns = [label + " varchar(255), " for label in untagged_headers]
last = len(untagged_headers)
untagged_columns[last-1] = untagged_columns[last-1].replace(',', ')')
untagged_columns = ''.join(untagged_columns)
    
#Connect to MYSQL database
cnx = mysql.connector.connect(**config)

#Initialize MYSQL cursor
cursor = cnx.cursor()

#Initialize new databse
cursor.execute("DROP DATABASE IF EXISTS python")
cursor.execute("CREATE DATABASE python")

#Use the New Database
cursor.execute("USE python")

#Create New Table
cursor.execute("""CREATE TABLE IF NOT EXISTS customer
(
id int primary key,
name varchar(30),
email varchar(30),
city varchar(25),
age int,
gender char(1),
last_visit date)""")

#Create Fraudulent Transactions
cursor.execute("CREATE TABLE IF NOT EXISTS fraud(" +fraud_columns )
cursor.execute("CREATE TABLE IF NOT EXISTS untagged(" +untagged_columns )
#query0 = "ALTER TABLE untagged ADD error VARCHAR(255)" 
#cursor.execute( query0 )

#Load CSV data into table
query = "LOAD DATA LOCAL INFILE 'FraudulentTransactions_2017.csv' INTO TABLE fraud FIELDS TERMINATED BY ',' IGNORE 1 LINES"
#cursor.execute(query)
#untagged_headers = [label + "," for label in untagged_headers]
#x = ''.join(untagged_headers)
#print(x)
query2 = "LOAD DATA LOCAL INFILE 'untagged_clean_1.csv' INTO TABLE untagged  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 LINES "
query3 = "LOAD DATA LOCAL INFILE 'untagged_clean_2.csv' INTO TABLE untagged FIELDS TERMINATED BY ',' IGNORE 1 LINES"
query4 = "LOAD DATA LOCAL INFILE 'untagged_clean_3.csv' INTO TABLE untagged FIELDS TERMINATED BY ',' IGNORE 1 LINES"

cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)

#Show table names (for checking)
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print(tables)

#Commit changes to MYSQL database
cnx.commit()

#Close MYSQL database connection
cnx.close()
