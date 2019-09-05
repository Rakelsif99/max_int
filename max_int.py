#The user repeatedly inputs numbers until a negative value is entered
num_int = int(input("Input a number: "))    
max_num = 0
while num_int >= 0:
    if num_int >= max_num:
        max_num = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_num) 