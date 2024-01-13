
def get_first_value(number_list):
    result=[]
    for num in number_list:
        if str(num).isnumeric:
           result.append(num) 
    print(result[0])
    return result
    

get_first_value([23,45,"ball", 56, "feet"])