from connection import *
username = "sudarshanpujari97@gmail.com"
password = "sudarshan"
# result = db.login.find_one({"username": username, "password":password})
result = db.login.find_one({"username": "username", "password":"adfa"})
# for i in result:
#     print(i['username'])
#     print(i['password'])
# print(result['username'])
# print(result['password'])
if result is None:
    # if result['username'] == username and result['password'] == password:
    print("FAIL")
else:
    print("PASS")