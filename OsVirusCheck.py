import random

CurrentSystem = 0
class system():
    def __init__(self, public_ip, wifiPass):
        self.public_ip = public_ip
        self.wifiPass = wifiPass


class Password():
    def __init__(self, Password):
        self.Password = Password
        self.Hash = ""
        self.HashString = "qwertyuioplkjhgfdsazxcvbnm,./;'[]=-0987654321`~!@#$%^&*()_+"
        for x in range(0, random.randint(0, 100)):
            self.Hash += random.choice(self.HashString)

class Server:
    def __init__(self, Passwords, systems, task, AdminIp, BannedIps):
        self.Passwords = Passwords
        self.systmes = systems
        self.task = task
        self.AdminIp = AdminIp
        self.BannedIps = BannedIps
    def Checkban(self, system):
        for x in range(0, len(self.BannedIps)):
            if(self.BannedIps[x] == system.public_ip):
                return True
            else:
                continue
        return False

class FireWall():
    def __init__(self, servers):
        self.servers = servers
    def KeepHistory(self, system):
        self.history = []
        self.history.append(system.public_ip + "" + "Joined")
    def AddHistory(self, system, action):
        self.history.append(action)


#use the 4th class variable to use for the server history, Also if you see some weird ban code in their i tried it and it did not work i will be adding more versions later on
MainServer = Server([], [], "", "123.213.10", [])
MainServerFireWall = FireWall([MainServer])

def RequestAccessToServerHistory():
    print("Warning if you enter the wrong ip we will log your ip and ban you, Type Exit to exit")
    Admin = input("Enter the Admin IP: ")
    if(Admin == MainServer.AdminIp):
        print(MainServerFireWall.history)
        Menu()
    elif(Admin == "Exit"):
        Menu()
    else:
        print("Invalid IP")
        if(CurrentSystem < len(MainServer.systmes)):
            MainServerFireWall.AddHistory(MainServer, str(MainServer.systmes[CurrentSystem].public_ip + "tried to access the server history"))
            MainServer.BannedIps.append(MainServer.systmes[CurrentSystem].public_ip)
            Menu()
        else:
            Menu()

def AddUser(system):
    pas2s = input("Enter a Server password: ")
    if(MainServer.Checkban(system) == True):
        print("You are have been banned")
        Menu()
    MainServer.Passwords.append(Password(pas2s))
    MainServer.systmes.append(system)
    MainServerFireWall.KeepHistory(system)
    Menu()
def CreateSystem():
    ip = input("Enter a public IP: ")
    wifi = input("Enter a wifi password: ")
    AddUser(system(ip, wifi))

def ChangeCurrentSystem():
    ip = input("Enter a public IP: ")
    for x in range(0, len(MainServer.systmes)):
        if(MainServer.systmes[x].public_ip == ip):
            CurrentSystem = x
            Menu()
    print("Invalid IP")
    Menu()

def Menu():
    if(len(MainServer.systmes) > 0):
        for x in range(0, len(MainServer.BannedIps)):
            if(MainServer.BannedIps[x] == MainServer.systmes[CurrentSystem].public_ip):
                print("You have been banned")
                Menu()
    Action = input("Enter a command: ")
    if(Action == "AddUser"):
        CreateSystem()
    elif(Action == "Request Access To Server History"):
        RequestAccessToServerHistory()
    elif(Action == "Change Current System"):
        ChangeCurrentSystem()
    else:
        print("Invalid Command")
        Menu()
Menu()




