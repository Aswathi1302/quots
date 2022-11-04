import requests
import json
import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database=' quotsdb')
except mysql.connector.Error as e:
    sys.exit("db connection error")
mycursor=mydb.cursor() 
data=requests.get("https://dummyjson.com/quotes").text
data_info=json.loads(data)
print(data_info)

datainf=data_info["quotes"]
for i in datainf:
    id=str(i['id'])
    sql="INSERT INTO `quots`(`id`, `quote`, `author`) VALUES (%s,%s,%s)"
    data=(i['id'],i['quote'],i['author'])
    mycursor.execute(sql,data)
    mydb.commit()
    print("data inserted success",i['id'])