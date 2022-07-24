# def countes(word):
#     count = 0
#     for letter in word:
#         if letter == "e":
#             count +=1
            
#     print(count)
               
# countes("excellent")
# countes("natalya")
# countes("lightyearmovie")

# def countes(word):
#     count = 0
#     i = 0
#     while i < len(word):
#         if word[i] == "e":
#             count +=1
            
            
#         i += 1
#     print(count)
               
# countes("excellent")
# countes("natalya")
# countes("lightyearmovie")


# def repeatphrase():

#     counter = 1

#     while counter <= 5:
#         print(counter)

#         counter += 1
# repeatphrase()



# print(21 % 5) #modulos(outputs remainder) 
    

# student = ["John", 25, ["Math", "CompSci"]]
# # student.append(1)
# # print(student)
# # x = student.pop()
# # print(x)
# # print(student)

# dict = {'name': "John", 'age': 25}
# # dict['color'] = 'pink'
# # dict['name'] = 'June'
# dict.update({'color': 'pink', 'name': "June"})

# for k, v in dict.items():
#     print(k, v)

# def validlicenseplate(plate):
#     # print(plate)
#     # print(plate[0].isalpha())
#     # print(plate[1].isalpha())
#     # print(plate[-1])
#     # print(len(plate))
    
#     if (not plate[0].isalpha() or not plate[1].isalpha()):
#         return False
    
#     if (len(plate) > 6 or len(plate) < 2):
#         return False
    
#     firstDigitFound = False
#     for eachletter in plate[2:]:
#         if eachletter.isdigit() and not firstDigitFound:
#             firstDigitFound = True
#             if (eachletter == "0"):
#                 return False
#             #continue 
#         if (firstDigitFound and eachletter.isalpha()):
#             return False
        
#     for eachletter in plate[2:]:
#         if (eachletter in "!@#$%^&*()_+-=}[]{|\<>?/,.';:\" "):
#             return False
    
#     return True

# validlicenseplate("SSF,F7")
# validlicenseplate("S6g8F7")
# validlicenseplate("abSFF37")
# plate = "SFF337"
# print(f"{plate}:", validlicenseplate(plate))



# def tipcalculator():
#     price = remove_dollarsign(input('What is the price?: '))
#     tip = remove_percentagesign(input('What percentage do you want to tip?: '))
#     total = tip/100.00 * price
#     finaltotal = total + price
#     print('Total tip', total)
#     print('Final price', finaltotal)
    
# def remove_dollarsign(vname):
#     return float(vname.replace('$', ''))

# def remove_percentagesign(vaname):
#     return float(vaname.replace('%', ''))


# tipcalculator()



# def tipcalculator():
#     price = int(input('What is the price?: '))
#     tip = int(input('What percentage do you want to tip?: '))
#     total = tip/100.00 * price
#     finaltotal = total + price
#     print('Total tip', total)
#     print('Final price', finaltotal)
#     return finaltotal

# x = tipcalculator()
# print(x)


# def einstein():
#     m = input('Mass: ')
#     c = 300000000
#     E = int(m) * c * c
#     print(E)

# einstein()


# def lowercase():
#     phrase = input('Write phrase: ')
#     print(phrase.upper())

# lowercase()


# def lowercase():
#     phrase = input('Write phrase: ')
#     print(phrase.lower())

# lowercase()


# def nameages(name,age):

#     if age < 18:
#         print(name,'cant smoke or drink')
#     elif age < 21:
#         print(name,'cant drink')
#     else:
#         print(name,'can smoke and drink and ajay nibbles on natalya as much as he pleases, nobody else') 
    

# name = input('Put in a name: ')
# age =  input('Age: ')

# nameages(name, int(age))


# def basicwindow (width=5,height=10,font='TNR',bgc='w',scrollbar=True):
#     print(width,height,font,bgc)

# basicwindow()


# def simple (num1,num2=5):
#     print (num1, num2)

# simple(2)
# simple(5)


# def simpleaddition (num1, num2):
#     answer = num1 + num2
#     print ('num1 is',num1)
#     print ('num2 is',num2)
#     print (answer)

# simpleaddition (num2=5,num1=3)


# def example():
#     print('basic function')
#     z = 3 + 9
#     print(z)

# example()


# x = 50
# y = 10
# z = 22

# if x < y:
#     print('x is greater than y')

# elif x < z:
#     print('x is less than z')

# else:
#     print('if and elif(s) never ran')


# x = 2

# while x < 10:

#     print(x)

#     x = x+2


# if x < y:
#     print('x is less than y')

# if x < 55:
#     print('x is greater than 55')

# else:
#     print('x is not less than y')