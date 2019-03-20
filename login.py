users = {}
phone = {}
email = {}
Firstname = {}
lastname = {}
status = ""

def search():
   search = raw_input("Enter username to search: ")
   if search in users:
     print search, " phone ", phone[search]
     print search, " email ", email[search]
     print search, " Firstname ", Firstname[search]
     print search, " lastname ", lastname[search]

def createlogin():
  createLogin = raw_input("Create login name: ")

  if createLogin in users: # check if login name exist in the dictionary
     print "Login name already exist!\n"
  else:
     users[createLogin] = raw_input("Create password: ")
     phone[createLogin] = raw_input("Give phone: ")
     email[createLogin] = raw_input("Give email: ")
     Firstname[createLogin] = raw_input("Give Firstname: ")
     lastname[createLogin] = raw_input("Give lastname: ")
     print("\nUser created!\n")

def validate():
  login = raw_input("Enter login name: ")

  if login in users:
     passw = raw_input("Enter password: ")

     if login in users and passw == users[login]: # login matches password
         print "Login successful!\n"
         search()

  else:
      print
      print("User doesn't exist!\n")


while status != "q":
    status = raw_input("Are you a registered user? y/n? Press q to quit: ")  

    if status == "n": 
         createlogin()
    elif status == "y": 
        validate()
