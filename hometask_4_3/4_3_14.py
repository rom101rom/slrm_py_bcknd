def dict_to_str(value, indent = 0):
    '''Function return string to dictionary'''
    res = []
    if isinstance(value, dict):
        for k, v in value.items():
            row = (f'\n{' ' * indent}{k}: {dict_to_str(v, indent + 2)}')
            res.append(row)
    elif isinstance(value, list):
        res.append(f' array= {value}')
    else: res.append(f'value= {value}')
    return ' '.join(res)


dict_to_str({'key': [1, 2, 3], 'key2': {'key1': 56, 'key2': [1, 2, 3, 4, 5], 'key3': {'key1': 56, 'key2': []}}})