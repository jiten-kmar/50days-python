def get_max():
    grades = [9.6, 9.2, 9.7]
    
    max_val=max(grades)
    min_val=min(grades)
    message = f"Max: {max_val}, Min: {min_val}"
    return message

val=get_max()
print(val)