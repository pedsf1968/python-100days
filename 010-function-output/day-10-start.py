# function with output

def my_function():
    result = 3 * 2
    return result

# Store function result in value
output = my_function()
print(output)

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "ERROR: you must enter first and last name!"
    formated_f_name =  f_name.capitalize()
    formated_l_name =  l_name.capitalize()
    return  f"{formated_f_name} {formated_l_name}"

formated_string = format_name(input("What's your first name?: "), input("What's your last name?: "))
print(formated_string)