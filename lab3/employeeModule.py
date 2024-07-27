import pandas as pd

# Function to add a new employee record
def add_employee(df, company_code, username, role, adhaar_no, pan_no):
    new_row = pd.DataFrame({
        'company_code': [company_code],
        'username': [username],
        'role': [role],
        'adhaar_no': [adhaar_no],
        'pan_no': [pan_no]
    })
    df = pd.concat([df, new_row], ignore_index=True)
    return df

# Function to delete an employee record
def delete_employee(df, company_code, username):
    condition = (df['company_code'] == company_code) & (df['username'] == username)
    if not df[condition].empty:
        df = df[~condition]
        return df
    else:
        return "Employee not found."

# Function to update an employee's role
def update_employee_role(df, company_code, username, new_role):
    condition = (df['company_code'] == company_code) & (df['username'] == username)
    if not df[condition].empty:
        df.loc[condition, 'role'] = new_role
        return df
    else:
        return "Employee not found."

# Function to retrieve all employees for a specific company code
def get_employees(df, company_code):
    condition = (df['company_code'] == company_code)
    employees = df[condition]
    if not employees.empty:
        return employees
    else:
        return "No employees found for the specified company."