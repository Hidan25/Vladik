import json

with open("data.json", "r") as data:
    file = json.load(data)

login = input("Your name")
pas = input("your password")


for user in file["users"]:
    # print(user)
    if login == user["login"] and pas == user["passowrd"]:
        print("Okay")
        break
else:
    print("Hotiv mene naebat?")
    exit(data.json)
