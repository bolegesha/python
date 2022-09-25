import hashlib
import json


class Login:
    def __init__(self, log, password):
        self.log = log
        self.password = password

    @classmethod
    def log(cls):
        log = input("Enter your login: ")

        # Explanation is on 53-rd line
        password = hashlib.md5(input("Enter your password: ").encode('utf-8')).hexdigest()
        bool = False
        with open("db.json", "r+") as f:
            db = json.load(f)
            for i in db["users"]:
                if log == i["username"] and password == i["password"]:
                    print("Successfully logged in")
                    bool = True
                    break
            if bool != True:
                print("Wrong login or password, please try again")
        return cls(log, password)


class Registration:
    def __init__(self, name, surname, age, log, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.log = log
        self.password = password

        self.user_dict = {"username": self.log, "password": self.password, "name": self.name,
                          "surname": self.surname, "age": self.age}

        @property
        def get_name(self):
            return self.name

        @property
        def get_surname(self):
            return self.surname

        @property
        def get_age(self):
            return self.age

        @property
        def get_log(self):
            return self.log

        @property
        def get_pswd(self):
            return self.password

    def write_json(self, filename):
        with open("db.json", "r+") as f:
            data = json.load(f)
            data["users"].append(self.user_dict)
            f.seek(0)
            json.dump(data, f, indent=4)

    @classmethod
    def reg(cls):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        age = input("Enter your age: ")
        log = input("Create new login: ")

        # Instead of creating a method to hash password, I hash the password immediately on input
        password = hashlib.md5(input("Enter password: ").encode('utf-8')).hexdigest()

        return cls(name, surname, age, log, password)


class Changepswd:

    @classmethod
    def change(cls) -> object:
        log = input("Enter your login: ")
        pswd = hashlib.md5(input("Enter your password: ").encode('utf-8')).hexdigest()
        i = 0

        with open("db.json") as f:
            db = json.load(f)
            for users in db["users"]:
                i += 1
                bolean = False
                if log == users["log"]:
                    if log != users["username"] or pswd != users["password"]:
                        new_pswd = input("Write a new password: ")
                        new_pswd1 = input("Write a new password again: ")
                        if new_pswd == new_pswd1:
                            print("Password successfully changed")
                            bolean = True
                        break
                    if bolean != True:
                        print("Incorrect login or password, please try again")

        def upd_json(data):
            with open("db.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("db.json") as f:
                data = json.load(f)
                data["users"][i - 1]["password"] = new_pswd
                chng(data)

        return (pswd)


n = input('if you are already registered press 1, if not 0, to change password press 2: ')

if n == "1":
    Login.log()

elif n == "0":
    user = Registration.reg()
    user.write_json("db.json")

elif n == "2":
    chng = Changepswd.change()
    chng.upd_json()
