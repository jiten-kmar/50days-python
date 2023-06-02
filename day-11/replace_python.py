import yaml

def replace_value_in_yaml(file_path, key_path, new_value):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Traverse the nested structure using the key path
    keys = key_path.split('.')
    current = data
    for key in keys[:-1]:
        current = current[key]
    
    # Replace the value at the specified key path
    current[keys[-1]] = new_value
    
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

# Usage example
replace_value_in_yaml('file.yaml', 'helm.sh/chart', 'jitender')

