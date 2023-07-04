import json

newUser = input("Sign in press 'S' or Log in press 'L'")
press = newUser
if press == "l":

    with open("data.json", "r") as data:
     file = json.load(data)
    login = input("Your name")
    pas = input("your password")
    for users in file["users"]:
    # print(user)
     if login == users["login"] and pas == users["password"]:
        print("Okay")
        break
    else:
     print("Hotiv mene naebat?")
    #(data.json)
elif press == "s":
  newUserLogin = input("Your Login")
    # print(newUserLogin)
  newUserPassword = input("Your password")
    # print(newUserPassword)
  with open("data.json", "r") as data:
        file = json.load(data)
  newUser = {"login": newUserLogin, "password": newUserPassword}
  file["users"].append(newUser)  
  with open("data.json", "w") as data:
        json.dump(file, data)
        print("Okay")
else:
    print("ty shos poputav paren")
