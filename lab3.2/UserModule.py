import pyqrcode
import png
from pyzbar.pyzbar import decode
from PIL import Image
import re

def get_user_input():
    data_dict = {
        "name": input("Enter name: "),
        "gender": input("Enter gender: "),
        "username": input("Enter username: "),
        "password": input("Enter password: "),
        "email": input("Enter email: "),
        "phone": input("Enter phone: ")
    }
    
    return data_dict

def encode_dict_to_qr(data_dict, filename='qr_code.png'):
    # Convert the dictionary to a string
    dict_str = ', '.join(f'{key}: {value}' for key, value in data_dict.items())
    
    # Generate the QR code
    qr_code = pyqrcode.create(dict_str)
    
    # Save the QR code as a PNG file
    qr_code.png(filename, scale=6)
    
    # Print the QR code to the terminal (optional)
    print(qr_code.terminal())

def decode_qr_code(filename):
    # Open the image file
    img = Image.open(filename)
    
    # Decode the QR code
    decoded_objects = decode(img)
    
    # Extract and return the data
    for obj in decoded_objects:
        data_str = obj.data.decode("utf-8")
        # Convert the string back to a dictionary
        data_dict = dict(item.split(": ") for item in data_str.split(", "))
        return data_dict
    
    return None

create_user_dict_lambda = lambda name, gender, username, password, email, phone: {
    "name": name,
    "gender": gender,
    "username": username,
    "password": password,
    "email": email,
    "phone": phone
}

add_user_to_list_lambda = lambda user_dict, user_list: user_list + [user_dict]

def add_user_to_list(user_dict, user_list):
    user_list.append(user_dict)
    return user_list

def show_users(user_list):
    for i in user_list:
        for k,v in i.items():
            print(k,v)
        print("* "*20)
def add_users_maunually(user_list):
    dict1 = get_user_input()
    add_user_to_list(dict1, user_list)

def smartScan(username, user_list):
    data_dict = decode_qr_code(username)
    add_user_to_list(data_dict,user_list)
    show_users(user_list)

def validation(data_dict):
    pattern = re.compile(r'[^a-zA-Z\s]')
    pattern2 = re.compile(r'r^\d{10}$')
    pattern3 = re.compile(r'[\s]')
    pattern4 = re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if (pattern.search(data_dict["name"])):
        return 1
    elif (pattern.search(data_dict["role"])):
        return 2
    elif (pattern2.search(data_dict["phone"])):
        return 3
    elif (pattern3.search(data_dict["username"])):
        return 4
    elif (pattern4.search(data_dict["email"])):
        return 5 
    else:
        return 0