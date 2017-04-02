import mysql.connector
#Configuration of MYSQL database
config = {
  'user': 'root',
  'password': 'delta3766',
  'host': '127.0.0.1',
  'raise_on_warnings': True,
}
#Connect to MYSQL database
cnx = mysql.connector.connect(**config)

#Initialize MYSQL cursor
cursor = cnx.cursor()

#Use the New Database
cursor.execute("USE python")

cursor.execute("CREATE TABLE IF NOT EXISTS copy LIKE new_fraud")

#Reformat transactionTime
query = "ALTER table new_fraud MODIFY transactionTime INT(6)"
cursor.execute(query)

#Check if new_fraud row is pre-fraud
querya = """UPDATE new_fraud n
INNER JOIN fraud f
ON (n.transactionTime = f.transactionTime) set n.tag = 2;"""
cursor.execute(querya)

#Create Actual Fraud Table from New Fraud
queryb = "CREATE TABLE IF NOT EXISTS actual_fraud AS SELECT * FROM new_fraud WHERE tag =1"
cursor.execute(queryb)

