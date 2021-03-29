import mysql.connector

mysqlDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        autocommit=True,
        database='FeedbackManagement'
    )