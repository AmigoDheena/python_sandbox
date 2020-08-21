print('Hello World')
print(10 * 10)
print('x' * 10)

# Multiple assignment
x,y,name,boolean = (1,1.2,'Dheena', True)
print(x,y,name,boolean)


# name = input('What is your name? ')
# fav_color = input('What is your Favourite color? ')
# print(name + ' Likes ' + fav_color)

# birthyear = input('Your Birth year: ')
# age = 2020 - int(birthyear)
# print(type(age))
# print("Your age is: " + str(age))

mail_str = ''' 
Hi there,
This is test mail
Thank you.
'''
print(mail_str)

string = 'Python String'
print(string[0:6]) #Starts from 0
print(string[:6]) #Starts from 0

name = 'Dheena'
age = 27

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# f-strint(3.6+ only) 
print(f'My name is {name} and I am {age}')


fruits = ['apple','orange','grape','banana']
print(fruits[1])
fruits.append('mango')
print(fruits)
print(len(fruits))
fruits.remove('grape')
fruits.insert(2,'Cherry')
print(fruits)

# Tuples
testtuples = ('apple','orange','grape','banana')

print(testtuples,len(testtuples))

#Sets
set_fruits = {'apple','orange','grape','banana'}


# Dict

person = {
    'name': 'Dheena',
    'age': 27,
    'Country': 'India'
}
print(person['name'])