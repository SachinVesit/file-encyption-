from flask import *
from connection import *
# print(db)
result = db.uploadedfiles.insert_one({'username':"sudarshan97@gmail.com"})
print(result)
if result is None:
	print("unsuccessfull")