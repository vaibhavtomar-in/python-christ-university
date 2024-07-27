import pandas as pd

# Function to add a new user record
def adduser(name_in, username_in, password_in, email_address_in, phone_no_in, df):
    new_data = {"name":name_in,"username" : username_in, "password":password_in,"email":email_address_in, "phone":phone_no_in}
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)
    return df


# Function to delete a user record
def deleteUser(attribute, value, df):
    df = df.loc[df[attribute]!=value]
    return df


# Function to delete a user record by username
def deleteUserByUsername(value,df):
    df = df.loc[df["username"]!=value]
    return df


# Function to update a user's info
def update_user_info(df, username, new_password=None, new_phone=None, new_email=None):
    # Check if the username exists in the DataFrame
    if username not in df['username'].values:
        return "Username not found."
    
    # Update the user's information
    if new_password:
        df.loc[df['username'] == username, 'password'] = new_password
    if new_phone:
        df.loc[df['username'] == username, 'phone'] = new_phone
    if new_email:
        df.loc[df['username'] == username, 'email'] = new_email
    
    return df