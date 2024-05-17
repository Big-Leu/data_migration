import re

def sanitize_input(data):
    sanitized_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            sanitized_data[key] = sanitize_input(value)
        elif isinstance(value, list):
            value = ' '.join(str(item) for item in value)
            sanitized_data[key] = re.sub(r'\W+', '', value)
        else:
            sanitized_data[key] = re.sub(r'\W+', '', str(value))
    return sanitized_data

def validate_input(data):
    required_keys = ['name', 'contact_number']
    if not all(key in data for key in required_keys):
        return False
    
    return True

