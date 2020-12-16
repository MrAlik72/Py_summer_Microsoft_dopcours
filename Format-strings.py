fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string =  "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'
rrrseventhrr_string = r'A literal string with a \n new line character'

eleventh_string = """Another literal string
     on more than one line
using double quotes"""


i=input()
print(i)

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)
print(rrrseventhrr_string)
print(eleventh_string)
print(' ')
####
first = 'Conrad'
second = 'Grant'
third = 'Bob' 
print(first, second)
print(first, second, third)
print(first, second, third, sep='-')#аргумент sep. Он определяет символ, который будет использоваться для разделения строк по мере их сцепления для вывода.
print(first, second, third, sep='-', end='.')#аргумент end. Он определяет символ, который мы хотим использовать в самом конце последовательности.
