def return_10():
    return 10

def add(num1,num2):
    return 1 + 2

def subtract(num1, num2):
    return 10 - 5

def multiply(num1, num2):
    return 4 * 2

def divide(num1, num2):
    return 10 / 2

def length_of_string(test_string):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)



def number_to_full_month_name(num):
    months = {
    1: "January",
    2: "February",
    3: "March", 
    4: "April",
    5: "May",
    6: "June", 
    7: "July",
    8: "August",
    9: "September"
}
    return months[num]

def number_to_short_month_name(num):
    months = {
    1: "Jan",
    2: "Feb",
    3: "Mar", 
    4: "Apr",
    5: "May",
    6: "Jun", 
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct"
}
    return months[num]

def length_width_height(num):
    return num * num * num


