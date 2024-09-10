Input = input("Enter your text:\n") # To enter text

def phone_number(Input) : # To find numbers from text function 
    number_phone = set()
    for j in range(len(Input)) :
        if Input[j:j + 2] == "09" and Input[j:j + 11].isdigit() == True and len(Input[j:j + 11]) == 11 :
            number_phone.add(Input[j:j + 11])
    return number_phone

phone_number = phone_number(Input) # Put in the function variable 

def operators(phone_number) : # To understand the function operator
    List_operator = list() # List to put the number and name of the operator in it
    for i in phone_number :
        operator = "" 
        if i[0:4] == "0999" :
            operator =  f"Shuttle : {i}"
            List_operator.append(operator)
        elif i[0:3] == "091" or i[0:3] == "099" :
            operator = f"Hamrah aval : {i}"
            List_operator.append(operator)
        elif i[0:3] == "093" or i[0:3] == "094" or i[0:3] == "090" :
            operator =  f"Irancel : {i}"
            List_operator.append(operator)
        elif i[0:3] == "092" :
            operator =  f"Rightel : {i}"
            List_operator.append(operator)
        else :
            operator = f"The number {i} is not among any of the operators."
            List_operator.append(operator)
    return List_operator

operators = operators(phone_number) # Cast in function variable

if operators == [] : # If there is no number in the text
    operators = "Did you think you could put a hat on me? There are no numbers in the text."

print(f"\n\n{operators}")













