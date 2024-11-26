print("Registrati")
Usernameinput= input("Username: ")
Passwordinput= input("Password: ")
print("Registrazione effettuata")
while(True):
 print("Login")
 Logusinput= input("Username: ")
 Logpassinput= input("Password: ")
 if (Logusinput==Usernameinput) & (Logpassinput==Passwordinput):
    print("Accesso Effettuato")
    break
 else:
    print("Username o Password errata")