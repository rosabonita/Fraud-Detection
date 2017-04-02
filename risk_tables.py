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

#Note more preprocessing and cleaning from Step 2 needs to happen
#Due to time constraints, will move on to Step 3 and attempt to clean on the go

#Possible variables for analysis
#['transactionCurrencyCode', 'transactionDate', 'transactionDeviceId', 'ipState', 'ipPostalCode', 'ipCountry', 'isProxyIP',  'browserLanguage', 'paymentInstrumentType', 'cardType', 'paymentBillingPostalCode', 'paymentBillingState', 'paymentBillingCountryCode', 'cvvVerifyResult', 'digitalItemCount', 'physicalItemCount', 'accountPostalCode', 'accountState', 'accountCountry', 'accountAge', 'isUserRegistered', 'numPaymentRejects1Day']

#Short list of Categorical Variables
cat_var = ['isProxyIP', 'paymentInstrumentType', 'cardType','cvvVerifyResult', 'isUserRegistered']

#query = "CREATE TABLE IF NOT EXISTS innocent AS SELECT * FROM untagged WHERE tag =0"
#cursor.execute(query)

#count number of distinct entries in categorical variables

#Create Actual Fraud Table from New Fraud
querya = "DROP TABLE isProxyIP_good"
cursor.execute(querya)
queryb = """CREATE TABLE IF NOT EXISTS isProxyIP_good
AS SELECT
  DISTINCT (isProxyIP),
  COUNT(*) AS `num`
FROM
  innocent
GROUP BY
  isProxyIP"""
cursor.execute(queryb)

#Create Actual Fraud Table from New Fraud
querya = "DROP TABLE IF EXISTS isProxyIP_bad"
cursor.execute(querya)
queryb = """CREATE TABLE IF NOT EXISTS isProxyIP_bad
AS SELECT
  DISTINCT (isProxyIP),
  COUNT(*) AS `num`
FROM
  new_fraud
GROUP BY
  isProxyIP"""
cursor.execute(queryb)


