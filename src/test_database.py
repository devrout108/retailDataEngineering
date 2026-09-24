from database import DatabaseConnection


db = DatabaseConnection()

connection = db.connect()

print("Connection test successful")

db.close()