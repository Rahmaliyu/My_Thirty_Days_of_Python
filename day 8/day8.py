dog = {}
dog['name'] = 'warrior'
dog['color'] ='black'
dog['breed'] = 'poodle'
dog['legs'] = 'long'
dog['age'] = '100'

student = {'first_name':'Audu',
            'last_name':'Lawi',
            'gender':'female',
            'age':'70',
            'is_married': True,
            'skills':['html' , 'c++', 'php', 'java'],
            'country':'Nigeria',
            'city':'Kano',
            'address':'No 1 Kurmi market Kano'
}
print('The lenght of the dictionary is : ', len(student))
print('the value of skills is : ', student.get('skills'), ' and its type is ', type(student['skills']))
student ['skills'].append ('Python')
print('Students skills after adding python ', student['skills'])
 
print('the list of keys in the dictionary is ', student.keys())
print('the list of values in the dictionary is ', student.values())
print('the list of tuples of the keysand values in the dictionary are ', student.items())

student.popitem()
print('the dictionary after deleting the last item is : ', student)

del dog