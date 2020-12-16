first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value 
print('Sum: ' + str(sum))
print('Difference: ' + str(difference))#% оператор модуля-дает остаток после деления.
print('Product: ' + str(product))    #Полезно определить, делится ли одно значение на другое без остатка.
print('Quotient: ' + str(quotient))  # **: оператор экспоненты. Например, "5 в четвертой степени", выражается как 5 * 5 * 5 * 5.
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))

####################################################################################
first_value = round(7.654321, 2)
print(first_value)
second_value = round(9.87654, 3)
print(second_value)
fahrenheit='5'#input('What is the temperature in fahrenheit? ')
if fahrenheit.isnumeric() == False:
    print('5')
elif fahrenheit.isnumeric()==True:
    fahrenheit=int(fahrenheit)
    celsius= float((fahrenheit - 32) * 5/9)
    print('Temperature in celsius is '+ str(celsius))
######################################################################################   
print('Simple calculator!')
per_chislo=input('First number? ')
operacia=input('Operation? ')
vtor_chislo=input('Second number? ')
if per_chislo.isnumeric()==True and vtor_chislo.isnumeric()==True :
    per_chislo=int(per_chislo)
    vtor_chislo=int(vtor_chislo)
    if operacia=='*' :
        print('product of '+str(per_chislo)+str(operacia)+str(vtor_chislo)+' equals '+str(per_chislo*vtor_chislo))
    if operacia=='/' :
        print('product of '+str(per_chislo)+str(operacia)+str(vtor_chislo)+' equals '+str(per_chislo/vtor_chislo))
    if operacia=='**' :
        print('product of '+str(per_chislo)+str(operacia)+str(vtor_chislo)+' equals '+str(per_chislo**vtor_chislo))     
    if operacia=='%' :    
        print('product of '+str(per_chislo)+str(operacia)+str(vtor_chislo)+' equals '+str(per_chislo%vtor_chislo))
    if operacia=='-' :
        print('product of '+str(per_chislo)+str(operacia)+str(vtor_chislo)+' equals '+str(per_chislo-vtor_chislo))
    if operacia=='+' :
        print('product of '+str(per_chislo)+str(operacia)+str(vtor_chislo)+' equals '+str(per_chislo+vtor_chislo))
    else :
        print('Operation not recognized.')

dict_values
