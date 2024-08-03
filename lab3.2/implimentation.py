import pyqrcode
import png
import UserModule
users = [{"name" : "vaibhav", "gender" : "M", "username" : "vaibhavtomar", "password" : "vaibhav@tomar", "email" : "vaibhavt1612003@gmail.com", "phone" : 8800700088}]

while(True):
    menu = '''
    to create new user(not add them to database) press 1
    to add a user using SmartScan press 2
    to fetch all users press 3
    to add users manually (without qr) press 4
    to exit code press 5 
    '''
    print(menu)
    option = int(input("enter your choice : "))
    print("* "*20)
    if(option == 1):
        data_dict=UserModule.get_user_input()
        UserModule.encode_dict_to_qr(data_dict,data_dict["username"]+".png")
        print("QR for user ",data_dict["username"]," is generated")
    elif(option == 2):
        try:
            username = input("enter the username of the user : ")
            UserModule.smartScan(username+".png", users)
        except:
            print("qr is not present")
    elif(option == 3):
        UserModule.show_users(users)
    elif(option == 4):
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        data_dict = UserModule.create_user_dict_lambda(name, gender, username, password, email, phone)
        UserModule.add_user_to_list_lambda(data_dict,users)
    elif(option == 5):
        break




