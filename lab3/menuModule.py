import pandas as pd
# Function to add a new menu item record
def add_menu_item(df, menu_code, company_code, item_name, diet, price_rs, quantity_gram):
    new_data = {
        'menu_code': menu_code,
        'company_code': company_code,
        'item_name': item_name,
        'diet': diet,
        'price_rs': price_rs,
        'quantity_gram': quantity_gram
    }
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)
    return df

# Function to delete a menu item record
def delete_menu_item(df, menu_code, company_code, item_name):
    condition = (df['menu_code'] == menu_code) & (df['company_code'] == company_code) & (df['item_name'] == item_name)
    if not df[condition].empty:
        df = df[~condition]
        return df
    else:
        return "Menu item not found."

# Function to increase price of all items in a menu by a certain percentage
def increase_price(df, menu_code, company_code, percentage):
    condition = (df['menu_code'] == menu_code) & (df['company_code'] == company_code)
    if not df[condition].empty:
        df.loc[condition, 'price_rs'] *= (1 + percentage / 100)
        return df
    else:
        return "No items found for the specified menu and company."
    
# Function to update diet type of a menu item
def update_diet_type(df, menu_code, company_code, item_name, new_diet):
    condition = (df['menu_code'] == menu_code) & (df['company_code'] == company_code) & (df['item_name'] == item_name)
    if not df[condition].empty:
        df.loc[condition, 'diet'] = new_diet
        return df
    else:
        return "Menu item not found."

# Function to get all items in a menu
def get_menu_items(df, menu_code, company_code):
    condition = (df['menu_code'] == menu_code) & (df['company_code'] == company_code)
    menu_items = df[condition]
    if not menu_items.empty:
        return menu_items
    else:
        return "No items found for the specified menu and company."
