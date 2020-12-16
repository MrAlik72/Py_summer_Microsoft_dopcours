value = '6'
#if состоит из трех частей: if; логическое выражение value == '7'; обязательный символ двоеточия :.
if value == '6':
    print('The value is 6')
elif value == '8':#elif состоит из:elif; должен включает логическое выражение;завершаться символом двоеточия :.
        print('The value is 8')
elif value == '9':
    print('The value is 9')
else: #Оператор else состоит из двух частей:  ключевое слово else; символ двоеточия :.
    print('The value is not 6')
print('###################Finished!###############')
########################################################################
first_number = 5
vtoroy_number = 0
true_value = True
false_value = False
 
if first_number > 1 and first_number < 10:
    print('Значение находится между 1 и 10.')

if first_number > 1 or vtoroy_number < 1:
    print('По крайней мере одно значение больше 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and vtoroy_number < 10:
    print('Оба значения проходят тест')
else:
    print('Оба значения НЕ проходят тест')

####TASK###########
vvod=input('Would you like to continue? ')
if vvod=='n' or vvod=='no' or vvod=='нет' or vvod=='н':
    print('Exiting')
if vvod=='y' or vvod=='yes' or vvod=='да' or vvod=='д':
    print('Continuing ...')
    print('Complete!')
else :
    print('Please try again and respond with yes or no.')
