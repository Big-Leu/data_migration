import sqlite3
def validate_input(data):
    required_keys = ['name', 'contact_number']
    
    # Check if all required keys are present
    if not all(key in data for key in required_keys):
        return False
    
    return True

data={'contact_number': '1234567890', 'name': 'John Doe', 'age': 30}
print(validate_input(data))